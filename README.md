![logo](https://raw.githubusercontent.com/Grzegorz96/Saper-game/master/docs/readme-images/logo.png)
# SAPER

The Saper application is a desktop game whose appearance is based on the iconic Minesweeper game written in 1981 by Robert Donner. In my version, I updated the game with new sounds and graphics. Additionally, I introduced four difficulty levels. The game dynamically generates the size of the game board and the corresponding game table, depending on the selected difficulty level. The project includes the feature of dynamically uncovering fields through recursion. My game is written and optimized for the Linux operating system.


## Description of the modules

The program consists of 4 modules, each of which plays a unique role in the functioning of the application. Below is a brief description of each module:

Config.py:
- The Config.py module contains all global variables essential for the correct operation of the entire program. It includes objects requiring global access.

Functions.py:
- The Functions.py module acts as the brain of the program, housing crucial functions. It determines what is hidden under the clicked button, generates the entire game_table, which is later responsible for where the bombs and fields with numbers are located. Game_table is a generated 2-D list with only zeros at first, then the required number of mines is randomly generated on this table. For list items that are not generated mines, adjacent item coordinates are searched. Then it is checked how many of the found elements are bombs. In the last step, the number of adjacent bombs is is overwritten for zero, and so on for each element that is not a bomb. The function in the module recursively discovers empty fields and fields adjacent to bombs. Modul is responsible for sounds and graphic files. This module determines when a win or loss occurs and what happens in those cases. In this file, global variables change their values and objects that are no longer needed are destroyed for better program operation and better memory management.

GUI.py:
- The GUI.py module is responsible for creating the main application window and initializing the application screens: start_label and game_label. In start_label we choose the difficulty level, after selecting the difficulty level, the game_label is initialized with the parameters and global variables selected for it. In the game_label there is a function responsible for initializing the game_board and calling the game_table function. In the game_label the clock and mines counter update function is called for the first time.

Main.py:
- The Main.py module executes the program. It calls the main application window creation functions, initializes the sound mixer object, loads the names of the needed images into a global variable, and calls the funkcje init_start_label for the root object. Finally, the main loop method of the program is executed on the root object, thanks to this method, the program does not terminate and runs in a loop.


## Features

- Choice of four difficulty levels:
###### - Beginner (rows=9, columns=15, mines_number=10)
###### - Intermediate (rows=15, columns=25, mines_number=40)
###### - Advanced (rows=20, columns=35, mines_number=100)
###### - Professional (rows=25, columns=45, mines_number=200)
- Dynamic generation of the game board depending on the user's choice.
- Sound system for every user action.
- Recursion function revealing empty squares on the board.
- Counter of placed flags.
- Game clock.
- Game reset function.
- Changing face icon on reset button during user action (four states).
- Win and lose functions.
- Showing bomb placements and misplaced flags after losing the game.
- Audio information about no available flags to place.
- Each square with the number 1-8 has its own sound.
- Additional sounds for bomb explosion, win, flag raising, flag removal, button clicks and recursion of board fields



## Technology used

**Client:** 
- Languages: Python
- Third Party Libraries: Tkinter, Pygame


## Installation

### To quickly launch the application on Linux:

- Download Saper-game repository:
```bash
 git clone https://github.com/Grzegorz96/Saper-game.git
```
- Enter the directory Saper-game/Saper_elf.
- If you want to move the Saper.elf file, do it together with the Sounds and Photos folders. You can also create a copy of the .elf file on your desktop.
- Run Saper.elf.

### For manually launching the application on the IDE:
#### Requirements:
##### Programs and libraries:
- Python 3.10.6
- IDE, for example Pycharm
- pygame 2.5.0
#### Instruction:
- Download Saper-game repository:
```bash
 git clone https://github.com/Grzegorz96/Saper-game.git
```
- Go to the Saper-game directory.
- Open the Saper-game on your IDE.
- Create virtual enviroment for the project (Linux):
```bash
 python3 -m venv venv
```
- Activate virtual enviroment (Linux):
```bash
 source venv/bin/activate
```
- Install required packages on your activated virtual enviroment:
```bash
  pip install -r requirements.txt
```
- or
```bash
 pip install pygame==2.5.0
```
- Run Main.py on Linux:
```bash
 python3 Main.py
```


## Lessons learned

While writing the program, I learned a lot about working with for loops and working with 2-D lists. I had to imagine how the program was supposed to work under the hood and implement all the solutions with which there were a lot of problems. This project required a bit more math than just program writing skills. I had to optimize the project in terms of destroying unnecessary objects because the program generates a whole lot of them and not destroying objects was associated with slow work of the program. In the case of the professional game level there are 1250 fields generated once, resetting the game creates new objects. Repeatedly generating new fields and not destroying the old ones was associated with a large performance loss. In this project, I had to use my imagination to combine the operation of the buttons with the generated board of bombs and numbers. I had to pay attention to changing the states of global flags at the right time, so that the program knew what it could do and what it couldn't do. The program developed my programming skills and taught me to solve problems in a slightly different way.


## Features to be implemented

- Scoring system implementation.
- Adding a backend so that users can create accounts and compete with each other in the number of points scored and time of completion of individual difficulty levels.
- In lost_game and update_button functions, some of the button objects from the global current_list_of_buttons are overwritten with labels and not all buttons are destroyed when the game is reset, the full destruction of the buttons takes place only when the entire game_label is destroyed when changing the window. The way to fix this would be to operate on two global lists, buttons and labels. Then, when the game is reset, it would be possible to destroy all created objects that are no longer needed.
- Loading of sound files into the global "sounds" dictionary when running Main.py. During operation, the program will use sounds stored in memory instead of reading them directly from the computer.


## Authors

[@Grzegorz96](https://www.github.com/Grzegorz96)


## Contact

E-mail: grzesstrzeszewski@gmail.com


## License

[MIT](https://github.com/Grzegorz96/Saper-game/blob/master/LICENSE.md)


## Screnshoots
##### Screenshot of the difficulty level selection window
![start_window](https://raw.githubusercontent.com/Grzegorz96/Saper-game/master/docs/readme-images/start_window.png)
##### Screenshot a beginner level game
![beginner](https://raw.githubusercontent.com/Grzegorz96/Saper-game/master/docs/readme-images/beginner.png)
##### Screenshot in game of beginner level game
![scared_face](https://raw.githubusercontent.com/Grzegorz96/Saper-game/master/docs/readme-images/scared_face.png)
##### Screenshot of a beginner level lose
![lose](https://raw.githubusercontent.com/Grzegorz96/Saper-game/master/docs/readme-images/lose.png)
##### Screenshot of a beginner level win
![won](https://raw.githubusercontent.com/Grzegorz96/Saper-game/master/docs/readme-images/won.png)
##### Screenshot of an intermediate level game
![Intermediate](https://raw.githubusercontent.com/Grzegorz96/Saper-game/master/docs/readme-images/intermediate.png)
##### Screenshot in game of intermediate level game
![intermediate_game](https://raw.githubusercontent.com/Grzegorz96/Saper-game/master/docs/readme-images/intermediate_game.png)
##### Screenshot of an intermediate level lose
![intermediate_lose](https://raw.githubusercontent.com/Grzegorz96/Saper-game/master/docs/readme-images/intermediate_lose.png)
##### Screenshot of an intermediate level win
![intermediate_won](https://raw.githubusercontent.com/Grzegorz96/Saper-game/master/docs/readme-images/intermediate_won.png)
##### Screenshot of a advanced level game
![advanced](https://raw.githubusercontent.com/Grzegorz96/Saper-game/master/docs/readme-images/advanced.png)
##### Screenshot of a professional level game
![professional](https://raw.githubusercontent.com/Grzegorz96/Saper-game/master/docs/readme-images/professional.png)
