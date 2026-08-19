"""Small helpers for structured output and run provenance."""

from __future__ import annotations

import hashlib
import json
import os
import platform
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def sha256_file(path: Path) -> str:
    """Identify file contents without storing another copy."""

    digest = hashlib.sha256()
    with path.open("rb") as input_file:
        for block in iter(lambda: input_file.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def git_code_state(script_path: Path) -> tuple[str | None, bool | None]:
    """Identify the Git revision and whether the analysis script differs."""

    try:
        repository = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=script_path.parent,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        revision = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repository,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        status = subprocess.run(
            ["git", "status", "--porcelain", "--", str(script_path)],
            cwd=repository,
            check=True,
            capture_output=True,
            text=True,
        ).stdout
        return revision, bool(status.strip())
    except (OSError, subprocess.CalledProcessError):
        return None, None


def write_json(path: Path, document: dict[str, object]) -> None:
    """Write completely before atomically replacing a JSON file."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False
    ) as output_file:
        json.dump(document, output_file, indent=2, sort_keys=True)
        output_file.write("\n")
        temporary_path = Path(output_file.name)
    try:
        os.replace(temporary_path, path)
    finally:
        temporary_path.unlink(missing_ok=True)


def run_manifest(
    *,
    script_path: Path,
    measurements_path: Path,
    config_path: Path,
    output_path: Path,
    accepted_quality_flags: frozenset[str],
    calibration_offset_celsius: float,
    command: list[str],
) -> dict[str, object]:
    """Record the facts needed to audit and rerun this small analysis."""

    revision, dirty = git_code_state(script_path)
    return {
        "schema_version": 1,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "command": command,
        "code": {
            "file": script_path.name,
            "sha256": sha256_file(script_path),
            "git_revision": revision,
            "dirty": dirty,
        },
        "input": {
            "file": measurements_path.name,
            "sha256": sha256_file(measurements_path),
        },
        "configuration": {
            "file": config_path.name,
            "sha256": sha256_file(config_path),
            "parameters": {
                "accepted_quality_flags": sorted(accepted_quality_flags),
                "calibration_offset_celsius": calibration_offset_celsius,
            },
        },
        "environment": {
            "python_implementation": platform.python_implementation(),
            "python_version": platform.python_version(),
            "platform": platform.platform(),
        },
        "output": {
            "file": output_path.name,
            "sha256": sha256_file(output_path),
        },
    }
