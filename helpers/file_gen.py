"""
    generator file_gen
"""

from pathlib import Path


def create_file_gen(filepath: Path):
    with filepath.open("rt", encoding="utf-8") as fin:
        for line in fin:
            yield line
