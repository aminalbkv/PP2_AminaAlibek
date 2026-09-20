# Here is a function that checks if text is a palindrome
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]