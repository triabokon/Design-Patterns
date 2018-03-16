"""
Read data from file
"""


def read_file(path):
    text_file = open(path, "r")
    lines = text_file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = lines[i].split(',')
    text_file.close()
    return lines


def write_file(path, lines):
    text_file = open(path, "w")
    for line in lines:
        str_line = line[0] + ',' + str(line[1]) + '\n'
        text_file.write(str_line)
    text_file.close()


