import random

class Worldscape:
    def __init__(self, name_list):
        """
        Constructor to initialize class attributes.
        """
        self.name_list = name_list
        self.letters_used = []
        self.name_guessed = ""
        self.lives = 8
        self.game_played = 0
        self.game_won = 0
        self.game_lost = 0

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

    def replace_encoded_name_with_guessed_letter(self, letter, secret_name, encoded_name):
        """
        Function to replace dashes in the encoded name with the correct guessed letter.
        """
        for i in range(len(secret_name)):
            if secret_name[i] == letter:
                self.name_guessed += letter.capitalize()
            else:
                self.name_guessed += encoded_name[i]
        return self.name_guessed

    def display_output(self, name):
        """
        Function displays game information to the user, including
        the number of remaining lives, the guessed letters and dashes in the
        secret name, and the list of letters that have been used before.
        """
        print("************************************")
        print(f"Lives: {self.lives}\n")
        print(f"{name}: {self.name_guessed}\n")
        print(f"Letters used: {', '.join(self.letters_used)}\n")
        print("************************************")

    def display_statistics(self):
        """
        Function displays statistics related to the user's gameplay,
        including the number of games played, games won, and games lost.
        """
        print("************************************")
        print("\nGame Statistics:")
        print("************************************")
        print(f"Game played: {self.game_played}")
        print(f"Game won: {self.game_won}")
        print(f"Game lost: {self.game_lost}")
        print("************************************")


    

        