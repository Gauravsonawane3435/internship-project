//word count python program

def word_counter(text):
    if not text.strip():
        print("Error: Please enter a non-empty sentence or paragraph.")
        return 0

    words = text.split()
    return len(words)

# User Input
user_input = input("Enter a sentence or paragraph: ")

# Word Counting Logic
word_count = word_counter(user_input)

# Output Display
print(f"Number of words: {word_count}")
