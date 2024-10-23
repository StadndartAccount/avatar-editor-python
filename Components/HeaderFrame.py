import tkinter as tk

class HeaderFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        export_button = tk.Button(self, height=2, width=4, text="EXPORT", command=lambda: self.export_tapped())
        export_button.pack(side=tk.RIGHT, pady=8, padx=4)

        to_history_button = tk.Button(self, height=2, width=4, text="SAVE", command=lambda: self.to_history_tapped())
        to_history_button.pack(side=tk.RIGHT, pady=8, padx=4)

        random_button = tk.Button(self, height=2, width=4, text="RANDOM", command=lambda: self.random_tapped())
        random_button.pack(side=tk.RIGHT, pady=8, padx=4)


    def export_tapped(self):
        self.delegate.export()


    def to_history_tapped(self):
        self.delegate.add_to_history()


    def random_tapped(self):
        self.delegate.randomize_character()