from tkinter import *
import Config
from Functions import init_game_table, make_grid, right_click, update_clock, update_mines_counter, change_face,\
    left_click, reset_game


def init_window():
    root = Tk()
    # Definition width and height of app window.
    window_width = 880
    window_height = 600
    # Definition width and height of monitor window.
    screen_width = 1920
    screen_height = 1080
    # Setting center of window
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    # Making tittle, geometry, resizable, color background, photos.
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root.title("SAPER")
    root.resizable(width=True, height=True)

    # Return root object into Main module.
    return root


def init_top_panel(root):
    Config.mines_counter_object = Label(root, bg="black", fg="red", font="Digital-7, 40")
    Config.mines_counter_object.grid(row=0, column=0, columnspan=6, ipadx=10, pady=30, padx=(15, 0))
    update_mines_counter()

    Config.face_object = Button(root, pady=20, padx=30, command=lambda: reset_game(init_game_board, root))
    Config.face_object.grid(row=0, column=Config.columns // 2 - 1, columnspan=3, pady=30)
    Config.face_object["image"] = Config.images["faces"][0]

    Config.clock_object = Label(root, bg="black", fg="red", font="Digital-7, 40")
    Config.clock_object.grid(row=0, column=Config.columns - 6, columnspan=6, ipadx=10, pady=30)
    update_clock(root)


def init_game_board(root):
    buttons = [Button(root) for _ in range(Config.rows * Config.columns)]
    game_table = init_game_table()

    for i in range(Config.rows):
        for j in range(Config.columns):
            make_grid(buttons, j, i)
            button = buttons[i * Config.columns + j]
            button.bind("<Button-1>", lambda event, b=button: left_click(buttons, b, game_table, root))
            button.bind("<Button-3>", lambda event, b=button: right_click(buttons, b, game_table))

            button.bind("<ButtonRelease>", lambda event: change_face())
