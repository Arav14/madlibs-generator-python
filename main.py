with open("Story.txt", "r") as f:  # Open the file in read mode
    story = f.read()  # Read the file

words = set()  # Store the content of the file in a set to avoid duplicates
start_of_word = -1   # Initialize start_of_word to -1

target_start = "<"  # Target character to find the start of a word
target_end = ">"  # Target character to find the end of a word

for i, char in enumerate(story):   # Loop through each character in the story
    if char == target_start:  # Check if the character is the start of a word
        start_of_word = i  # Update start_of_word to the current index

    # Check if the character if the end of the word and start_of_word is not -1
    if char == target_end and start_of_word != -1:

        # Sub slicing the story to get the word. End index is exclusive
        word = story[start_of_word: i + 1]
        words.add(word)  # Append the word to the list
        start_of_word = -1  # Reset start_of_word to -1 for the next word

answers = {}  # Dictionary to store user inputs for each word

for word in words:  # Loop through each word in the set
    answer = input("Enter a word for " + word + ": ")  # Prompt user for input
    answers[word] = answer  # Store the user's input in the dictionary

for word in words:  # Loop through each word in the set again

    # Replace the word in the story with user's input and store it in the story variable
    story = story.replace(word, answers[word])

print(story)
