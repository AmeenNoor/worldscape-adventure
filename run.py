from worldscape import Worldscape
from names import country_list, city_list, landmark_list
from os import system, name
from simple_colors import red, green
# https://pypi.org/project/simple-colors/
import pyfiglet

# Variables are used to keep track of game statistics:
game_played = 0
game_won = 0
game_lost = 0


def clear_terminal():
    """
    Function to clear the terminal screen based on the operating system.
    The logic for function was adopted from 'How to clear screen in
    python?' tutorial at https://www.geeksforgeeks.org/clear-screen-python/
    """
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')


def display_statistics():
    """
    Function displays statistics related to the user's gameplay,
    including the number of games played, games won, and games lost.
    """
    print("************************************")
    print("\nGame Statistics:")
    print("************************************")
    print(f"Game played: {green(game_played)}")
    print(f"Game won: {green(game_won)}")
    print(f"Game lost: {red(game_lost)}")
    print("************************************")


def update_game_statistics(is_won):
    """
    Function to increment the total games played and either the total
    games won or the total games lost based on the outcome of the game.
    """
    global game_played, game_won, game_lost
    game_played += 1
    if is_won:
        game_won += 1
    else:
        game_lost += 1


def display_how_to_play():
    """
    Function provides a set of step-by-step instructions on how to play
    the game,
    """
    print("******************************************************************")
    print("-------------------------- HOW TO PLAY ---------------------------")
    print("******************************************************************")
    print("1. Select 'PLAY GAME' from the main menu.")
    print("2. Choose whether you want to guess a country, city, or landmark.")
    print("3. You will be presented with a name, where the letters are")
    print("initially hidden with dashes.")
    print("4. You have 8 lives to guess the name correctly.")
    print("5. Guess one letter at a time by entering a single alphabetical")
    print("character.")
    print("6. If the letter you guessed is in the name, it will be revealed.")
    print("7. If the letter is not in the name, you will lose one life.")
    print("8. Keep guessing letters until you either correctly guess the")
    print("entire name or run out of lives.")
    print("9. If you correctly guess the name, you win the game.")
    print("Otherwise, you lose.")
    print("10. You can play again as many times as you like or view your")
    print("game statistics.")
    print("******************************************************************")


def play_game(name_list, name):
    """
    Function to initiate and manage a game session, allowing the player to
    guess letters and attempt to uncover the secret name.
    """
    # Create an object of Worldscape class.
    game = Worldscape(name_list)
    # Calling 'generate_secret_name()' function to generate a secret name.
    game.generate_secret_name().lower()
    # Calling 'encode_name()' function to encode the secret name with dashes.
    game.encode_name()
    clear_terminal()
    while game.lives > 0:
        print("\n" * 2)
        # Calling 'display_output()' function to display the game information.
        game.display_output(name)
        print("\n" * 2)
        # Prompt the player for a letter guess.
        input_letter = input("Guess a letter: \n\n").lower()
        clear_terminal()
        # Calling 'is_letter_valid()' function to check if letter is valid
        if game.is_letter_valid(input_letter):
            # Calling 'is_letter_used_before()' function to check if user
            # entered same letter before.
            if game.is_letter_used_before(input_letter):
                print("\n")
                print(f"{red('You have already used:')} "
                      f"{green(input_letter.capitalize())}\n")
            else:
                # Calling 'add_used_letter()' function to record the guessed
                # letter.
                game.add_used_letter(input_letter)
                # Calling 'is_letter_in_name()' function to check if letter
                # in secret name.
                if game.is_letter_in_name(input_letter):
                    # Calling the function to update the encoded name
                    game.replace_encoded_name_with_guessed_letter(input_letter)
                    if game.secret_name == game.encoded_name.lower():
                        print("\n" * 2)
                        print(green("Congratulations, you won the game!"))
                        # Calling 'update_game_statistics' function to update
                        # game statistics for a win.
                        update_game_statistics(True)
                        # Exit the game loop if the name is fully guessed.
                        break
                else:
                    # Decrement lives if the guessed letter is not in the
                    # secret name.
                    game.lives -= 1
        else:
            print("\n")
            print(red("Invalid input: Please enter a letter, not a number, ")
                  + red("special character nor string!\n"))
    if game.secret_name != game.encoded_name.lower():
        clear_terminal()
        print("\n" * 2)
        print(red("Sorry, you lost the game."))
        print("\n")
        print(f"The {name} was: {green(game.secret_name.upper())}\n")
        # Calling 'update_game_statistics' function to update game
        # statistics for a loss.
        update_game_statistics(False)


def main():
    """
    Function serves as the primary entry point for the game,allowing users
    to navigate through the game menu, select game options, and play the game.
    """
    print("\n")
    print(green(pyfiglet.figlet_format("Welcome To", font="banner3-D", width=110)))
    print(green(pyfiglet.figlet_format("Worldscape", font="banner3-D", width=110)))
    print("\n")
    print(green("Get ready to explore the world and test your knowledge!\n"))
    while True:
        # Display the main menu options.
        print("\n")
        print("A. HOW TO PLAY")
        print("B. PLAY GAME")
        print("C. GAME STATISTICS")
        print("E. EXIT")
        print("\n")
        option = input(
            green("Please choose one of the above options:\n\n")).lower()
        if option == 'a':
            clear_terminal()
            print("\n")
            # Calling 'display_how_to_play()' function to display instructions
            # on how to play the game.
            display_how_to_play()
        elif option == 'b':
            clear_terminal()
            while True:
                # Display game category options.
                print("\n" * 2)
                print("A. COUNTRY")
                print("B. CITY")
                print("C. LANDMARKS")
                print("E. BACK TO MAIN MENU")
                print("\n" * 2)

                option_game = input(
                  green("Select a game to play: (A. Country, B. City, ")
                  + green("C. Landmarks)\n\n")
                ).lower()
                if (
                    option_game != 'a' and
                    option_game != 'b' and
                    option_game != 'c' and
                    option_game != 'e'
                ):
                    clear_terminal()
                    print("\n")
                    print(red("Enter 'a', 'b', 'c' or 'e' to choose from ")
                          + red("the menu to play!"))
                    continue
                elif option_game == 'a':
                    clear_terminal()
                    # Calling 'play_game()' function to start a game in the
                    # "Country" category.
                    play_game(country_list, "Country")
                elif option_game == 'b':
                    clear_terminal()
                    # Calling 'play_game()' function to start a game in the
                    # "City" category.
                    play_game(city_list, "City")
                elif option_game == 'c':
                    clear_terminal()
                    # Calling 'play_game()' function to start a game in the
                    # "Landmarks" category.
                    play_game(city_list, "Landmarks")
                else:
                    clear_terminal()
                    break
                print("\n")
                play_again = input(
                    green("Play another game (y to continue, anything else ")
                    + green("will stop the game)?\n\n")
                    )
                clear_terminal()
                if play_again.lower() != 'y':
                    break
        elif option == 'c':
            clear_terminal()
            print("\n")
            # Calling 'display_statistics()' function to display game
            # statistics.
            display_statistics()
            print("\n")
        elif option == 'e':
            clear_terminal()
            print("\n")
            print("Thank you for using the App! Have a great day!")
            print("\n")
            # Exit the game loop if the user selects 'E' to exit the
            # application.
            break
        else:
            clear_terminal()
            print("\n")
            print(red("Invalid input! Enter 'a', 'b', 'c', or 'e' ")
                  + red("to choose from the menu.\n"))


if __name__ == "__main__":
    main()
