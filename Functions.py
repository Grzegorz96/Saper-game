from tkinter import *
import Config
import random


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


def update_clock(root):
    if Config.is_clock_work:
        Config.time += 1
        Config.clock_object["text"] = "0" * (4 - len(str(Config.time))) + str(Config.time)
        root.after(1000, update_clock, root)


def update_mines_counter():
    Config.mines_counter_object["text"] = "0" * (4 - len(str(Config.flags_number_left))) + str(Config.flags_number_left)


def change_face():
    if not Config.is_this_end_game:
        Config.face_object["image"] = Config.images["faces"][0]


def make_grid(buttons, x, y):
    if x == 0:
        buttons[y*Config.columns+x].grid(row=y+1, column=x, padx=(20, 0))

    else:
        buttons[y*Config.columns+x].grid(row=y+1, column=x)


def lost_game(buttons, game_table, root):
    Config.is_this_end_game = True
    Config.is_clock_work = False
    for i in range(Config.rows):
        for j in range(Config.columns):
            if isinstance(buttons[i * Config.columns + j], Button) and buttons[i * Config.columns + j]["state"]\
                    != "disabled":
                buttons[i * Config.columns + j]["state"] = "disabled"
                buttons[i * Config.columns + j].unbind("<Button-1>")
                buttons[i * Config.columns + j].unbind("<Button-3>")
                if game_table[i][j] == 'x':
                    buttons[i * Config.columns + j] = Label(root, image=Config.images["mines"][0])
                    make_grid(buttons, j, i)


def won_game(buttons):

    Config.is_this_end_game = True
    Config.is_clock_work = False
    for i in range(Config.rows):
        for j in range(Config.columns):
            if isinstance(buttons[i * Config.columns + j], Button) and buttons[i * Config.columns + j]["state"]\
                    != "disabled":
                buttons[i * Config.columns + j]["state"] = "disabled"
                buttons[i * Config.columns + j].unbind("<Button-1>")
                buttons[i * Config.columns + j].unbind("<Button-3>")


def update_button(buttons, index, field, game_table, root):
    buttons[index].configure(state="disabled", border=1, highlightbackground="black")
    buttons[index].unbind("<Button-1>")
    buttons[index].unbind("<Button-3>")

    if field != 0:

        buttons[index] = Label(root, image=Config.images["digits"][field - 1])
        make_grid(buttons, index % Config.columns, index//Config.columns)

    else:
        neighbours = find_neighbours(index // Config.columns, index % Config.columns)
        for y, x in neighbours:
            if isinstance(buttons[y * Config.columns + x], Button) and buttons[y * Config.columns + x]["state"]\
                    != "disabled" and not buttons[y * Config.columns + x].cget("image"):
                update_button(buttons, y * Config.columns + x, game_table[y][x], game_table, root)


def left_click(buttons, button, game_table, root):
    if not button.cget("image"):

        Config.face_object["image"] = Config.images["faces"][1]
        index = buttons.index(button)
        field = game_table[index//Config.columns][index % Config.columns]

        if field == "x":
            Config.face_object["image"] = Config.images["faces"][2]
            lost_game(buttons, game_table, root)
        else:
            update_button(buttons, index, field, game_table, root)


def right_click(buttons, button, game_table):
    Config.face_object["image"] = Config.images["faces"][1]

    index = buttons.index(button)

    field = game_table[index // Config.columns][index % Config.columns]

    if button.cget("image"):
        button['image'] = ""

        Config.flags_number_left += 1
        if field == "x":

            Config.number_guessed_mines -= 1
    else:
        if Config.flags_number_left != 0:
            button['image'] = Config.images['flag']
            Config.flags_number_left -= 1
            if field == "x":
                Config.number_guessed_mines += 1
                if Config.number_guessed_mines == Config.mines_number:
                    Config.face_object["image"] = Config.images["faces"][3]
                    won_game(buttons)
    update_mines_counter()


def loading_images():
    Config.images["digits"] = [PhotoImage(file="Photos/" + str(i) + ".png") for i in range(1, 9)]
    Config.images["faces"] = [PhotoImage(file="Photos/buzka" + str(i) + ".png") for i in range(1, 5)]
    Config.images["flag"] = PhotoImage(file="Photos/flaga.png")
    Config.images["mines"] = [PhotoImage(file="Photos/mina.png"), PhotoImage(file="Photos/pierwsza.png")]


def reset_game(init_game_board, root):
    init_game_board(root)
    Config.face_object["image"] = Config.images["faces"][0]
    Config.number_guessed_mines = 0
    Config.is_this_end_game = False
    Config.flags_number_left = Config.mines_number
    update_mines_counter()

    Config.time = 0
    if not Config.is_clock_work:
        Config.is_clock_work = True
        update_clock(root)
