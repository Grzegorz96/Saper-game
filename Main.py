from GUI import init_window, init_top_panel, init_game_board
from Functions import loading_images


if __name__ == "__main__":
    root = init_window()
    loading_images()
    init_top_panel(root)
    init_game_board(root)

    root.mainloop()
