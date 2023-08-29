import random

class Worldscape:
    def __init__(self, name_list):
        """
        Constructor to initialize class attributes.
        """
        self.name_list = name_list
        self.lives = 8

    def generate_secret_name(self):
        """
        Function randomly select element from list
        """
        return random.choice(self.name_list).lower()    #https://www.w3schools.com/python/ref_random_choice.asp

    def encode_name(self, secret_name):
        """
        Function to encode the name by replacing its characters with "-".
        If country name contains spaces will display spaces as spaces and other letters as dashes.
        """
        encoded_name = ""
        for x in secret_name:
            if (x == " "):
                encoded_name += " "
            else:
                encoded_name += "-"
        return encoded_name

    def is_letter_valid(self, input_letter):
        """
        Function validates whether the given input letter is a single
        alphabetical character.
        """
        try:
            if len(input_letter) != 1 or not input_letter.isalpha():
                raise ValueError(f"Please enter a letter, not a number, special character nor string")
            
        except ValueError as e:
            print(f"Invalid input: {e}, please try again.\n")
            return False

        return True
        