# Here is a function that reverses the words
def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()

    return " ".join(words)


# Here is user input
sentence = input("Enter a sentence: ")

# Here is the result
print(reverse_sentence(sentence))