# Worldscape Adventure

## Author

Ameen Noor

## Introduction

"Worldscape Adventure" is an interactive word-guessing game that offers players an engaging and educational experience. In this game, players will have the opportunity to explore and guess names of countries, cities, and landmarks from around the world. The objective is to unveil the hidden name by guessing one letter at a time while managing a limited number of lives. The game is designed to test players' knowledge of geography and improve their letter-guessing skills.

![Am I Responsive](https://github.com/AmeenNoor/activeBeat-center/blob/main/assets/responsive/am-i-responsive.png)

Click [here](https://worldscape-adventure-6f50d85fec22.herokuapp.com/) to visit the website.

## Table of Contents

- [ActiveBeat Center](#activebeat-center)
  - [Author](#author)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [User Experience (UX)](#user-experience-ux)
    - [User storis](#user-storis)
    - [Design](#design)
  - [How To Play](#how-to-play)
  - [Features](#features)
    - [Implemented Features](#implemented-features)
    - [Future Features](#future-features)
  - [Data Model/ Classes](#data-model-classes)
    - [Worldscape](#worldscape)
    - [Main Program](#main-program)
    - [Data Flow](#data-flow)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
  - [Testing](#testing)
    - [Testing User Stories](#testing-user-stories)
    - [Validation Testing](#validation-testing)
    - [Compatibility and Responsive Testing](#compatibility-and-responsive-testing)
    - [Manual Testing](#manual-testing)
    - [Accessibility](#accessibility)
    - [Fixing Bugs](#fixing-bugs)
    - [Open Bugs](#open-bugs)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Gitpod](#gitpod)
  - [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
    - [Media](#media)
    - [Mentor](#mentor)


## User Experience (UX)
### User storis

1. As a player, I want to find a clear and understandable main menu with options like "How to Play," "Play Game," "Game Statistics," and "Exit" for easy navigation.

2. As a player, I want to access straightforward instructions when choosing "How to Play" from the main menu, ensuring I can quickly grasp the game's mechanics.

3. As a player, I want a user-friendly "Play Game" menu where I can select whether to guess a country, city, or landmark name, and the ability to return to the main menu.

4. As a player, I want smooth and engaging gameplay, with clear feedback on guessed letters and an enjoyable way to reveal the hidden name.

5. As a player, I want a simple "Game Statistics" section that displays the number of games played, games won, and games lost, allowing me to easily track my progress.


### Design
#### Flow Chart


![Flow Chart](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/flowchart/flow-chart.png)


## How To Play

1. **Main Menu**:
    - When you start the game, you'll see the main menu with four options: "HOW TO PLAY," "PLAY GAME," "GAME STATISTICS," and "EXIT."
    - Use the keyboard to select the option you want by entering the corresponding letter (e.g., 'A' for "HOW TO PLAY").

2. **How to Play**:
    - If you're new to the game or need a refresher, choose "HOW TO PLAY" from the main menu ('A').
    - Read the provided instructions to understand the game rules and how to navigate the game.

3. **Play Game**:
    - To start playing, select "PLAY GAME" from the main menu ('B').
    - You will then have the option to choose a game category: "COUNTRY," "CITY," or "LANDMARKS." Enter the corresponding letter to make your choice ('A' for "COUNTRY," 'B' for "CITY," or 'C' for "LANDMARKS").

4. **Gameplay**:
    - You'll be presented with a hidden name from your chosen category, with the letters initially replaced by dashes.
    - You have 8 lives to guess the name correctly.
    - Guess one letter at a time by entering a single alphabetical character.
    - If the letter you guess is in the name, it will be revealed. If not, you'll lose a life.
    - Continue guessing letters until you either guess the entire name correctly or run out of lives.

5. **Winning the Game**:
    - If you correctly guess the name, congratulations, you win the game!
    - The game will display a winning message.

6. **Losing the Game**:
    - If you run out of lives without guessing the name correctly, you lose the game.
    - The game will display a losing message and reveal the correct answer.

7. **Play Again**:
    - After a game, you have the option to play another round within the same category.
    - If you choose to play again, you can keep guessing new names to improve your skills.

8. **Game Statistics**:
    - You can view your game statistics at any time by selecting "GAME STATISTICS" from the main menu ('C').
    - This option shows you the number of games played, games won, and games lost.

9. **Exiting the Game**:
    - To exit the game, select "EXIT" from the main menu ('E').


## Features
### Implemented Features

1. Main Menu Navigation: The main menu provides clear options for the user, including "How to Play," "Play Game," "Game Statistics," and "Exit," ensuring easy navigation and interaction.

![Navigation Bar](https://github.com/AmeenNoor/activeBeat-center/blob/main/assets/features/nav-menu.png)

2. Game Instructions ("How to Play"): Users can access comprehensive game instructions, allowing them to quickly understand the game's rules.

![Contact Form](https://github.com/AmeenNoor/activeBeat-center/blob/main/assets/features/contact-form.png)

3. Game Category Selection: Players can choose from three categories - countries, cities, or landmarks - to guess the name they want to unveil, adding variety and excitement to the gameplay.

![Google Map](https://github.com/AmeenNoor/activeBeat-center/blob/main/assets/features/google-map.png)

4. Interactive Gameplay: During the game, users interact by guessing letters one at a time, with immediate feedback. Correct guesses reveal hidden letters, while incorrect ones deduct lives.

![Contact Information](https://github.com/AmeenNoor/activeBeat-center/blob/main/assets/features/contact-information.png)

5. Life System: The game features a life system, with players having eight lives to guess the name correctly. 

![Social Media Links](https://github.com/AmeenNoor/activeBeat-center/blob/main/assets/features/social-media-icons.png)

6. Progress Tracking ("Game Statistics"): The "Game Statistics" option allows users to track their progress effortlessly, displaying the number of games played, games won, and games lost.


![Thank You page](https://github.com/AmeenNoor/activeBeat-center/blob/main/assets/features/thankyou-message.png)

7. Exit Option: Users can exit the game smoothly by selecting "Exit" from the main menu. The program closes gracefully, providing a hassle-free experience.


![404 page](https://github.com/AmeenNoor/activeBeat-center/blob/main/assets/features/e404-page.png)

8. Feedback and Notifications: The game offers clear feedback and notifications when users guess letters or complete the game, enhancing engagement and providing a satisfying gaming experience.

9. Colorful Text (Simple Colors Library): The game implements colored text to enhance visual appeal and make the user interface more engaging.

### Future Features

1. **High Score Tracking**: Implement a feature to ask the user for their name and record all game statistics in an Excel file, allowing players to view high scores and compete for the top spot.

2. **Difficulty Levels**: Add the option for players to choose between different difficulty levels, such as easy and difficult.

3. **Dynamic Word Generation**: Instead of using a constant list of words, connect to an API for word generation, to ensure every game is an exciting adventure.

## Data Model/ Classes
### Worldscape

The Worldscape class represents a word-guessing game environment, allowing players to guess letters to unveil a secret word, track their progress, and manage their remaining lives.

**Attributes:**

1. **name_list**: A list of names (countries, cities, landmarks) from which the secret name will be randomly selected.

2. **secret_name**: The current secret name that the player needs to guess.

3. **encoded_name**: The secret name encoded with dashes, where each letter is initially hidden.

4. **letters_used**: A list of letters that the player has already guessed.

5. **lives**: The number of remaining lives the player has.

**Functions:**

1. **__init__(self, name_list)**: Constructor method to initialize class attributes.
    - **name_list**: The list of names provided as an argument.
    - **Initializes** secret_name and encoded_named as empty strings.
    - **Initializes** letters_used as an empty list.
    - **Initializes** lives to 8.

2. **generate_secret_name(self)**: Randomly selects a secret name from the provided **name_list**.
    - Returns the generated **secret name**.

4. **encode_name(self)**: Encodes the secret name by replacing its characters with dashes.
    - If the country name contains spaces, spaces are displayed as spaces, and other letters are displayed as dashes.
    - Returns the **encoded name**.

5. **is_letter_valid(self, input_letter)**: Validates whether the given input letter is a single alphabetical character.
    - Returns **True** if the input is valid, **False** otherwise.

6. **is_letter_in_name(self, letter)**: Determines whether a given letter is present in the secret name.
    - Returns **True** if the letter is in the name, **False** otherwise.

7. **add_used_letter(self, letter)**: Takes a letter entered by the user and adds it to the letters_used list.
    - Returns the updated list of **used letters**.

8. **is_letter_used_before(self, letter)**: Checks whether a letter has been previously entered by the user.
    - Returns **True** if the letter has been used before, **False** otherwise.

9. **replace_encoded_name_with_guessed_letter(self, letter)**: Replaces dashes in the encoded name with the correct guessed letter.
    - Returns the updated **encoded name**.

10. **display_output(self, name)**: Displays game information to the user, including the number of remaining lives, the guessed letters and dashes in the secret name, and the list of letters that have been used before.

### Main Program

The main program consists of various functions and the main function to facilitate gameplay and user interaction.

**Functions**:

1. **clear_terminal()**: Clears the terminal screen based on the operating system (Windows or Mac/Linux).

2. **display_statistics()**: Displays statistics related to the user's gameplay, including the number of games played, games won, and games lost.

3. **update_game_statistics(is_won)**: Increments the total games played and either the total games won or the total games lost based on the outcome of the game.

4. **display_how_to_play()**: Provides step-by-step instructions on how to play the game.

5. **play_game(name_list, name)**: Initiates and manages a game session, allowing the player to guess letters and attempt to uncover the secret name.

6. **main()**: Serves as the primary entry point for the game, allowing users to navigate through the game menu, select game options, and play the game.

### Data Flow

- The **Worldscape** class handles game-specific data, such as the secret name, lives, and encoded name.

- The **main program** manages user interaction, displays menus, and calls the appropriate functions of the Worldscape class based on user input.

## Technologies Used
### Languages Used

1. Python
   
### Frameworks, Libraries and Programs Used

1. [Heroku](https://www.heroku.com/):
   Heroku was employed for project deployment.

2. [GitHub](https://github.com/):
   GitHub was utilized to store the project file and folder remotely.

3. [Git](https://git-scm.com/):
   Git was used in the Gitpod terminal to add, commit, and then push the changes to GitHub.

4. [CI's pep8 tool](https://pep8ci.herokuapp.com/):
   CI's pep8 tool was used to ensure the code is valid and follows proper indentation

5. [pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/):
   Pyfiglet was used to stylized ASCII art text for titles and banners.

6. [simple-colors](https://pypi.org/project/simple-colors/):
   Simple-colors was used to colored text.

7. [draw.io](https://app.diagrams.net/):
   draw.io was used to craft the flowchart

## Testing
### Validation Testing

Validation testing was performed using CI's PEP8 tool to ensure code quality. Here are the validation testing results for each file:

1. #### worldscape.py

![Worldscape](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/testing/worldscape-validation-testing.png)  

2. #### names.py
  
![Names List](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/testing/names-validation-testing.png)  

3. #### run.py

![Main Program](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/testing/run-validation-testing.png)  

### Compatibility and Responsive Testing
The website was tested on various browsers and devices to ensure compatibility and optimal user experience. The testing process yielded successful results for most browsers and devices, except for Safari browser. In Safari, it was observed that the navigation menu was not displayed as expected. See table and screenshots below:

<div align="center">

| Device                    | Browser         | OS       | Screen Width | Status |
| ------------------------- | --------------- | -------- | ------------ | ------ |
| dev tools: iPhone SE      | Chrome          | iOS      | 375 x 667    | ✔      |
| dev tools: iPhone 12      | Chrome          | iOS      | 390 x 844    | ✔      |
| dev tools: iPad Air       | Chrome          | iOS      | 820 x 1180   | ✔      |
| dev tools: Galaxy S8      | Chrome          | Android  | 362 x 740    | ✔      |
| real computer: Toshiba    | Microsoft Edge  | Windows 10 | 1366 x 768  | ✔      |
| real computer: Toshiba    | Firefox         | Ubuntu 22.04 | 1920 x 1080 | ✔      |
| real computer: MacBook Pro 13" | Safari    | iOS      | 1920 x 1080  | ✘      |
| real mobile phone: iPhone 7 Plus | Safari    | iOS      | 1920 x 1080  | ✘      |

</div>

- #### Safari browser
  The screenshots below showcase the website being tested on Safari browser across different devices, including a MacBook Pro M1 and an iPhone 7 Plus. During the testing phase, an issue was identified where a portion of the navigation menu appeared to float down on these devices.

  - ##### MacBook Pro 13"
    ![Safari-Macbook Pro Test](https://github.com/AmeenNoor/activeBeat-center/blob/main/assets/testing/safari-macbook-pro.png)
  - ##### iPhone 7 Plus
    <div align="center">
        <img src="https://github.com/AmeenNoor/activeBeat-center/blob/main/assets/testing/safari-iphone-7-plus.jpeg" alt="Safari-iPhone 7 Plus" width="400px" height="600px">
    </div>
### Manual Testing
View manual testing results [here!](https://docs.google.com/spreadsheets/d/1C0XAiSfxOVXIjn1UhXu-7vf35j0WS67IYKl_2fVBWd0/edit#gid=0)

![Manual Testing Image](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/testing/manual-testing.png)
### Accessibility
- #### Accessibility Audits
  Accessibility testing was done on the website, and Lighthouse, a testing tool, was used for this purpose. The Lighthouse report, displayed in the provided screenshot, indicates a successful outcome of the accessibility testing.

  ![Accessibility Test](https://github.com/AmeenNoor/activeBeat-center/blob/main/assets/testing/accessibility-test.png)

- #### Keyboard Navigation
  Keyboard Navigation testing was conduced on the website. keyboard was used for navigation and interaction, without relying on a mouse. The purpose of this testing was to ensure that all elements and features of the website could be accessed and operated through keyboard inputs. See image below:

 ![Keyboard Navigation](https://github.com/AmeenNoor/activeBeat-center/blob/main/assets/testing/keyboard-navigation.gif)

- #### Screen Reader Testing
  Screen Reader testing was done on the website, and ChromeVox extension in Google Chrome and VoiceOver on Mac were used for this purpose. Both screen readers were successfully able to read the content displayed on the screen.

### Fixing Bugs
- #### Validation Bug
  
  1. **worldscape.py**:
  Indentation issues in the 'worldscape.py' file have been fixed.

  ![Worldscape Fixed](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/testing/names-fixed.png)

  2. **names.py**:
  Indentation issues in the 'names.py' file have been fixed.

  ![Names Fixed](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/testing/names-fixed.png) 
  
  3. **run.py**:
  Indentation issues in the 'run.py' file have been fixed.

  ![Run Fixed](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/testing/names-fixed.png)

- #### Safari Bug
  The bug was; during the testing phase, an issue was identified where a portion of the navigation menu appeared to float down on these devices. As a temporary solution, the bug was fixed by removing the "Us" portion from the "Contact Us" section.
  
  1. MacBook Pro 13":

  ![Safari-Macbook Pro Bug Fixed](https://github.com/AmeenNoor/activeBeat-center/blob/main/assets/testing/bug-fixed-macbook.png)

  2. iPhone 7 Plus:

  <div align="center">
    <img src="https://github.com/AmeenNoor/activeBeat-center/blob/main/assets/testing/bug-fixed-iPhone.jpeg" alt="Safari-iPhone 7 Plus Bug Fixed" width="400px" height="600px">
  </div>
  
### Open Bugs
An open bug refers to a Safari bug that was identified during the testing phase. The bug causes a portion of the navigation menu to appear floating down on certain devices. As a temporary solution, the bug was addressed by removing the "Us" portion from the "Contact Us" section. However, it is important to note that this is only a temporary fix, and the bug should be resolved in a proper and more permanent manner in the future.

## Deployment
### Heroku
To deploy the site on Heroku, follow these steps:

1. Begin by forking the repository: https://github.com/AmeenNoor/worldscape-adventure.

2. Log in to Heroku and click "New." Select "Create new app."(see screenshots below):

![Deployment_1](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/deployment/deployment-image1.png)

3. Choose a unique name for your app, select your desired region, and then click "Create app." (see screenshot below):

![Deployment_2](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/deployment/deployment-image2.png)

4. In the app settings, navigate to the "Config Vars" section. Add a key-value pair where the key is "PORT" and the value is "8000." (see screenshots below):

![Deployment_3](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/deployment/deployment-image3.png)

![Deployment_4](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/deployment/deployment-image4.png)

![Deployment_5](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/deployment/deployment-image5.png)

5. Under the "Buildpacks" section, click "Add buildpacks." Add "python" and "nodejs" as buildpacks. Ensure that Python is selected first, followed by Node.js. Save your selections. (see screenshots below):

![Deployment_6](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/deployment/deployment-image6.png)

![Deployment_7](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/deployment/deployment-image7.png)

![Deployment_8](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/deployment/deployment-image8.png)

6. In the "Deploy" section, choose "GitHub/Connect to GitHub" as your deployment method. Search for the project on GitHub and connect it. (see screenshots below):

![Deployment_9](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/deployment/deployment-image9.png)

![Deployment_10](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/deployment/deployment-image10.png)

![Deployment_11](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/deployment/deployment-image11.png)

7. Finally, click "Deploy Branch" to deploy your project. (see screenshot below):

![Deployment_12](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/deployment/deployment-image12.png)

![Deployment_13](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/deployment/deployment-image13.png)

### Gitpod
To work with the project using Gitpod, follow these steps:

1. Fork the repository to create your own copy for personal use.

2. Install the Gitpod extension from the Visual Studio Code marketplace or your preferred extension source.

3. Inside the Gitpod workspace, install the project's requirements by running the command **pip3 install -r requirements.txt** in the terminal.

4. Start the program by running **python3 run.py** in the terminal.

## Credits
### Code

1. The GitHub repository was created using the "Code Institute template." You can find the template at: [Code Institute Template](https://github.com/Code-Institute-Org/p3-template).

2. The logic for **clear_terminal()** function was adopted from [How to clear screen in python?](https://www.geeksforgeeks.org/clear-screen-python/).

### Content

1. **List of Countries:** obtained from [Worldometers](https://www.worldometers.info/).

2. **List of Cities:** obtained from [World Maps](https://ontheworldmap.com/all/cities/).

3. **List of Landmarks:** obtained from [Destguides](https://www.destguides.com/famous-landmarks).
   
### Media

3. The responsive image is generated using the [Am I Responsive](https://ui.dev/amiresponsive) tool.


### Mentor
Huge thanks to my mentor "Malia Havlicek" for her support and guidance.
