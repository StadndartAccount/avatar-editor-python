import tkinter as tk
from Components.HeaderFrame import *
from Components.AvatarFrame import *
from Components.OptionsSelectorMainFrame import *

class Main:
    def __init__(self):
        root = tk.Tk()
        root.title("Avatar Creator")
        root.geometry("560x720")
        root.resizable(False, False)

        header_frame = HeaderFrame(root, background="white")
        header_frame.pack(fill=tk.X)
        header_frame.delegate = self

        self.avatar_frame = AvatarFrame(root)
        self.avatar_frame.pack(fill=tk.X)
        self.avatar_frame.configure(height=280) # temp

        options_selector_frame = OptionsSelectorMainFrame(root, background="white")
        options_selector_frame.pack(fill=tk.BOTH, expand=True)
        options_selector_frame.delegate = self

        root.mainloop()


    def export(self):
        self.model.export_avatar()


    def select_new_option(self, option, new_image):
        self.avatar_frame.set_new_option_value(option, new_image)


    def select_new_color(self, option, new_color):
        self.avatar_frame.update_option_color(option, new_color)


Main()