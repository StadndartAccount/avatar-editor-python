import tkinter as tk
from Tab import *

class TabGroup(tk.Frame):
    def __init__(self, master, selected_tab = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        for tab in Tab:
            if tab == selected_tab:
                border_frame = tk.Frame(self, bg="black")
                border_frame.pack(pady=4, side=tk.LEFT, padx=4, fill=tk.X, expand=True)
                tab_frame = tk.Button(border_frame, height=2, width=1, text=tab.get_name(), command=lambda value=tab: self.select_tab(value))
                tab_frame.pack(padx=2, pady=2, fill=tk.BOTH, expand=True)
            else:
                tab_frame = tk.Button(self, height=2, width=1, text=tab.get_name(), command=lambda value=tab: self.select_tab(value))
                tab_frame.pack(pady=4, side=tk.LEFT, padx=4, fill=tk.X, expand=True)
        

    def select_tab(self, selected_option):
        self.delegate.select_tab(selected_option)