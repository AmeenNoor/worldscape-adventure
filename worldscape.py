import random

class Worldscape:
    def __init__(self, name_list):
        """
        Constructor to initialize class attributes.
        """
        self.name_list = name_list
        self.letters_used = []
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

    def is_letter_in_name(self, secret_name, letter):
        """
        Function determines whether a given letter is present in the secret name.
        """
        if letter in secret_name:
            return True
        else:
            return False

    def letters_used(self, letter):
        """
        Function takes a letter entered by the user and adds it to the `letters_used` list.
        """
        self.letters_used.append(letter)
        return self.letters_used

    def is_letter_used_before(self, letter):
        """
        Function checks whether if a letter has been previously entered by the user.
        """
        if letter in self.letters_used:
            return True
        else:
            return False

    

        