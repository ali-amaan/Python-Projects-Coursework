import sys


def print_character_and_line_counts1(path):
    input_file = None
    try:
        input_file = open(path)
    except OSError:
        print("Could not open {}".format(path), file=sys.stderr)
    else:
        lineCount = 0
        characterCount = 0
        for line in input_file:
            lineCount += 1
            characterCount += len(line)
        print("File {} has {} characters in {} lines".format(path, characterCount, lineCount))
    finally:
        if input_file:
            input_file.close()


def print_character_and_line_counts2(path):
    with open(path) as input_file:
        lineCount = 0
        characterCount = 0
        for line in input_file:
            lineCount += 1
            characterCount += len(line)
        print("File {} has {} characters in {} lines".format(path, characterCount, lineCount))

        
def print_character_and_line_counts3(path):
    try:
        with open(path) as input_file:
            lineCount = 0
            characterCount = 0
            for line in input_file:
                lineCount += 1
                characterCount += len(line)
            print("File {} has {} characters in {} lines".format(path, characterCount, lineCount))
    except OSError:
        print("Could not open {}".format(path), file=sys.stderr)


def print_sorted_file(path):
    try:
        with open(path) as input_file:
            lines = input_file.readlines()
            lines.sort()
            for line in lines:
                print(line.rstrip())
    except OSError:
        print("Could not open {}".format(path), file=sys.stderr)


with open('out.txt', mode='w') as f:
    f.write('Print number {}\n'.format(10))
    print('Print number {}'.format(10), file=f)
            
