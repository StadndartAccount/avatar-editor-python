import tkinter as tk
from Components.HeaderFrame import *
from Components.AvatarFrame import *
from Components.OptionsSelectorMainFrame import *

class Main:
    def __init__(self):
        root = tk.Tk()
        root.title("Avatar Creator")
        root.geometry("584x720")
        root.resizable(False, False)

        header_frame = HeaderFrame(root, background="white")
        header_frame.pack(fill=tk.X)
        header_frame.delegate = self

        self.avatar_frame = AvatarFrame(root)
        self.avatar_frame.pack(fill=tk.X)
        self.avatar_frame.configure(height=280) # temp

        options_selector_frame = OptionsSelectorMainFrame(root)
        options_selector_frame.pack(fill=tk.BOTH, expand=True)

        root.mainloop()


    def export(self):
        print("export")


Main()