#!/usr/bin/env python3

import sys
from pathlib import Path

from wc import wc_all, wc_byte, wc_word, wc_line, wc_stdin, wc_char


def get_option():
    option = sys.argv[1] if len(sys.argv) > 2 else ''
    return option


def get_filepath():
    filepath = ''

    if len(sys.argv) > 2:
        filepath = Path(sys.argv[2])
    elif len(sys.argv) == 3:
        filepath = sys.argv[1]
    else:
        filepath = None
    return filepath


OPTION = get_option()
FILE_PATH = get_filepath()


options = {
    '-c': wc_byte,
    '-l': wc_line,
    '-w': wc_word,
    '-m': wc_char,
    '': wc_all
    }


def execute():
    if OPTION and FILE_PATH:
        print(options[OPTION](FILE_PATH))
    else:
        wc_stdin(options[OPTION])


if __name__ == '__main__':
    execute()
