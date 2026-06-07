import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

EXCLUDE_DIRS = {
    "__pycache__",
    ".git",
    "node_modules",
    "venv",
    ".venv",
    "dist",
    "build"
}

EXCLUDE_EXTENSIONS = {
    ".pyc"
}

def print_tree(start_path, prefix=""):
    items = sorted(os.listdir(start_path))

    items = [
        item for item in items
        if item not in EXCLUDE_DIRS
        and not any(item.endswith(ext) for ext in EXCLUDE_EXTENSIONS)
    ]

    for index, item in enumerate(items):
        path = os.path.join(start_path, item)
        connector = "└── " if index == len(items) - 1 else "├── "

        print(prefix + connector + item)

        if os.path.isdir(path):
            extension = "    " if index == len(items) - 1 else "│   "
            print_tree(path, prefix + extension)

print(os.path.basename(os.getcwd()))
print_tree(os.getcwd())