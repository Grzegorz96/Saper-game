# Import modules.
from tkinter import *
# Import global variables.
import Config
# Import functions for GUI.
from Functions import init_game_table, make_grid, right_click, update_clock, update_mines_counter, normal_face,\
    left_click, reset_game, configure_variables_for_game_label, create_app_geometry, \
    configure_variables_for_start_label, scared_face
# Import mixer.
from pygame import mixer


def init_window():
    """Function responsible for initializing the main application window."""
    # Creating root object.
    root = Tk()
    # Creating title and resizable.
    root.title("SAPER")
    root.resizable(width=False, height=False)
    # Calling the window geometry creation function for window with 880 and window height 600.
    create_app_geometry(root, 880, 600)
    # Return root object into Main module.
    return root


def init_start_label(root):
    """The function responsible for initializing the start_label to select the game difficulty level."""
    # Run soundtrack in infinite loop.
    mixer.music.load(r"Sounds/saper_soundtrack.mp3")
    mixer.music.play(-1)
    # Function called first time will not enter this part of code, because current_page = None.
    if isinstance(Config.current_page, Label):
        Config.current_page.destroy()
    # Create start_label with photo and pack it into root.
    start_label = Label(root, width=880, height=600, image=Config.images["background"])
    start_label.pack()

    # Creating a difficulty level selection label.
    Label(start_label, text="Poziom trudności:", font=("Arial", 22), bg="#A9A9A9").place(x=315, y=200)
    # "Beginner" button with specific values in default parameters and assigning it an indirect function that configures
    # global variables for the game.
    Button(start_label, text="Początkujący", width=30, bg="#A9A9A9", highlightbackground="#1E90FF",
           command=lambda rows=9, columns=15, mines_number=10, window_width=460, window_height=430:
           configure_variables_for_game_label(rows, columns, mines_number, window_width,
                                              window_height, root, init_game_label)).place(x=300, y=250)
    # "Intermediate" button with specific values in default parameters and assigning it an indirect function that
    # configures global variables for the game.
    Button(start_label, text="Średniozaawansowany", width=30, bg="#A9A9A9", highlightbackground="#1E90FF",
           command=lambda rows=15, columns=25, mines_number=40, window_width=740, window_height=615:
           configure_variables_for_game_label(rows, columns, mines_number, window_width,
                                              window_height, root, init_game_label)).place(x=300, y=290)
    # "Advanced" button with specific values in default parameters and assigning it an indirect function that configures
    # global variables for the game.
    Button(start_label, text="Zaawansowany", width=30, bg="#A9A9A9", highlightbackground="#1E90FF",
           command=lambda rows=20, columns=35, mines_number=100, window_width=1020, window_height=770:
           configure_variables_for_game_label(rows, columns, mines_number, window_width,
                                              window_height, root, init_game_label)).place(x=300, y=330)
    # "Professional" button with specific values in default parameters and assigning it an indirect function that
    # configures global variables for the game.
    Button(start_label, text="Profesjonalista", width=30, bg="#A9A9A9", highlightbackground="#1E90FF",
           command=lambda rows=25, columns=45, mines_number=200, window_width=1300, window_height=925:
           configure_variables_for_game_label(rows, columns, mines_number, window_width,
                                              window_height, root, init_game_label)).place(x=300, y=370)

    # assignment start_label into Config.current_page.
    Config.current_page = start_label


def init_game_label(root, window_width, window_height):
    """The function responsible for initializing the game_label, which contains objects informing about the game state
    and a game reset button."""
    # Stop the sound of the soundtrack.
    mixer.music.stop()
    # Destroying current_page.
    Config.current_page.destroy()

    # Creating game_label and grid it into root.
    game_label = Label(root, width=window_width, height=window_height)
    game_label.grid()

    # Creating global mines_counter_object.
    Config.mines_counter_object = Label(game_label, bg="black", fg="red", font="Digital-7, 40")
    Config.mines_counter_object.grid(row=0, column=0, columnspan=6, ipadx=10, pady=30, padx=(15, 0))
    # Calling update_mines_counter from Functions.py.
    update_mines_counter()

    # Creating global face_object and assigning the game reset function to it.
    Config.face_object = Button(game_label, pady=20, padx=30, command=lambda: reset_game(init_game_board, game_label))
    Config.face_object.grid(row=0, column=Config.columns // 2 - 1, columnspan=3, pady=30)
    # Setting image of button with smiley face.
    Config.face_object["image"] = Config.images["faces"][0]

    # Creating global clock_object.
    Config.clock_object = Label(game_label, bg="black", fg="red", font="Digital-7, 40")
    Config.clock_object.grid(row=0, column=Config.columns - 6, columnspan=6, ipadx=10, pady=30)
    # Start clock.
    update_clock()

    # Creating Back button and assigning it an indirect function that configures global variables.
    Button(game_label, text="Wróć do menu", font="Digital-7, 8",
           command=lambda: configure_variables_for_start_label(root, init_start_label)).place(x=window_width-123, y=5,
                                                                                              width=100, height=25)

    def init_game_board():
        """The function responsible for initializing game_board (button panel) and calling the function to initialize
        the game_table (bomb panel and numbers of adjacent bombs)."""
        # Creating global current_list_of_buttons containing the number of buttons equal to rows x columns.
        Config.current_list_of_buttons = [Button(game_label) for _ in range(Config.rows * Config.columns)]
        # Creating local game_table from function call. This is a generated 2d list, it contains bombs and numbers 0-8.
        game_table = init_game_table()

        # Placing each button in the right place on the board and binding the function to it with the corresponding
        # parameters.
        for i in range(Config.rows):
            for j in range(Config.columns):
                # Executing the button placement function for the appropriate values: i,j = x,y.
                make_grid(j, i)
                # Assigning the button object from the list to a variable and setting it as a parameter to the lambda
                # function.
                button = Config.current_list_of_buttons[i * Config.columns + j]
                # binding the release of the left mouse button as the function of checking what is hidden under the
                # pressed button.
                button.config(command=lambda b=button: left_click(b, game_table, game_label))
                # Bind holding down the left mouse button to change the face image to scared.
                button.bind("<Button-1>", lambda event: scared_face())
                # Binding releasing the left mouse button to change the face image to smiling.
                button.bind("<ButtonRelease-1>", lambda event: normal_face())
                # Binding right click to insert or remove flags.
                button.bind("<Button-3>", lambda event, b=button: right_click(b, game_table))

    # First function call initializing game_board.
    init_game_board()
    # Assignment game_label into Config.current_page.
    Config.current_page = game_label
