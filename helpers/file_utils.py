"""
    generator create_file_gen
"""

from pathlib import Path
from typing import Iterator


def create_file_gen(filepath: Path) -> Iterator[str]:
    with filepath.open("rt", encoding="utf-8") as fin:
        for line in fin:
            yield line.strip()
