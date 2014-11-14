__author__ = 'm_shalamov'


def read_file_line_by_line(file_path):
    with open(file_path, 'r') as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            yield line
