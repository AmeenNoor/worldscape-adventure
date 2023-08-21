# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
country_list = ["Ameen", "Noor", "Python", "repuBlic of Ireland"]

def secret_country(list):
    """
    Function randomly select element from list
    """
    return random.choice(list) # https://www.w3schools.com/python/ref_random_choice.asp

def encode_country(country):
    """
    Function to encode the country by replacing its characters with "*".
    If country name contains spaces will display spaces as spaces and other letters as asterisks.
    """
    encode = ""
    for x in country:
        if (x == " "):
            encode += " "
        else:
            encode += "*"
    return encode


print(encode_country(secret_country(country_list)))