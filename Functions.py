from tkinter import *
import Config
import random
from pygame import mixer


def init_game_table():
    game_table = [[0 for _ in range(Config.columns)] for _ in range(Config.rows)]
    mines_to_be_drawn = Config.mines_number

    while mines_to_be_drawn:
        x = random.randint(0, Config.columns-1)
        y = random.randint(0, Config.rows-1)

        if game_table[y][x] == 0:
            game_table[y][x] = "x"
            mines_to_be_drawn -= 1

    for i in range(Config.rows):
        for j in range(Config.columns):

            if game_table[i][j] == 0:
                neighbours = find_neighbours(i, j)
                number_neighbours_mines = 0

                for y, x in neighbours:
                    if game_table[y][x] == "x":
                        number_neighbours_mines += 1

                game_table[i][j] = number_neighbours_mines

    return game_table


def find_neighbours(y, x):
    neighbours = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                if 0 <= y + i < Config.rows:
                    if 0 <= x + j < Config.columns:
                        neighbours.append((y+i, x+j))

    return neighbours


def update_clock():
    if Config.is_clock_work:
        Config.time += 1
        Config.clock_object["text"] = "0" * (4 - len(str(Config.time))) + str(Config.time)
        Config.clock_object.after(1000, update_clock)


def update_mines_counter():
    Config.mines_counter_object["text"] = "0" * (4 - len(str(Config.flags_number_left))) + str(Config.flags_number_left)


def normal_face():
    Config.face_object["image"] = Config.images["faces"][0]


def scared_face():
    Config.face_object["image"] = Config.images["faces"][1]


def make_grid(x, y):
    if x == 0:
        Config.current_list_of_buttons[y*Config.columns+x].grid(row=y+1, column=x, padx=(20, 0))

    else:
        Config.current_list_of_buttons[y*Config.columns+x].grid(row=y+1, column=x)


def lost_game(game_table, game_label, button):
    Config.is_clock_work = False
    for i in range(Config.rows):
        for j in range(Config.columns):
            if (isinstance(Config.current_list_of_buttons[i * Config.columns + j], Button) and
                    Config.current_list_of_buttons[i * Config.columns + j]["state"] != "disabled"):
                Config.current_list_of_buttons[i * Config.columns + j]["state"] = "disabled"
                Config.current_list_of_buttons[i * Config.columns + j].unbind("<Button-1>")
                Config.current_list_of_buttons[i * Config.columns + j].unbind("<Button-3>")
                Config.current_list_of_buttons[i * Config.columns + j].unbind("<ButtonRelease-1>")

                if game_table[i][j] == 'x':
                    if Config.current_list_of_buttons[i * Config.columns + j] is button:
                        Config.current_list_of_buttons[i * Config.columns + j] = Label(game_label,
                                                                                       image=Config.images["mines"][1])
                    else:
                        Config.current_list_of_buttons[i * Config.columns + j] = Label(game_label,
                                                                                       image=Config.images["mines"][0])
                    make_grid(j, i)

                elif Config.current_list_of_buttons[i * Config.columns + j].cget("image"):
                    Config.current_list_of_buttons[i * Config.columns + j]["image"] = Config.images["flags"][1]


def won_game():
    Config.is_clock_work = False
    for i in range(Config.rows):
        for j in range(Config.columns):
            if (isinstance(Config.current_list_of_buttons[i * Config.columns + j], Button)
                    and Config.current_list_of_buttons[i * Config.columns + j]["state"] != "disabled"):
                Config.current_list_of_buttons[i * Config.columns + j]["state"] = "disabled"
                Config.current_list_of_buttons[i * Config.columns + j].unbind("<Button-1>")
                Config.current_list_of_buttons[i * Config.columns + j].unbind("<Button-3>")
                Config.current_list_of_buttons[i * Config.columns + j].unbind("<ButtonRelease-1>")


