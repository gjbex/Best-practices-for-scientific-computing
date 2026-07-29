#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
template_dir="${script_dir}/demo_repository"

if (( $# > 1 )); then
    echo "Usage: $0 [empty-target-directory]" >&2
    exit 2
fi

if (( $# == 1 )); then
    target_dir="$1"
    if [[ -e "$target_dir" && ! -d "$target_dir" ]]; then
        echo "Error: target exists and is not a directory: $target_dir" >&2
        exit 2
    fi
    mkdir -p -- "$target_dir"

    shopt -s nullglob dotglob
    target_contents=("$target_dir"/*)
    shopt -u nullglob dotglob
    if (( ${#target_contents[@]} > 0 )); then
        echo "Error: target directory is not empty: $target_dir" >&2
        exit 2
    fi
else
    target_dir="$(mktemp -d "${TMPDIR:-/tmp}/version-control-demo.XXXXXX")"
fi

cp -R -- "${template_dir}/." "$target_dir/"

git -C "$target_dir" init --quiet
git -C "$target_dir" config user.name "Version Control Demo"
git -C "$target_dir" config user.email "version-control-demo@example.invalid"
git -C "$target_dir" add README.md check_result.py measurements.csv \
    temperature_analysis.py
git -C "$target_dir" \
    -c commit.gpgsign=false \
    -c core.hooksPath=/dev/null \
    commit --quiet -m "Add reproducible temperature analysis"

printf '%s\n' "$target_dir"
