from os import path
from utils.operation_with_files import read_file_line_by_line

__author__ = 'm_shalamov'

FILE_PATH = 'source/string_data_one.txt'


def find_world_with_max_len():
    file_path = path.relpath(FILE_PATH)
    read_line = read_file_line_by_line(file_path)

    source_string = read_line.next().replace('.', '')
    source_list = source_string.split(' ')

    world_max_len = len(max(source_list, key=lambda i: len(i)))

    result = []

    for source_item in source_list:
        if len(source_item) >= world_max_len:
            result.append(source_item)

    for result_item in result:
        print result_item


if __name__ == '__main__':
    find_world_with_max_len()