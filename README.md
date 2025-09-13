## Project Overview
The **Text Analyzer** is a Python script designed to analyze a text file to determine important statistics about its content.
The output results in the following information on a text file:
- Total number of words
- Number of unique words
- Top 5 most frequent words
- Number of words longer than 3 characters

## How to Run
1. Ensure Python is installed on your device
2. Place your text file ('sample.txt' by default) in the same folder as 'text_analyzer.py'
3. Run the script from your terminal or command line

## Key Improvements
PEP 8 Compliance:
- Function and variable names use snake_case
- Docstrings were added to exlain functions
- Indentation and spacing were cleaned up

Context Managers:
- Replaced open() and close() with a with block
- Ensures that file closes automatically, even if an error occurs

collections.Counter class:
- Python's built-in counter counts word frequencies
- Faster than a manual dictionary loop

List Comprehensions:
- Replaced loops used to find long words with a list comprehension
- Shorter and improves readability

Modular Functions:
- Code is broken down into more focused functions
- Improves readability, reuasability, and sustainability
