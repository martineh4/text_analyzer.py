# Text analyzer

from collections import Counter

def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read().lower().split()
    
def count_words(words):
    return Counter(words)
 
def find_long_words(words, min_length = 4):
    # Now let's find the words with more than 3 characters
    return [word_element for word_element in words if len(word_element) > min_length]

def display(words, word_frequencies, long_words):      
    print(f"The total number of words is: {len(words)}")
    print(f"The unique words count is: {len(word_frequencies)}")
    print("The most frequent words are:")
    for word, count in word_frequencies.most_common(5):
        print(f"'{word}': {count}")
    print(f"Long words (more than 3 characters): {len(long_words)}")

# You will need to create a text file named 'sample.txt' for testing.
def analyze_text(file_name):
    words = read_file(file_name)
    word_frequencies = count_words(words)
    long_words = find_long_words(words)
    display(words, word_frequencies, long_words)

if __name__ == "__main__":
    analyze_text("sample.txt")