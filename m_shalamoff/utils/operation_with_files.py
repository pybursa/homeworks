__author__ = 'm_shalamov'

from os import path


def read_file_line_by_line(file_path):
    with open(path.relpath(file_path), 'r') as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            yield line


def get_string_line(file_path):
    read_line = read_file_line_by_line(file_path)
    return read_line.next()
