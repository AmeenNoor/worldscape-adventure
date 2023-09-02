# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from worldscape import Worldscape

if __name__ == "__main__":
    name_list = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", 
    "Austria", "Azerbaijan"]

    run_game = True
    game_played = 0
    game_won = 0
    game_lost = 0

    while run_game:
        game = Worldscape(name_list)
        game.generate_secret_name().lower()
        game.encode_name()

        
        while game.lives > 0:
            game.display_output("Country")
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
            print(f"The word was: {game.secret_name.upper()}")
            game_played += 1
            game_lost += 1

        play_again = input("Play another game (y to continue, anything else will stop the game)? ")
        if play_again.lower() != 'y':
            game.display_statistics(game_played, game_won, game_lost)
            run_game = False
        
            