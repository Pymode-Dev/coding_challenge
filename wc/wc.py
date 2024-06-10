#!/usr/bin/env python3
"""
wc - word count tool from unix OS
"""
import sys

from pathlib import Path


def read_file(filepath, mode: str, line=False, e=None):
    try:
        with open(filepath, mode=mode, encoding=e) as f:
            if line:
                file_reader = f.readlines()
            else:
                file_reader = f.read()
            return file_reader
    except FileNotFoundError:
        print(f"[FileNotFoundError] the file {filepath} does not exist.")
        sys.exit(0)


def wc_byte(filepath: Path) -> int:
    if isinstance(filepath, bytes):
        return len(filepath)
    output = read_file(filepath,"rb")
    return len(output)


def wc_line(filepath: Path) -> int:
    if isinstance(filepath, bytes):
        return len(filepath.decode().strip().split('\n'))
    else:
        file_reader = read_file(filepath, "rb", True)
    return len(file_reader)


def wc_char(filepath: Path) -> int:
    if isinstance(filepath, bytes):
        return len("".join(filepath.decode().split('\r\n\" "')))
    file_reader = read_file(filepath, "r", e="utf-8")
    return sum([len(i) for i in file_reader.split("\r\n")])


def wc_word(filepath: Path) -> int:
    if isinstance(filepath, bytes):
        return len(filepath.decode().split())
    file_reader = read_file(filepath, "r", e="utf-8")
    return len(file_reader.split())


def wc_all(filepath: Path):
    byte_read = wc_byte(filepath)
    line_read = wc_line(filepath)
    word_read = wc_word(filepath)
    return (f"{line_read} {word_read} {byte_read} {'' if isinstance(filepath, bytes) else filepath}")
