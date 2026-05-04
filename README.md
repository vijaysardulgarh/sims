md sims

cd sims

python -m venv venv

venv\bin\activate

python -m pip install --upgrade pip

pip install django

Create a .gitignore File

          # Environments
          venv/
          env/
          
          # Python
          *.pyc
          __pycache__/
          
          # Django
          db.sqlite3
          *.media/
          
          # Secrets / Environment Variables
          .env      

dfdfd          
