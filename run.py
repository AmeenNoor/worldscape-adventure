# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from worldscape import Worldscape

if __name__ == "__main__":
    name_list = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", 
    "Austria", "Azerbaijan"]

    run_game = True
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
                        if '-' not in game.encoded_named:
                            print("Congratulations, you won the game!")
                            game.game_played += 1
                            game.game_won += 1
                    else:
                        game.lives -= 1

        if game.secret_name != game.encoded_named:
            print("Sorry, you lost the game.")
            print(f"The word was: {game.secret_name.capitalize()}")
            game.game_lost += 1

        play_again = input("Play another game (y to continue, anything else will stop the game)? ")
        if play_again.lower() != 'y':
            game.display_statistics()
            run_game = False
        
            