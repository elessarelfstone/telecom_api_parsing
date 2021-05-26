import csv
from pathlib import Path
from typing import Tuple


def append_file(fpath, data):
    """ Add new line to file"""
    with open(fpath, 'a+', encoding="utf8") as f:
        f.write(data + '\n')


def read_lines(fpath):
    """ Return rows of file as list """
    with open(fpath, "r", encoding="utf-8") as f:
        lines = [b.rstrip() for b in f.readlines()]

    return lines


def read_tsv(tsv_fpath: str):
    rows = []
    with open(tsv_fpath) as f:
        rd = csv.reader(f, delimiter="\t", quotechar='"')
        for row in rd:
            rows.append(tuple(row))

    return rows


def replace_fext(fpath, ext):
    return Path(fpath).with_suffix(ext)


def build_fpath(fpath: str, fname: str, ext: str, suff=None) -> str:
    _suff = f'_{suff}' if suff else ''
    return str(Path(fpath).joinpath(f'{fname}{_suff}').with_suffix(ext))