# DOT503 - DevOps Tools
# Assessment 2 - Continuous integration and testing pipeline

# This is a simple code in python of a program that count lines in a file called text.txt.

# Function to count lines
def count_lines(file):
    file.seek(0)  # Reset file pointer to the start
    return sum(1 for line in file)

# Function to count words
def count_words(file):
    file.seek(0)  # Reset file pointer to the start
    return sum(len(line.split()) for line in file)

# Main execution for feature-z
filename = 'text.txt'
with open(filename, 'r') as file:
    line_count = count_lines(file)
    word_count = count_words(file)

# Modified print statement for feature-z
print(f"[Feature Z] The file '{filename}' has {line_count} lines and {word_count} words.")