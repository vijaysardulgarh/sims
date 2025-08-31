#!/bin/bash

# Variables
DOMAIN="vijaysardulgarh.com"
IP="34.131.65.194"
USER="vijaysardulgarh"
PROJECT_NAME="sims"
GITHUB_REPO="https://github.com/vijaysardulgarh/sims.git"

# Directories
PROJECT_DIR="/home/$USER/$PROJECT_NAME"
SOCKET_FILE="/run/$PROJECT_NAME.gunicorn.sock"
NGINX_SOCKET_FILE="/etc/systemd/system/$PROJECT_NAME.gunicorn.socket"
NGINX_SERVICE_FILE="/etc/systemd/system/$PROJECT_NAME.gunicorn.service"
NGINX_CONFIG_DIR="/etc/nginx/sites-available"
NGINX_SITES_ENABLED_DIR="/etc/nginx/sites-enabled"
GUNICORN_BIN="$PROJECT_DIR/venv/bin/gunicorn"

# Adjust if your Django app is not 'school'
GUNICORN_WSGI="school.wsgi:application"
DATABASE_FILE="$PROJECT_DIR/db.sqlite3"

echo "===== Deploying $PROJECT_NAME ====="

# Clone or pull project from GitHub
if [ -d "$PROJECT_DIR/.git" ]; then
    echo "Pulling latest changes..."
    cd $PROJECT_DIR && git pull origin main
else
    echo "Cloning repository..."
    git clone $GITHUB_REPO $PROJECT_DIR
fi

# Create virtual environment
if [ ! -d "$PROJECT_DIR/venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $PROJECT_DIR/venv
fi

# Activate virtual environment
source $PROJECT_DIR/venv/bin/activate

# Install project dependencies
echo "Installing project dependencies..."
pip install --upgrade pip
pip install -r $PROJECT_DIR/requirements.txt

# Run migrations
echo "Running migrations..."
python3 $PROJECT_DIR/manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python3 $PROJECT_DIR/manage.py collectstatic --noinput

# Ensure database file permissions (if SQLite)
if [ -f "$DATABASE_FILE" ]; then
    sudo chown $USER:$USER $DATABASE_FILE
    sudo chmod 664 $DATABASE_FILE
    echo "Database permissions updated."
fi


# Check if the database file exists
if [ ! -f "$DATABASE_FILE" ]; then
    echo "Error: Database file '$DATABASE_FILE' not found."
    exit 1
fi

# Change the permissions of the database file
sudo chown $USER:$USER $DATABASE_FILE
sudo chmod 664 $DATABASE_FILE

echo "Permissions of '$DATABASE_FILE' have been changed successfully."

# Install Gunicorn
echo "Installing Gunicorn..."
pip install gunicorn

# Deactivate virtual environment
deactivate

# Create Gunicorn socket file
echo "Creating Gunicorn socket file..."
cat << EOF | sudo tee $NGINX_SOCKET_FILE
[Unit]
Description=$PROJECT_NAME.gunicorn socket

[Socket]
ListenStream=$SOCKET_FILE

[Install]
WantedBy=sockets.target
EOF

# Create Gunicorn service file
echo "Creating Gunicorn service file..."
cat << EOF | sudo tee $NGINX_SERVICE_FILE
[Unit]
Description=$PROJECT_NAME.gunicorn daemon
Requires=$PROJECT_NAME.gunicorn.socket
After=network.target

[Service]
User=$USER
Group=$USER
WorkingDirectory=$PROJECT_DIR
ExecStart=$GUNICORN_BIN --access-logfile - --workers 3 --bind unix:$SOCKET_FILE $GUNICORN_WSGI

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd and enable services
echo "Reloading systemd..."
sudo systemctl daemon-reload
sudo systemctl enable $PROJECT_NAME.gunicorn.socket
sudo systemctl start $PROJECT_NAME.gunicorn.socket
sudo systemctl enable $PROJECT_NAME.gunicorn.service
sudo systemctl start $PROJECT_NAME.gunicorn.service

# Remove existing Nginx configuration file if it exists
if [ -f "$NGINX_CONFIG_DIR/$DOMAIN" ]; then
    echo "Removing existing Nginx config..."
    sudo rm "$NGINX_CONFIG_DIR/$DOMAIN"
fi

# Create new Nginx configuration
echo "Creating Nginx configuration..."
cat << EOF | sudo tee $NGINX_CONFIG_DIR/$DOMAIN
server {
    listen 80;
    listen [::]:80;
    server_name $DOMAIN www.$DOMAIN $IP;

    location = /favicon.ico { access_log off; log_not_found off; }

    location / {
        proxy_set_header Host \$http_host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_pass http://unix:$SOCKET_FILE;
    }

    location /static/ {
        alias $PROJECT_DIR/static/;
    }

    location /media/ {
        alias $PROJECT_DIR/media/;
    }
}
EOF



# Enable Nginx site
if [ -L "$NGINX_SITES_ENABLED_DIR/$DOMAIN" ]; then
    echo "Removing old symlink..."
    sudo rm "$NGINX_SITES_ENABLED_DIR/$DOMAIN"
fi
sudo ln -s "$NGINX_CONFIG_DIR/$DOMAIN" "$NGINX_SITES_ENABLED_DIR/$DOMAIN"

# Test and reload Nginx
echo "Testing and restarting Nginx..."
sudo nginx -t && sudo systemctl restart nginx

# Install Certbot and setup HTTPS
echo "Setting up SSL with Certbot..."
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d $DOMAIN -d www.$DOMAIN --non-interactive --agree-tos -m admin@$DOMAIN

# Fix project ownership
sudo chown -R $USER:$USER $PROJECT_DIR


echo "Restarting Gunicorn service..."
sudo systemctl restart sims.gunicorn.service



echo "===== Deployment of $PROJECT_NAME completed successfully! ====="


