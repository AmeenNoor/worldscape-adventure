# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from worldscape import Worldscape
from names import country_list, city_list, landmark_list


game_played = 0
game_won = 0
game_lost = 0

def display_statistics():
    """
    Function displays statistics related to the user's gameplay,
    including the number of games played, games won, and games lost.
    """
    print("************************************")
    print("\nGame Statistics:")
    print("************************************")
    print(f"Game played: {game_played}")
    print(f"Game won: {game_won}")
    print(f"Game lost: {game_lost}")
    print("************************************")

def update_game_statistics(is_won):
    """
    Function to increment the total games played and either the total games won 
    or the total games lost based on the outcome of the game.
    """
    global game_played, game_won, game_lost
    game_played += 1
    if is_won:
        game_won += 1
    else:
        game_lost += 1

def display_how_to_play():
    print("************************************")
    print("HOW TO PLAY")
    print("************************************")
    print("Welcome to the Worldscape game!")
    print("In this game, you will be given the opportunity to guess a name, which could be a country, city, or landmark.")
    print("Here's how to play:")
    print("1. Select 'PLAY GAME' from the main menu.")
    print("2. Choose whether you want to guess a country, city, or landmark.")
    print("3. You will be presented with a name, where the letters are initially hidden with dashes.")
    print("4. You have 8 lives to guess the name correctly.")
    print("5. Guess one letter at a time by entering a single alphabetical character.")
    print("6. If the letter you guessed is in the name, it will be revealed.")
    print("7. If the letter is not in the name, you will lose one life.")
    print("8. Keep guessing letters until you either correctly guess the entire name or run out of lives.")
    print("9. If you correctly guess the name, you win the game. Otherwise, you lose.")
    print("10. You can play again as many times as you like or view your game statistics.")
    print("************************************")


def play_game(name_list, name):
    game = Worldscape(name_list)
    game.generate_secret_name().lower()
    game.encode_name()
    while game.lives > 0:
        game.display_output(name)
        input_letter = input("Guess a letter: \n").lower()
        if game.is_letter_valid(input_letter):
            if game.is_letter_used_before(input_letter):
                print(f"You have already used: {input_letter}")
            else:
                game.add_used_letter(input_letter)
                if game.is_letter_in_name(input_letter):
                    game.replace_encoded_name_with_guessed_letter(input_letter)
                    print(game.secret_name) #australia
                    print(game.encoded_named) #AUSTRALIA
                    if game.secret_name == game.encoded_named.lower():
                        print("Congratulations, you won the game!")
                        update_game_statistics(True)
                        break
                else:
                    game.lives -= 1
    print(game.secret_name) #australia
    print(game.encoded_named) #AUSTRALIA
    if game.secret_name != game.encoded_named.lower():
        print("Sorry, you lost the game.")
        print(f"The {name} was: {game.secret_name.upper()}")
        update_game_statistics(False)

def main():
    while True:      
        print("A. HOW TO PLAY")
        print("B. PLAY GAME")
        print("C. GAME STATISTICS")
        print("E. EXIT")
        option = input("Please choose one the above options\n").lower()     
        if option != 'a' and option != 'b' and option != 'c' and option != 'e':
            print("Enter 'a', 'b', 'c' or 'e' to choose from the menu!\n")
        elif option == 'a':
            display_how_to_play()
        elif option == 'b':
            while True:
                print("A. COUNTRY")
                print("B. CITY")
                print("C. LANDMARKS")
                option_game = input("Select a game to play: (A. Country, B. City, C. Landmarks)\n").lower()
                if option_game != 'a' and option_game != 'b' and option_game != 'c':
                    print("Enter 'a', 'b' or 'c' to choose from the menu to play!")
                    continue
                elif option_game == 'a':
                    play_game(country_list, "Country")
                elif option_game == 'b':
                    play_game(city_list, "City")
                else:
                    play_game(city_list, "Landmarks")
                play_again = input("Play another game (y to continue, anything else will stop the game)? ")
                if play_again.lower() != 'y':
                    break
        elif option == 'c':
            display_statistics()
        else:
            print("Thank you for using the App! Have a great day!")
            break

if __name__ == "__main__":
    main()