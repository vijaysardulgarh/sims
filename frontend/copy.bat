find . \
-path "./node_modules" -prune -o \
-path "./.venv" -prune -o \
-path "./dist" -prune -o \
-path "./build" -prune -o \
\( -name "*.js" -o -name "*.jsx" -o -name "*.py" \) \
-type f -print | while read file; do

echo ""
echo "=================================================="
echo "FILE: $file"
echo "=================================================="

cat "$file"

done > full_project.txt