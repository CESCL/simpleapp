# DOT503 - DevOps Tools
# Assessment 2 - Continuous integration and testing pipeline

# This is a simple code in python of a program that count lines in a file called text.txt.

# Function to count lines
def count_lines(file):
    file.seek(0)  # Ensure you're at the start of the file. Addedd also in feature-y development. 
    return sum(1 for line in file)

# Function to count bytes
def count_bytes(file):
    file.seek(0)  # Ensure you're at the start of the file. Addedd also in feature-y development. 
    return len(file.read())

# Function to count words
def count_words(file):
    file.seek(0)  # Reset file pointer to the start added in feature-x
    return sum(len(line.split()) for line in file)

# Main execution
filename = 'text.txt'
with open(filename, 'r') as file:
    line_count = count_lines(file)
    word_count = count_words(file)
    byte_count = count_bytes(file)
    
# Modified print statement for feature-z # Modified to merge with master in the conflict resolution. 
print(f"[Feature Z] The file '{filename}' has {line_count} lines, {word_count} words and {byte_count} bytes.")
# This is the final version of the code merged into master