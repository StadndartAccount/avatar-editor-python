import tkinter as tk
from Tools import split_into_chunks


class PaletteFrame(tk.Frame):
    def __init__(self, master, colors = [], selected_color = None, columns_number = 2, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.colors = colors
        self.columns_number = columns_number
        self.selected_color = selected_color

        self.update_content()


    def handle_clicked_color(self, color):
        self.delegate.handle_clicked_color(color)
        self.update_content()

    def update_content(self):
        for widget in self.winfo_children():
            widget.destroy()

        rows = split_into_chunks(self.colors, self.columns_number)

        side_length = 32
        border_width = 2
        margin = 4

        for row_colors in rows:
            row_frame = tk.Frame(self)
            row_frame.pack(fill=tk.X, expand=True)

            for color in row_colors:
                if color == self.selected_color:
                    item_border = tk.Frame(row_frame, bg="red")
                    color_square = tk.Frame(item_border, height=side_length - border_width*2, width=side_length - border_width*2, background=color)
                    item_border.pack(padx=margin, pady=margin, side=tk.LEFT)
                    color_square.pack(padx=border_width, pady=border_width, expand=True)
                else:
                    color_square = tk.Frame(row_frame, background=color, width=side_length, height=side_length)
                    color_square.pack(padx=margin, pady=margin, side=tk.LEFT)
                    color_square.bind("<Button-1>", lambda e, color=color: self.handle_clicked_color(color))

