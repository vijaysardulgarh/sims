#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

# -----------------------------
# Configuration
# -----------------------------
APP_NAME="sims"
PROJECT_DIR="/home/vijaysardulgarh/sims"
VENV_DIR="$PROJECT_DIR/venv"
DJANGO_SETTINGS_MODULE="sims.settings"
GUNICORN_SOCK="/run/$APP_NAME.sock"
USER="vijaysardulgarh"
GROUP="www-data"
NUM_WORKERS=3
BIND="unix:$GUNICORN_SOCK"
DJANGO_MANAGE="$VENV_DIR/bin/python $PROJECT_DIR/manage.py"

# -----------------------------
# Update & pull latest code
# -----------------------------
echo ">>> Pulling latest code..."
cd $PROJECT_DIR
git pull origin main

# -----------------------------
# Install dependencies
# -----------------------------
echo ">>> Installing dependencies..."
$VENV_DIR/bin/pip install --upgrade pip
$VENV_DIR/bin/pip install -r requirements.txt

# -----------------------------
# Run migrations & collectstatic
# -----------------------------
echo ">>> Applying database migrations..."
$DJANGO_MANAGE migrate --noinput

echo ">>> Collecting static files..."
$DJANGO_MANAGE collectstatic --noinput

# -----------------------------
# Fix permissions
# -----------------------------
echo ">>> Setting permissions..."
sudo chown -R $USER:$GROUP $PROJECT_DIR
sudo chmod -R 755 $PROJECT_DIR

# -----------------------------
# Restart Gunicorn
# -----------------------------
echo ">>> Restarting Gunicorn..."
sudo systemctl daemon-reload
sudo systemctl restart gunicorn

# -----------------------------
# Restart Nginx
# -----------------------------
echo ">>> Restarting Nginx..."
sudo systemctl restart nginx

echo ">>> Deployment complete!"
