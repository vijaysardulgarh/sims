#!/bin/bash

echo "====================================="
echo "DJANGO SAFE RESET SCRIPT"
echo "====================================="

PROJECT_ROOT=$(pwd)

echo "Project Root: $PROJECT_ROOT"


echo ""
echo "====================================="
echo "SQLITE DATABASE TO DELETE"
echo "====================================="

if [ -f "$PROJECT_ROOT/db.sqlite3" ]; then
    echo "$PROJECT_ROOT/db.sqlite3"
else
    echo "No db.sqlite3 found"
fi


echo ""
echo "====================================="
echo "MIGRATION FILES TO DELETE"
echo "====================================="

find "$PROJECT_ROOT" \
    -path "$PROJECT_ROOT/venv" -prune -o \
    -path "*/migrations/*.py" \
    ! -name "__init__.py" \
    -type f \
    -print

find "$PROJECT_ROOT" \
    -path "$PROJECT_ROOT/venv" -prune -o \
    -path "*/migrations/*.pyc" \
    -type f \
    -print


echo ""
echo "====================================="
echo "__pycache__ FOLDERS TO DELETE"
echo "====================================="

find "$PROJECT_ROOT" \
    -path "$PROJECT_ROOT/venv" -prune -o \
    -type d \
    -name "__pycache__" \
    -print


echo ""
echo "====================================="
echo "CONFIRM DELETE?"
echo "====================================="

read -p "Type YES to continue: " CONFIRM


if [ "$CONFIRM" != "YES" ]; then
    echo ""
    echo "Operation cancelled."
    exit 1
fi


echo ""
echo "====================================="
echo "DELETING SQLITE DATABASE"
echo "====================================="

rm -f "$PROJECT_ROOT/db.sqlite3"


echo ""
echo "====================================="
echo "DELETING MIGRATION FILES"
echo "====================================="

find "$PROJECT_ROOT" \
    -path "$PROJECT_ROOT/venv" -prune -o \
    -path "*/migrations/*.py" \
    ! -name "__init__.py" \
    -type f \
    -delete

find "$PROJECT_ROOT" \
    -path "$PROJECT_ROOT/venv" -prune -o \
    -path "*/migrations/*.pyc" \
    -type f \
    -delete


echo ""
echo "====================================="
echo "DELETING __pycache__"
echo "====================================="

find "$PROJECT_ROOT" \
    -path "$PROJECT_ROOT/venv" -prune -o \
    -type d \
    -name "__pycache__" \
    -exec rm -rf {} +


echo ""
echo "====================================="
echo "RUNNING MAKEMIGRATIONS"
echo "====================================="

python manage.py makemigrations


echo ""
echo "====================================="
echo "RUNNING MIGRATE"
echo "====================================="

python manage.py migrate


echo ""
echo "====================================="
echo "CREATE SUPERUSER"
echo "====================================="

python manage.py createsuperuser