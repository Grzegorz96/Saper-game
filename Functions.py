# Modules import.
from tkinter import *
# Import global variables.
import Config
import random
from pygame import mixer


# Initialization game_table.
def init_game_table():
    # Creating 2d table for range columns and rows. First a list with a range of columns, then as many lists as there
    # are rows.
    # game_table is like [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]].
    game_table = [[0 for _ in range(Config.columns)] for _ in range(Config.rows)]
    # From the global variable mines_number we assign the value to the local mines_to_be_drawn, which is nedded to draw
    # mines.
    mines_to_be_drawn = Config.mines_number

    # While mines_to_be_drawn will not 0, the program randomizes two x and y coordinates. x=element/y=list
    while mines_to_be_drawn:
        x = random.randint(0, Config.columns-1)
        y = random.randint(0, Config.rows-1)

        # Y = index list in list / X = index element in the drawn list. If this element is 0 then change value to "x"
        # and mines_to_be_drawn -=1.
        if game_table[y][x] == 0:
            game_table[y][x] = "x"
            mines_to_be_drawn -= 1

    # We look for neighboring bombs and write down their number instead of 0 if there are any.
    for i in range(Config.rows):
        for j in range(Config.columns):

            if game_table[i][j] == 0:
                # Calling the find_neighbors function for the argument of the current element, the coordinates of the
                # neighboring elements are assigned to the variable.
                neighbours = find_neighbours(i, j)
                # Temporary counter of adjacent mines.
                number_neighbours_mines = 0

                # We iterate over the coordinate tuples in the neighbors list and check if the element with the given
                # coordinates is a mine, if so we increase the min counter by one.
                for y, x in neighbours:
                    if game_table[y][x] == "x":
                        number_neighbours_mines += 1

                # Finally, we assign for a given element which was "0", the number of adjacent mines found.
                game_table[i][j] = number_neighbours_mines

    # Returning generated game_table (for example: [[0,0,1,x,1],[0,x,x,3,0],[1,1,2,0,0],[0,1,x,0,x]]
    return game_table


# The function of finding adjacent coordinates of an element.
def find_neighbours(y, x):
    # Temporary list.
    neighbours = []

    # Iterating over all adjacent indexes.
    for i in range(-1, 2):
        for j in range(-1, 2):
            # i == 0/ j == 0 is currently imported coordinates.
            if not (i == 0 and j == 0):
                # Checking if the neighbor's coordinates fit in the board horizontally
                if 0 <= y + i < Config.rows:
                    # Checking if the neighbor's coordinates fit in the board vertically
                    if 0 <= x + j < Config.columns:
                        # If the coordinates pass the validations, they will be added to the list.
                        # An offset relative to the neighbor will be added to the current coordinates.
                        neighbours.append((y+i, x+j))

    # Returns a list of neighboring coordinates.
    return neighbours


# Function for clock updating.
def update_clock():
    # Checking if the clock should work.
    if Config.is_clock_work:
        # Adding += 1 second.
        Config.time += 1
        # Configure object.
        Config.clock_object["text"] = "0" * (4 - len(str(Config.time))) + str(Config.time)
        # Calling the function again in 1 second.
        Config.clock_object.after(1000, update_clock)


# A function that updates the minutes counter on the game label.
def update_mines_counter():
    Config.mines_counter_object["text"] = "0" * (4 - len(str(Config.flags_number_left))) + str(Config.flags_number_left)


# A function that changes the image of  face to a smiling one.
def normal_face():
    Config.face_object["image"] = Config.images["faces"][0]


# A function that changes the image of  face to a scared one.
def scared_face():
    Config.face_object["image"] = Config.images["faces"][1]


# The function that is responsible for pasting objects on the label.
def make_grid(x, y):
    # If the object's column is 0 then we add an extra margin to the left.
    if x == 0:
        Config.current_list_of_buttons[y*Config.columns+x].grid(row=y+1, column=x, padx=(20, 0))
    # We also need to add one extra row in both cases because the top panel is already on the first row.
    else:
        Config.current_list_of_buttons[y*Config.columns+x].grid(row=y+1, column=x)


# Game end feature.
def lost_game(game_table, game_label, button):
    # Changing flag of clock on False.
    Config.is_clock_work = False
    # Unbinding and disabling buttons that have not been pressed before.
    for i in range(Config.rows):
        for j in range(Config.columns):
            if (isinstance(Config.current_list_of_buttons[i * Config.columns + j], Button)
                    and Config.current_list_of_buttons[i * Config.columns + j]["state"] != "disabled"):
                Config.current_list_of_buttons[i * Config.columns + j]["state"] = "disabled"
                Config.current_list_of_buttons[i * Config.columns + j].unbind("<Button-1>")
                Config.current_list_of_buttons[i * Config.columns + j].unbind("<Button-3>")
                Config.current_list_of_buttons[i * Config.columns + j].unbind("<ButtonRelease-1>")

                # Checking if there is a bomb under this button.
                if game_table[i][j] == 'x':
                    # If it is the currently pressed button then the label with the bomb will be red.
                    if Config.current_list_of_buttons[i * Config.columns + j] is button:
                        Config.current_list_of_buttons[i * Config.columns + j] = Label(game_label,
                                                                                       image=Config.images["mines"][1])
                    # If not, the label with bomb will be plain black.
                    else:
                        Config.current_list_of_buttons[i * Config.columns + j] = Label(game_label,
                                                                                       image=Config.images["mines"][0])
                    # Placement of newly created objects on the board.
                    make_grid(j, i)

                # If we know that the button does not have a mine under it, we check whether it had a flag attached to
                # it, if so, then we change the picture to a crossed out one.
                elif Config.current_list_of_buttons[i * Config.columns + j].cget("image"):
                    Config.current_list_of_buttons[i * Config.columns + j]["image"] = Config.images["flags"][1]


