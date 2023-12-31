import random
# Worldscape class


class Worldscape:
    """
    Worldscape class represents a word-guessing game environment.
    Players can guess letters to unveil a secret word, track their
    progress, and manage their remaining lives.
    """
    def __init__(self, name_list):
        """
        Constructor to initialize class attributes.
        """
        self.name_list = name_list
        self.secret_name = ""
        self.encoded_name = ""
        self.letters_used = []
        self.lives = 8

    def generate_secret_name(self):
        """
        Function randomly select element from list
        """
        # https://www.w3schools.com/python/ref_random_choice.asp
        self.secret_name = random.choice(self.name_list).lower()
        return self.secret_name

    def encode_name(self):
        """
        Function to encode the name by replacing its characters with "-".
        If country name contains spaces will display spaces as spaces and
        other letters as dashes.
        """
        for x in self.secret_name:
            if (x == " "):
                self.encoded_name += " "
            else:
                self.encoded_name += "-"
        return self.encoded_name

    def is_letter_valid(self, input_letter):
        """
        Function validates whether the given input letter is a single
        alphabetical character.
        """
        if len(input_letter) != 1 or not input_letter.isalpha():
            return False
        else:
            return True

    def is_letter_in_name(self, letter):
        """
        Function determines whether a given letter is present in the
        secret name.
        """
        if letter in self.secret_name:
            return True
        else:
            return False

    def add_used_letter(self, letter):
        """
        Function takes a letter entered by the user and adds it to the
        `letters_used` list.
        """
        self.letters_used.append(letter)
        return self.letters_used

    def is_letter_used_before(self, letter):
        """
        Function checks whether if a letter has been previously entered
        by the user.
        """
        if letter in self.letters_used:
            return True
        else:
            return False

    def replace_encoded_name_with_guessed_letter(self, letter):
        """
        Function to replace dashes in the encoded name with the
        correct guessed letter.
        """
        new_encoded_name = ""
        for i in range(len(self.secret_name)):
            if self.secret_name[i] == letter:
                new_encoded_name += letter.capitalize()
            else:
                new_encoded_name += self.encoded_name[i]
        self.encoded_name = new_encoded_name
        return self.encoded_name

    def display_output(self, name):
        """
        Function displays game information to the user, including
        the number of remaining lives, the guessed letters and dashes in the
        secret name, and the list of letters that have been used before.
        """
        print("************************************")
        print(f"Lives: {self.lives}\n")
        print(f"{name}: {self.encoded_name}\n")
        print(f"Letters used: {', '.join(self.letters_used)}\n")
        print("************************************")
