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
    game_played += 1
    if is_won:
        game_won += 1
    else:
        game_lost += 1

def play_game(name_list, name):
    global game_played, game_won, game_lost
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

    play_again = input("Play another game (y to continue, anything else will stop the game)? ")
    if play_again.lower() != 'y':
        display_statistics()

def main():
    while True:      
        print("1. HOW TO PLAY")
        print("2. PLAY GAME")
        print("3. GAME STATISTICS")
        print("4. EXIT")
        option = int(input("Please choose one the above options\n"))      
        if option != 1 and option != 2 and option != 3 and option != 4:
            print("Enter '1' or '2' to choose from the menu!\n")
        elif option == 1:
            pass
        elif option == 2:
            while True:
                print("1. COUNTRY")
                print("2. CITY")
                print("3. LANDMARKS")
                option_game = int(input("Select game: "))
                if option != 1 and option != 2:
                    print("Enter '1' or '2' to choose from the menu to play!")
                elif option_game == 1:
                    play_game(country_list, "Country")
                elif option_game == 2:
                    play_game(city_list, "City")
                else:
                    play_game(city_list, "Landmarks")
        elif option == 3:
            display_statistics()
        else:
            print("Thanks")
            break

if __name__ == "__main__":
    main()