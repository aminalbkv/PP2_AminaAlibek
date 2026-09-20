# Here is a class for working with a string
class StringManager:

    # Here is a method to get a string from the user
    def getString(self):
        self.text = input("Enter a string: ")

    # Here is a method to print the string in uppercase
    def printString(self):
        print(self.text.upper())


# Here is an object of the StringManager class
my_string = StringManager()

# Here is a call to get the string
my_string.getString()

# Here is a call to print the string
my_string.printString()