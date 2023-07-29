# Modules import.
from GUI import init_window, init_start_label
from Functions import loading_images, init_sound_mixer

# Main.
if __name__ == "__main__":
    # Creating root.
    root = init_window()
    # Initialization sound mixer call.
    init_sound_mixer()
    # Loading graphic files for project.
    loading_images()
    # Calling start_label initialization.
    init_start_label(root)
    # Running root object to mainloop.
    root.mainloop()
