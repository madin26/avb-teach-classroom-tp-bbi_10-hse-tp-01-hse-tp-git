#!/bin/bash

if [[ "$#" -lt 2 ]]; then
  echo "Usage: ./collect_files.sh in_dir out_dir [--max_depth N]"
  exit 1
fi

in_dir="$1"
out_dir="$2"
arg3="$3"
arg4="$4"

echo "Running Python script..."

if [[ "$arg3" == "--max_depth" && -n "$arg4" ]]; then
  python3 collect_files.py "$in_dir" "$out_dir" "$arg3" "$arg4"
else
  python3 collect_files.py "$in_dir" "$out_dir"
fi
