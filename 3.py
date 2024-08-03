# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

# Read the input string
s = input()

# Use groupby to group consecutive characters
result = [(len(list(group)), int(key)) for key, group in groupby(s)]

# Print the tuples in the specified format
print(' '.join(f"({count}, {char})" for count, char in result))
