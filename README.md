![tło readme](https://github.com/Grzegorz96/Saper-game/assets/129303867/1dc4d7b8-853f-46b3-99e3-57183c492a15)
# SAPER

The look of my game is based on the cult game Minesweeper written in 1981 by Robert Donner. In my version, I updated the game with new sounds and graphics. I also added four 
difficulty levels. The game dynamically generates the size of the game board and the corresponding game table, depending on the selected difficulty level. The project has the function of dynamic expansion of fields through recursion. My project is written and optimized for the Linux operating system.


## Description of the modules
The program was created from four modules. The Config.py module contains all the global variables needed for the correct operation of the entire program. It consists of objects that need global access, flags, a dictionary with the names of graphic files and global integers. Function.py is the whole brain of the program, it contains the most important functions. It determines what is hidden under the clicked button, generates the entire game_table, which is later responsible for where the bombs and fields with numbers are located. Game_table is a generated 2-D list with only zeros at first, then the required number of mines is randomly generated on this table. For list items that are not generated mines, adjacent item coordinates are searched. Then it is checked how many of the found elements are bombs. In the last step, the number of adjacent bombs is is overwritten for zero, and so on for each element that is not a bomb. The function in the module recurses to display empty fields and fields adjacent to bombs. Modul is responsible for sounds and graphic files. This module determines when a win or loss occurs and what happens in those cases. In this file, global variables change their values and objects that are no longer needed are destroyed for better program operation and better memory management. GUI.py is responsible for creating the main application window and initializing the application screens: start_label and game_label. In start_label we choose the difficulty level, after selecting the difficulty level, the game_label is initialized with the parameters and global variables selected for it. In the game_label there is a function responsible for initializing the game_board and calling the game_table function. In the game_label the clock and mines counter update function is called for the first time. Main.py is the module that executes the program. It calls the main application window creation functions, initializes the sound mixer object, loads the names of the needed images into a global variable, and initializes the start_label for the root object. Finally, the main loop method of the program is executed on the root object, thanks to this method, the program does not terminate and runs in a loop.


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
 pip install pygame==2.5.0
```
- Run Main.py on Linux:
```bash
 python3 Main.py
```


## Lessons Learned
While writing the program, I learned a lot about working with for loops and working with 2-D lists. I had to imagine how the program was supposed to work under the hood and implement all the solutions with which there were a lot of problems. This project required a bit more math than just program writing skills. I had to optimize the project in terms of destroying unnecessary objects because the program generates a whole lot of them and not destroying objects was associated with slow work of the program. In the case of the professional game level there are 1250 fields generated once, resetting the game creates new objects. Repeatedly generating new fields and not destroying the old ones was associated with a large performance loss. In this project, I had to use my imagination to combine the operation of the buttons with the generated board of bombs and numbers. I had to pay attention to changing the states of global flags at the right time, so that the program knew what it could do and what it couldn't do. The program developed my programming skills and taught me to solve problems in a slightly different way.


## Features to be implemented
- Scoring system implementation.
- Adding a backend so that users can create accounts and compete with each other in the number of points scored and time of completion of individual difficulty levels.
- In lost_game and update_button functions, some of the button objects from the global current_list_of_buttons are overwritten with labels and not all buttons are destroyed when the game is reset, the full destruction of the buttons takes place only when the entire game_label is destroyed when changing the window. The way to fix this would be to operate on two global lists, buttons and labels. Then, when the game is reset, it would be possible to destroy all created objects that are no longer needed.
- Loading of sound files into the global "sounds" dictionary when running Main.py. During operation, the program will use sounds stored in memory instead of reading them directly from the computer.


## Authors

- [@Grzegorz96](https://www.github.com/Grzegorz96)


## Contact

E-mail: grzesstrzeszewski@gmail.com


## License

[MIT](https://github.com/Grzegorz96/Saper-game/blob/master/LICENSE.md)


## Screnshoots
##### Screenshot of the difficulty level selection window
![start_window](https://github.com/Grzegorz96/Saper-game/assets/129303867/b44363b8-3329-4bfa-898c-20db28ebe366)
##### Screenshot a beginner level game
![beginner](https://github.com/Grzegorz96/Saper-game/assets/129303867/375bded5-ff57-4640-8665-825f796abf2e)
##### Screenshot in game of beginner level game
![scared_face](https://github.com/Grzegorz96/Saper-game/assets/129303867/4b05b591-d62b-4e63-9064-688fd67aef10)
##### Screenshot of a beginner level lose
![lose](https://github.com/Grzegorz96/Saper-game/assets/129303867/32717b00-e98c-4917-94a8-52dafb717ce1)
##### Screenshot of a beginner level win
![won](https://github.com/Grzegorz96/Saper-game/assets/129303867/0e68562a-5095-4236-9fa5-f40de1504669)
##### Screenshot of an intermediate level game
![Intermediate](https://github.com/Grzegorz96/Saper-game/assets/129303867/cd9726ac-33da-46a3-9af3-1997a396d6bf)
##### Screenshot in game of intermediate level game
![inter_game](https://github.com/Grzegorz96/Saper-game/assets/129303867/4237c45b-4e87-4a58-8833-c98d9bb55622)
##### Screenshot of an intermediate level lose
![inter_lose](https://github.com/Grzegorz96/Saper-game/assets/129303867/e93218bf-b1e3-4029-b8d4-399f52ac1918)
##### Screenshot of an intermediate level win
![inter_won](https://github.com/Grzegorz96/Saper-game/assets/129303867/4c72b6e1-cadd-4871-baae-92dfa134fcfc)
##### Screenshot of a advanced level game
![advanced](https://github.com/Grzegorz96/Saper-game/assets/129303867/e6b0d50e-d792-488c-ab8d-db2378c7c9e5)
##### Screenshot of a professional level game
![pro](https://github.com/Grzegorz96/Saper-game/assets/129303867/6813ab92-9ecd-4eae-9069-1b8eee189d56)
