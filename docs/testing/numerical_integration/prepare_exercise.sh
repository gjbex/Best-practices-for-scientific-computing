#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
starter_dir="${script_dir}/starter"
reference_dir="${script_dir}/reference_implementation"

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
    target_dir="$(mktemp -d "${TMPDIR:-/tmp}/integration-exercise.XXXXXX")"
fi

cp -- "${reference_dir}/integration.py" "$target_dir/"
cp -- "${starter_dir}/test_integration.py" "$target_dir/"

printf '%s\n' "$target_dir"
