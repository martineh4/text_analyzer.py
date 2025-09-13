# Text analyzer

from collections import Counter

def read_file(file_name):
    """Opens a file and returns the words in lowercase"""
    with open(file_name, "r") as file:
        return file.read().lower().split()
    
def count_words(words):
    """Counts word frequencies with Counter"""
    return Counter(words)
 
def find_long_words(words, min_length = 3):
    """Returns number of words longer than the minimum length (3 characters)"""
    return [word for word in words if len(word) > min_length]

def display(words, word_frequencies, long_words):  
    """Prints information about the file"""
    print(f"The total number of words is: {len(words)}")
    print(f"The unique words count is: {len(word_frequencies)}")
    print("The most frequent words are:")
    for word, count in word_frequencies.most_common(5):
        print(f"'{word}': {count}")
    print(f"Long words (more than 3 characters): {len(long_words)}")

# You will need to create a text file named 'sample.txt' to be analyzed.
def analyze_text(file_name):
    """Carries out all steps of the text analysis"""
    words = read_file(file_name)
    word_frequencies = count_words(words)
    long_words = find_long_words(words)
    display(words, word_frequencies, long_words)

if __name__ == "__main__":
    analyze_text("sample.txt")