# Game win feature
def won_game():
    # Changing flag of clock on False.
    Config.is_clock_work = False
    # Disable and unbind buttons that have not been pressed before.
    for i in range(Config.rows):
        for j in range(Config.columns):
            if (isinstance(Config.current_list_of_buttons[i * Config.columns + j], Button)
                    and Config.current_list_of_buttons[i * Config.columns + j]["state"] != "disabled"):
                Config.current_list_of_buttons[i * Config.columns + j]["state"] = "disabled"
                Config.current_list_of_buttons[i * Config.columns + j].unbind("<Button-1>")
                Config.current_list_of_buttons[i * Config.columns + j].unbind("<Button-3>")
                Config.current_list_of_buttons[i * Config.columns + j].unbind("<ButtonRelease-1>")


# Button update function.
def update_button(index, field, game_table, game_label):
    # Changing the state of the button to disabled and unbinding it.
    Config.current_list_of_buttons[index].configure(state="disabled", border=1, highlightbackground="black")
    Config.current_list_of_buttons[index].unbind("<Button-1>")
    Config.current_list_of_buttons[index].unbind("<Button-3>")
    Config.current_list_of_buttons[index].unbind("<ButtonRelease-1>")

    # If there is a field 1-8 under the clicked button then it enters this instruction.
    if field != 0:
        # A flag to protect against recursive playback of a sound that is to be played only once per click.
        if Config.permission_to_play_one_sound:
            # Playing a sound, for each number a different sound.
            run_sound_effect(f"{field}.wav")
            # Setting flag on False.
            Config.permission_to_play_one_sound = False

        # Replacing the pressed button with a label with an image corresponding to the number of adjacent mines.
        Config.current_list_of_buttons[index] = Label(game_label, image=Config.images["digits"][field - 1])
        # Placing label.
        make_grid(index % Config.columns, index//Config.columns)

    # If there is a field with 0 under the button, then there will be a recurrence until the fields adjacent to the
    # mines are found.
    else:
        # A flag to protect against recursive playback of a sound that is to be played only once per click.
        if Config.permission_to_play_one_sound:
            # Playing a sound of recursion.
            run_sound_effect("recursion.wav")
            # Setting flag on False.
            Config.permission_to_play_one_sound = False

        # Finding the coordinates of adjacent fields relative to the field with 0.
        neighbours = find_neighbours(index // Config.columns, index % Config.columns)
        # If the button with the given coordinates is: a button, is not disabled, and does not have a flag on it,
        # then we can call the function update button for this button. We know that buttons directly adjacent to 0
        # cannot be bombs, if there is a number under the button, I will not enter the recursion instruction.
        # The recursion will continue to expand until buttons with numbers that are directly adjacent to the bombs are
        # uncovered. y is row(list)/ x is column(element in list)
        for y, x in neighbours:
            if (isinstance(Config.current_list_of_buttons[y * Config.columns + x], Button)
                    and Config.current_list_of_buttons[y * Config.columns + x]["state"] != "disabled"
                    and not Config.current_list_of_buttons[y * Config.columns + x].cget("image")):
                # We import to the function: calculated button index, calculated field element,
                # game_table and game_label.
                update_button(y * Config.columns + x, game_table[y][x], game_table, game_label)


# Left button function.
def left_click(button, game_table, game_label):
    # The function will do nothing if we click on the protected field with the flag.
    if not button.cget("image"):
        # Creating index of button and the corresponding field from game_table.
        index = Config.current_list_of_buttons.index(button)
        field = game_table[index//Config.columns][index % Config.columns]

        # If there's a bomb under the button.
        if field == "x":
            # A bomb sound will be made, the face will change to a sad one and the game end function will be called.
            run_sound_effect("bomb.wav")
            Config.face_object["image"] = Config.images["faces"][2]
            lost_game(game_table, game_label, button)

        # If there is no bomb under the button.
        else:
            # The user will receive permission to open some sound once and the update function of the button will be
            # performed.
            Config.permission_to_play_one_sound = True
            update_button(index, field, game_table, game_label)


# Right click function.
def right_click(button, game_table):
    # Creating index of button and the corresponding field from game_table.
    index = Config.current_list_of_buttons.index(button)
    field = game_table[index // Config.columns][index % Config.columns]

    # Checking if the clicked button already has a flag.
    if button.cget("image"):
        # Plays the flag removal sound and removes the flag image.
        run_sound_effect("delete_flag.wav")
        button["image"] = ""
        # Changing the number of available flags.
        Config.flags_number_left += 1
        # Checking if there is a bomb under this button.
        if field == "x":
            # Changing the number of guessed mines if there was a mine under this button.
            Config.number_guessed_mines -= 1

    # If the button did not have a flag.
    else:
        # Checking if the user has flags to add.
        if Config.flags_number_left > 0:
            # Playing the sound of adding a flag,adding a picture of a flag, and changing the number of available flags.
            run_sound_effect("put_flag.wav")
            button["image"] = Config.images["flags"][0]
            Config.flags_number_left -= 1
            # If there is a bomb under the button then it updates the number of guessed mines.
            if field == "x":
                Config.number_guessed_mines += 1
                # I check if the number of guessed mines is equal to the number of all mines generated on the board.
                if Config.number_guessed_mines == Config.mines_number:
                    # Playing the win sound, changing the face image and calling the won game function.
                    run_sound_effect("winner.wav")
                    Config.face_object["image"] = Config.images["faces"][3]
                    won_game()
        # In case the user wants to add a flag but has no more flags available then a sound will be triggered
        # informing him about it.
        else:
            run_sound_effect("empty_flag.wav")

    # Finally, the mines counter will be updated so that the user always has the current number of available mines
    # displayed.
    update_mines_counter()


# A function that loads images into a global dictionary and a global variable.
def loading_images():
    Config.images["digits"] = [PhotoImage(file="Photos/" + str(i) + ".png") for i in range(1, 9)]
    Config.images["faces"] = [PhotoImage(file="Photos/face" + str(i) + ".png") for i in range(1, 5)]
    Config.images["flags"] = [PhotoImage(file="Photos/flag.png"), PhotoImage(file="Photos/crossed_out_flag.png")]
    Config.images["mines"] = [PhotoImage(file="Photos/mine.png"), PhotoImage(file="Photos/first_mine.png")]
    Config.photo = PhotoImage(file="Photos/background.png")


# Game reset function
def reset_game(init_game_board, game_label):
    # Playing a button sound.
    run_sound_effect("button.wav")
    # Disabling the clock function by changing the global flag.
    Config.is_clock_work = False
    # Destruction of the created list of buttons.
    for button in Config.current_list_of_buttons:
        button.destroy()
    # Creating a new list of buttons, adding them to the label and creating a new game_table.
    init_game_board()
    # Changing the face image.
    Config.face_object["image"] = Config.images["faces"][0]
    # Resetting the number of guessed mines.
    Config.number_guessed_mines = 0
    # Updated the number of flags available to the number of bombs for a given difficulty level.
    Config.flags_number_left = Config.mines_number
    # mines counter update.
    update_mines_counter()
    # Assigning the time variable to 0
    Config.time = 0
    # Destroying the clock object and creating a new one prevents the duplicate clock bug.
    Config.clock_object.destroy()
    Config.clock_object = Label(game_label, bg="black", fg="red", font="Digital-7, 40")
    Config.clock_object.grid(row=0, column=Config.columns - 6, columnspan=6, ipadx=10, pady=30)
    # Changing the clock flag and calling the function that will run it.
    Config.is_clock_work = True
    update_clock()


# Indirect function that configures global variables before creating the game.
def configure_variables_for_game_label(rows, columns, mines_number, window_width, window_height, root, init_game_label):
    # Run sound.
    run_sound_effect("button.wav")
    # Global variables are assigned values selected by the user.
    Config.rows = rows
    Config.columns = columns
    Config.mines_number = mines_number
    Config.flags_number_left = Config.mines_number
    # Changing the clock run flag.
    Config.is_clock_work = True
    # Creating the geometry of the game window.
    create_app_geometry(root, window_width, window_height)
    # Initialization game_label.
    init_game_label(root, window_width, window_height)


# Indirect function to configure global variables before going to start_label.
def configure_variables_for_start_label(root, init_start_label):
    # Run sound.
    run_sound_effect("button.wav")
    # Set default global variables
    Config.is_clock_work = False
    Config.face_object = None
    Config.mines_counter_object = None
    Config.clock_object = None
    Config.current_list_of_buttons = None
    Config.rows = 0
    Config.columns = 0
    Config.time = 0
    Config.flags_number_left = 0
    Config.mines_number = 0
    Config.number_guessed_mines = 0
    # Creating geometry of start_window.
    create_app_geometry(root, 880, 600)
    # Initialization start_label.
    init_start_label(root)


# A function that creates the window geometry.
def create_app_geometry(root, window_width, window_height):
    # Definition width and height of monitor window.
    screen_width = 1920
    screen_height = 1080
    # Setting center of window.
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    # Making geometry with the imported window width and height, and with the creation coordinates.
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


# Initialization sound mixer for app.
def init_sound_mixer():
    mixer.init()
    # Setting volume on 0.2.
    mixer.music.set_volume(0.2)


# Sound effect function.
def run_sound_effect(sound):
    # Making object of sound effect, setting volume on 0.2 and play.
    sound_effect = mixer.Sound(fr"Sounds/{sound}")
    sound_effect.set_volume(0.2)
    sound_effect.play()
