

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
        