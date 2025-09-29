# Starter code for Python Text Processing Assignment

# Task 1: Text File Analyzer
# You may use this skeleton to get started

def analyze_file(filename):
    try:
        with open(filename, 'r') as f:
            text = f.read()
        lines = text.splitlines()
        words = text.split()
        chars = len(text)
        print(f"Lines: {len(lines)}")
        print(f"Words: {len(words)}")
        print(f"Characters: {chars}")
    except FileNotFoundError:
        print("File not found.")

# Task 2: Text Search and Replace
# You may use this skeleton to get started

def search_and_replace(filename, search_term, replacement, output_filename):
    try:
        with open(filename, 'r') as f:
            text = f.read()
        count = text.count(search_term)
        new_text = text.replace(search_term, replacement)
        with open(output_filename, 'w') as f:
            f.write(new_text)
        print(f"Replaced {count} occurrence(s) of '{search_term}' with '{replacement}'.")
    except FileNotFoundError:
        print("File not found.")

# Example usage (uncomment to use):
# analyze_file('sample.txt')
# search_and_replace('sample.txt', 'old', 'new', 'output.txt')
