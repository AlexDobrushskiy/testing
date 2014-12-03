import sys


def string_reverse(input_string):
    result = ''
    for i in input_string:
        result = i + result
    return result

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.stderr.write('This util needs some input: ./string_reverse.py string_to_reverse\n')
        sys.exit()
    input_string = sys.argv[1]
    if len(sys.argv) > 2:
        sys.stderr.write('Warning: the second and the following arguments ignored\n')
    sys.stdout.write('Initial string: {}\n'.format(input_string))
    sys.stdout.write('Reversed string: {}\n'.format(string_reverse(input_string)))