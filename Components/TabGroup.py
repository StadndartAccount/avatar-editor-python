import tkinter as tk
from AvatarLayer import *

class TabGroup(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        button_1 = tk.Button(self, height=2, width=1, text="BODY", command=lambda: self.select_tab(AvatarLayer.body))
        button_1.pack(pady=4, side=tk.LEFT, padx=4, fill=tk.X, expand=True)

        button_2 = tk.Button(self, height=2, width=1, text="HAIR", command=lambda: self.select_tab(AvatarLayer.hair))
        button_2.pack(pady=4, side=tk.LEFT, padx=4, fill=tk.X, expand=True)

        button_3 = tk.Button(self, height=2, width=1, text="FACE", command=lambda: self.select_tab(AvatarLayer.eyes))
        button_3.pack(pady=4, side=tk.LEFT, padx=4, fill=tk.X, expand=True)

        button_4 = tk.Button(self, height=2, width=1, text="SCENE", command=lambda: self.select_tab(AvatarLayer.scene) )
        button_4.pack(pady=4, side=tk.LEFT, padx=4, fill=tk.X, expand=True)

    def select_tab(self, selected_option):
        self.delegate.select_tab(selected_option)