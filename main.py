# DOT503 - DevOps Tools
# Assessment 2 - Continuous integration and testing pipeline

# This is a simple code in python of a program that count lines in a file called text.txt.

# Simple function to count lines
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
    byte_count = count_bytes(file)
    word_count = count_words(file)
    
print(f"The number of lines in the file is: {line_count}")
print(f"The number of bytes in the file is: {byte_count}")
print(f"The number of words in the file is: {word_count}")
