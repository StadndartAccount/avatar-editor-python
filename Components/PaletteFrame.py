import tkinter as tk
from Tools import split_into_chunks


class PaletteFrame(tk.Frame):
    def __init__(self, master, colors = [], columns_number = 2, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        rows = split_into_chunks(colors, columns_number)

        for row_colors in rows:
            row_frame = tk.Frame(self)
            row_frame.pack(fill=tk.X, expand=True)

            for color in row_colors:
                color_square = tk.Frame(row_frame, background=color, width=32, height=32)
                color_square.pack(padx=4, pady=4, side=tk.LEFT)
                color_square.bind("<Button-1>", lambda e, color=color: self.handle_clicked_color(color))

    def handle_clicked_color(self, color):
        self.delegate.handle_clicked_color(color)

