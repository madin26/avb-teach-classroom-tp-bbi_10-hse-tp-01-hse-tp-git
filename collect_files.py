import os
import sys
import shutil

args = sys.argv[1:]

if len(args) < 2:
    print("Usage: collect_files.py in_dir out_dir [--max_depth N]")
    sys.exit(1)

in_dir = args[0]
out_dir = args[1]
max_depth = None

if len(args) == 4 and args[2] == "--max_depth":
    try:
        max_depth = int(args[3])
    except ValueError:
        print("Error: max_depth must be an integer")
        sys.exit(1)

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

names = {}

for root, dirs, files in os.walk(in_dir):
    rel_path = os.path.relpath(root, in_dir)
    depth = rel_path.count(os.sep)

    if rel_path == '.':
        depth = 0

    if max_depth is not None and depth >= max_depth:
        continue

    for file in files:
        source_path = os.path.join(root, file)
        base_name, ext = os.path.splitext(file)

        if file in names:
            count = names[file]
            new_name = f"{base_name}{count}{ext}"
            names[file] += 1
        else:
            new_name = file
            names[file] = 1

        target_path = os.path.join(out_dir, new_name)
        shutil.copy2(source_path, target_path)
