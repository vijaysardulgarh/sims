@echo off

echo =====================================
echo DELETING SQLITE DATABASE
echo =====================================

del db.sqlite3

echo =====================================
echo DELETING MIGRATIONS
echo =====================================

for /d /r %%d in (migrations) do (

    del "%%d\0*.py" >nul 2>&1

    del "%%d\0*.pyc" >nul 2>&1
)

echo =====================================
echo MAKEMIGRATIONS
echo =====================================

python manage.py makemigrations

echo =====================================
echo MIGRATE
echo =====================================

python manage.py migrate

echo =====================================
echo CREATE SUPERUSER
echo =====================================

python manage.py createsuperuser