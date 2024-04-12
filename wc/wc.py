#!/usr/bin/env python3
"""
wc - word count tool from unix OS
"""
import sys

from pathlib import Path


def wc_byte(filepath: Path) -> int:
    with open(filepath, mode="rb") as f:
        file_reader = f.read()
        return len(file_reader)


def wc_line(filepath: Path) -> int:
    with open(filepath, mode="rb") as f:
        file_reader = f.readlines()
        return len(file_reader)


def wc_char(filepath: Path) -> int:
    with open(filepath, mode="rb") as f:
        file_reader = f.read()
        return len(file_reader)


def wc_word(filepath: Path) -> int:
    with open(filepath, mode="rb") as f:
        file_reader = f.read().split()
        return len(file_reader)


def wc_all(filepath: Path):
    byte_read = wc_byte(filepath)
    line_read = wc_line(filepath)
    word_read = wc_word(filepath)
    return f"{line_read} {word_read} {byte_read} {filepath}"


def wc_stdin(func):
    for line in sys.stdin:
        return func(line.strip())
