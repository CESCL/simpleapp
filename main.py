# DOT503 - DevOps Tools
# Assessment 2 - Continuous integration and testing pipeline

# This is a simple code in python of a program that count lines in a file called text.txt.

# Simple function to count lines
def count_lines(file):
    return sum(1 for line in file)

# Main execution
filename = 'text.txt'
with open(filename, 'r') as file:
    line_count = count_lines(file)

print(f"The number of lines in the file is: {line_count}")