import os

# ============================================================
# CONFIG
# ============================================================

PROJECT_ROOT = r"."

STRUCTURE_FILE = "django_structure.txt"
CODE_FILE = "django_code.txt"

INCLUDE_EXTENSIONS = {
    ".py",
    ".json",
    ".yaml",
    ".yml",
    ".env",
    ".txt",
}

EXCLUDE_DIRS = {
    "__pycache__",
    ".git",
    ".idea",
    ".vscode",
    "venv",
    "env",
    "staticfiles",
    "media",
    "node_modules",
    "migrations",
}

# ============================================================
# EXPORT STRUCTURE
# ============================================================

with open(STRUCTURE_FILE, "w", encoding="utf-8") as f:

    for root, dirs, files in os.walk(PROJECT_ROOT):

        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        level = root.replace(PROJECT_ROOT, "").count(os.sep)

        indent = "│   " * level

        f.write(f"{indent}├── {os.path.basename(root)}\n")

        for file in sorted(files):
            f.write(f"{indent}│   ├── {file}\n")

# ============================================================
# EXPORT CODE
# ============================================================

with open(CODE_FILE, "w", encoding="utf-8") as output:

    for root, dirs, files in os.walk(PROJECT_ROOT):

        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file in sorted(files):

            ext = os.path.splitext(file)[1]

            if ext not in INCLUDE_EXTENSIONS:
                continue

            filepath = os.path.join(root, file)

            try:

                with open(filepath, "r", encoding="utf-8") as source:

                    output.write("\n\n")
                    output.write("# ============================================================\n")
                    output.write(f"# FILE: {filepath}\n")
                    output.write("# ============================================================\n\n")

                    output.write(source.read())
                    output.write("\n")

            except Exception as e:

                output.write("\n\n")
                output.write("# ============================================================\n")
                output.write(f"# ERROR: {filepath}\n")
                output.write("# ============================================================\n")
                output.write(str(e))
                output.write("\n")

print("Done!")
print("Generated:")
print("-", STRUCTURE_FILE)
print("-", CODE_FILE)