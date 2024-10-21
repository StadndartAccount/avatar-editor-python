import tkinter as tk

class HeaderFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        export_button = tk.Button(self, height=2, width=4, text="EXPORT", command=lambda: self.export_tapped())
        export_button.pack(side=tk.RIGHT, pady=8, padx=4)

    def export_tapped(self):
        self.delegate.export()

