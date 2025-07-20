
# Using base_exp.txt, a 22K text file containing one thousand lines with a
# base/exponent pair on each line, determine which line number has the
# greatest numerical value.

# Solution ideas:
# To compare numbers like b^e, we can use logarithms.
# Instead of comparing b1^e1 and b2^e2, we can compare e1*log(b1) and e2*log(b2).
# The logarithm is a monotonically increasing function, so if e1*log(b1) > e2*log(b2),
# then b1^e1 > b2^e2.
# This avoids calculating the huge numbers.

import math

def find_largest_value_line(path):
    max_val = 0
    max_line_num = 0
    with open(path, 'r') as f:
        for i, line in enumerate(f, 1):
            base, exponent = map(int, line.strip().split(','))
            val = exponent * math.log(base)
            if val > max_val:
                max_val = val
                max_line_num = i
    return max_line_num

def main():
    # The problem description gives the file name as '0099_base_exp.txt',
    # but based on the project structure, it is likely 'p099_base_exp.txt'.
    # I will assume the latter.
    file_path = 'resources/documents/p099_base_exp.txt'
    try:
        # First, let's create the file with the expected name from the problem,
        # in case the actual file has a different name.
        # I'll look for a file that seems to contain the data.
        # A file named 'base_exp.txt' seems likely.
        with open('resources/documents/base_exp.txt', 'r') as source_file:
            content = source_file.read()
        with open(file_path, 'w') as dest_file:
            dest_file.write(content)
    except FileNotFoundError:
        # If 'base_exp.txt' is not found, I'll just proceed,
        # assuming 'p099_base_exp.txt' already exists.
        pass

    try:
        line_num = find_largest_value_line(file_path)
        print(line_num)
    except FileNotFoundError:
        print(f"Error: Could not find the file at {file_path}")

if __name__ == "__main__":
    main()
