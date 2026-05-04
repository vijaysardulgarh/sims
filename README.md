md sims

cd sims

md backend
md frontend

cd backend

python -m venv venv

venv\bin\activate

python -m pip install --upgrade pip

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
