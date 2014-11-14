from os import path
from utils.operation_with_files import read_file_line_by_line

__author__ = 'm_shalamov'

FILE_PATH = 'source/string_data_one.txt'
REFERENCE = ['A', 'E', 'I', 'O', 'U', 'Y']


def count_number_vowels():
    file_path = path.relpath(FILE_PATH)
    read_line = read_file_line_by_line(file_path)

    source_string = read_line.next()
    source_list = source_string.split(' ')

    temp, result, char_count = '', '', 0

    for source_item in source_list:
        char_list = list(source_item.upper())
        for char_item in char_list:
            if char_item in REFERENCE:
                temp += char_item
        if len(temp) > len(result):
            result = temp
            char_count = len(result)
        temp = ''

    print result + ' ' + str(char_count)


if __name__ == '__main__':
    count_number_vowels()