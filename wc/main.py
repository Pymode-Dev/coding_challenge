#!/usr/bin/env python3

import re
import sys

from argparse import ArgumentParser, FileType
from pathlib import Path

from wc import wc_all, wc_byte, wc_word, wc_line, wc_char


def parser():
    args = ArgumentParser(
        prog="wc",
        description="count words, lines, characters, and bytes in a file",
        epilog="Thanks for using wc"
    )
    args.add_argument("file", type=FileType('r'), default=sys.stdin, nargs="?")
    args.add_argument("-l", help="Count lines in a file", action='store_true')
    args.add_argument("-c", help="Count bytes in a file", action='store_true')
    args.add_argument("-m", help="Count characters in a file", action='store_true')
    args.add_argument("-w", help="Count words in a file", action='store_true')
    args.add_argument("-v", action="version", version="%(prog)s 1.0")

    return args.parse_args()


options = {
    '-c': wc_byte,
    '-l': wc_line,
    '-w': wc_word,
    '-m': wc_char,
    '': wc_all
    }


def execute():
    args = parser()
    funct = args.__dict__.items()
    opt = [k for k, v in funct if v is True]
    option = f"-{opt[0]}" if opt != [] else ''

    file = args.file.name

    if file == '<stdin>':
        print(options[option](sys.stdin.read().encode()))
    else:
        print(options[option](file))

    

if __name__ == '__main__':
    execute()