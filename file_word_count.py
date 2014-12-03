"""
This short script counts a number of files in a given folder.
Also it counts total number of words in all files of a given folder.
All files on folder should be text files.
"""
import os
import sys


def file_word_count(folder):
    """

    :param folder: Target folder path. Must be accessible for reading for current user.
    :return: (File count, Words count)
    """

    file_list = os.listdir(folder)

    total_word_count = 0
    file_count = 0

    for text_file in file_list:
        file_path = os.path.join(folder, text_file)

        if os.path.isfile(file_path):
            file_count += 1

            with open(file_path) as f:
                content = f.read()
                total_word_count += len(content.split())

    return file_count, total_word_count


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write('This util needs some input: ./file_word_count.py "/Path/to/target/folder"\n')
        sys.exit()

    folder = sys.argv[1]

    if not os.access(folder, os.R_OK):
        sys.stderr.write('Sorry! I have no rights to read given folder\n'
                         'Please check permissions\n')
        sys.exit()

    file_count, total_word_count = file_word_count(folder)
    sys.stdout.write('Totally {} files in given folder\n'.format(file_count))
    sys.stdout.write('Totally {} words in all files of a given folder\n'.format(total_word_count))