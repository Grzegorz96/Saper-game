from GUI import init_window, init_start_label
from Functions import loading_images, init_sound_mixer


if __name__ == "__main__":
    root = init_window()
    init_sound_mixer()
    loading_images()
    init_start_label(root)
    root.mainloop()
