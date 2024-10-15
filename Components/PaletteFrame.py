import tkinter as tk
import numpy as np

class PaletteFrame(tk.Frame):
    def __init__(self, master, colors = [], *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        columns_number = 2
        rows_number = int((len(colors) + columns_number - 1) / columns_number)

        rows = np.array_split(colors, rows_number)

        for row_colors in rows:
            row_frame = tk.Frame(self)
            row_frame.pack(fill=tk.X, expand=True)

            for color in row_colors:
                string_color = self.convert_color_to_string(color)
                color_square = tk.Frame(row_frame, background=string_color, width=32, height=32)
                color_square.pack(padx=4, pady=4, side=tk.LEFT)
                color_square.bind("<Button-1>", lambda e, color=color: self.handle_clicked_color(color))

    def handle_clicked_color(self, color):
        self.delegate.handle_clicked_color(color)

    def convert_color_to_string(self, color):
        return f"#{f"{color[0]:02x}"}{f"{color[1]:02x}"}{f"{color[2]:02x}"}"