def update_button(index, field, game_table, game_label):
    Config.current_list_of_buttons[index].configure(state="disabled", border=1, highlightbackground="black")
    Config.current_list_of_buttons[index].unbind("<Button-1>")
    Config.current_list_of_buttons[index].unbind("<Button-3>")
    Config.current_list_of_buttons[index].unbind("<ButtonRelease-1>")

    if field != 0:
        if Config.permission_to_play_one_sound:
            if field == 1:
                run_sound_effect("1.wav")
            elif field == 2:
                run_sound_effect("2.wav")
            elif field == 3:
                run_sound_effect("3.wav")
            elif field == 4:
                run_sound_effect("4.wav")
            elif field == 5:
                run_sound_effect("5.wav")
            elif field == 6:
                run_sound_effect("6.wav")
            elif field == 7:
                run_sound_effect("7.wav")
            elif field == 8:
                run_sound_effect("8.wav")

            Config.permission_to_play_one_sound = False

        Config.current_list_of_buttons[index] = Label(game_label, image=Config.images["digits"][field - 1])
        make_grid(index % Config.columns, index//Config.columns)

    else:
        if Config.permission_to_play_one_sound:
            run_sound_effect("recursion.wav")
            Config.permission_to_play_one_sound = False
        neighbours = find_neighbours(index // Config.columns, index % Config.columns)
        for y, x in neighbours:
            if (isinstance(Config.current_list_of_buttons[y * Config.columns + x], Button)
                    and Config.current_list_of_buttons[y * Config.columns + x]["state"] != "disabled"
                    and not Config.current_list_of_buttons[y * Config.columns + x].cget("image")):
                update_button(y * Config.columns + x, game_table[y][x], game_table, game_label)


def left_click(button, game_table, game_label):
    if not button.cget("image"):

        index = Config.current_list_of_buttons.index(button)
        field = game_table[index//Config.columns][index % Config.columns]

        if field == "x":
            run_sound_effect("bomb.wav")
            Config.face_object["image"] = Config.images["faces"][2]
            lost_game(game_table, game_label, button)
        else:
            Config.permission_to_play_one_sound = True
            update_button(index, field, game_table, game_label)


def right_click(button, game_table):
    index = Config.current_list_of_buttons.index(button)

    field = game_table[index // Config.columns][index % Config.columns]

    if button.cget("image"):
        run_sound_effect("delete_flag.wav")
        button["image"] = ""

        Config.flags_number_left += 1
        if field == "x":

            Config.number_guessed_mines -= 1
    else:
        if Config.flags_number_left > 0:
            run_sound_effect("put_flag.wav")
            button["image"] = Config.images["flags"][0]
            Config.flags_number_left -= 1
            if field == "x":
                Config.number_guessed_mines += 1
                if Config.number_guessed_mines == Config.mines_number:
                    run_sound_effect("winner.wav")
                    Config.face_object["image"] = Config.images["faces"][3]
                    won_game()
        else:
            run_sound_effect("empty_flag.wav")

    update_mines_counter()


def loading_images():
    Config.images["digits"] = [PhotoImage(file="Photos/" + str(i) + ".png") for i in range(1, 9)]
    Config.images["faces"] = [PhotoImage(file="Photos/face" + str(i) + ".png") for i in range(1, 5)]
    Config.images["flags"] = [PhotoImage(file="Photos/flag.png"), PhotoImage(file="Photos/crossed_out_flag.png")]
    Config.images["mines"] = [PhotoImage(file="Photos/mine.png"), PhotoImage(file="Photos/first_mine.png")]


def reset_game(init_game_board, game_label):
    run_sound_effect("button.wav")
    Config.is_clock_work = False
    for button in Config.current_list_of_buttons:
        button.destroy()
    init_game_board()
    Config.face_object["image"] = Config.images["faces"][0]
    Config.number_guessed_mines = 0
    Config.flags_number_left = Config.mines_number
    update_mines_counter()

    Config.time = 0
    Config.clock_object.destroy()
    Config.clock_object = Label(game_label, bg="black", fg="red", font="Digital-7, 40")
    Config.clock_object.grid(row=0, column=Config.columns - 6, columnspan=6, ipadx=10, pady=30)
    Config.is_clock_work = True
    update_clock()


def configure_variables_for_game_label(rows, columns, mines_number, window_width, window_height, root, init_game_label):
    run_sound_effect("button.wav")
    Config.rows = rows
    Config.columns = columns
    Config.mines_number = mines_number
    Config.flags_number_left = Config.mines_number
    Config.is_clock_work = True
    create_app_geometry(root, window_width, window_height)
    init_game_label(root, window_width, window_height)


def configure_variables_for_start_label(root, init_start_label):
    run_sound_effect("button.wav")
    Config.is_clock_work = False
    Config.face_object = None
    Config.mines_counter_object = None
    Config.clock_object = None
    Config.current_list_of_buttons = None
    Config.rows = 0
    Config.columns = 0
    Config.time = 0
    Config.mines_number = 0
    Config.number_guessed_mines = 0
    create_app_geometry(root, 880, 600)
    init_start_label(root)


def create_app_geometry(root, window_width, window_height):
    # Definition width and height of monitor window.
    screen_width = 1920
    screen_height = 1080
    # Setting center of window
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    # Making tittle, geometry, resizable, color background, photos.
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")


# Initialization sound mixer for app.
def init_sound_mixer():
    mixer.init()
    # Setting volume on 0.2.
    mixer.music.set_volume(0.2)


def run_sound_effect(sound):
    # Making object of fifty/fifty sound effect, setting volume on 0.5 and run.
    sound_effect = mixer.Sound(fr"Sounds/{sound}")
    sound_effect.set_volume(0.2)
    sound_effect.play()
