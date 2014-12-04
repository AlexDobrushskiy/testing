
"""
Add {% csrf_token %} to all html forms without such token in a given folder.
Works recursively.
==========================================
Usage:
> python append_csrf.py <path_to_proccess>
"""

import os
import re
import sys


# recursively walk the directory and do some actions with each file


def walk(path):
    """
    Walk over the directory. Return list of full file paths.
    :param path:
    :return:
    """
    if not os.path.isdir(path):
        return []

    dir_content = os.listdir(path)
    result = []

    for item in dir_content:
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            result += walk(full_path)
        else:
            result += [full_path]

    return result


def csrf_repl(match_obj):
    if '{% csrf_token %}' in match_obj.group(2):
        return match_obj.group(0)
    else:
        return match_obj.group(1) + '{% csrf_token %}' + match_obj.group(2) + match_obj.group(3)


def append_csrf_to_forms(template_text):
    return re.sub(r'(<form.*?>)(.*?)(</form>)', csrf_repl, template_text, flags=re.DOTALL)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write('This util needs some input: ./append_csrf.py string_to_reverse\n')
        sys.exit()
    path = sys.argv[1]
    file_list = walk(path)

    for item in file_list:
        with open(item, 'r') as f:
            content = f.read()

        content = append_csrf_to_forms(content)
        with open(item, 'w') as f:
            f.write(content)
    sys.stdout.write('Complete!\n')