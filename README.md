md sims

cd sims

md backend
md frontend

cd backend

python -m pip install --upgrade pip

python -m venv venv

venv\scripts\activate

pip install django

Create a .gitignore File

          # Python/Django
          venv/
          env/
          *.pyc
          __pycache__/
          db.sqlite3
          *.media/
          .env
          
          # Frontend (React/Vue/etc.)
          node_modules/
          dist/
          build/    

git init          

git remote add origin https://github.com/vijaysardulgarh/sims.git

git push -u origin main

django-admin startproject sims .

Commands for pushing files to github

          git add .
          git commit -m "your message"
          git push
