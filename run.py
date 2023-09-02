# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from worldscape import Worldscape
from names import country_list, city_list

if __name__ == "__main__":

    def play_game(name_list, name):
        run_game = True
        game_played = 0
        game_won = 0
        game_lost = 0

        while run_game:
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
                                game_played += 1
                                game_won += 1
                                break
                        else:
                            game.lives -= 1
            print(game.secret_name) #australia
            print(game.encoded_named) #AUSTRALIA
            if game.secret_name != game.encoded_named.lower():
                print("Sorry, you lost the game.")
                print(f"The {name} was: {game.secret_name.upper()}")
                game_played += 1
                game_lost += 1

            play_again = input("Play another game (y to continue, anything else will stop the game)? ")
            if play_again.lower() != 'y':
                game.display_statistics(game_played, game_won, game_lost)
                run_game = False

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
            pass
        else:
            print("Thanks")
            break