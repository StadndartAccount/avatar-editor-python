import tkinter as tk
from Components.ScrollableFrame import *
from PIL import Image, ImageTk
from BodySelection.BodySelectionModel import *
from Components.AvatarFrame import AvatarLayer
from Components.PaletteFrame import *


class BodyCollection(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.model = BodySelectionModel()

        columns_number = 3

        rows_number = int((len(self.model.body_head_combinations) + columns_number - 1) / columns_number)

        content_frame = tk.Frame(self)
        content_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        palette_container_frame = tk.Frame(self)
        palette_container_frame.pack(fill=tk.X, expand=True, side=tk.LEFT, anchor=tk.N)

        head_color_label = tk.Label(palette_container_frame, text="Head")
        head_color_label.pack(fill=tk.X, expand=True)

        palette_frame = PaletteFrame(palette_container_frame, colors=self.model.body_colors)
        palette_frame.pack(fill=tk.X, expand=True)
        palette_frame.delegate = self

        for column in range(columns_number): content_frame.columnconfigure(index=column, weight=1)
        for row in range(rows_number): content_frame.rowconfigure(index=row, weight=1)

        for index, body_head in enumerate(self.model.body_head_combinations):
            image = Image.open(body_head[0].get_image_path()).resize((146, 146))
            photo = ImageTk.PhotoImage(image)

            item_frame = tk.Button(content_frame, image=photo, height=146, width=146, command=lambda combination=body_head: self.item_selected(combination))
            item_frame.image = photo
            row = int(index / columns_number)
            column = int(index % columns_number)
            item_frame.grid(row=row, column=column)


    def item_selected(self, body_head: tuple[Body, Head]):
        self.delegate.select_new_option(option=AvatarLayer.body, new_image=body_head[0].get_image_path())
        self.delegate.select_new_option(option=AvatarLayer.head, new_image=body_head[1].get_image_path())

    def handle_clicked_color(self, new_color):
        self.delegate.select_new_color(option=AvatarLayer.body, new_color=new_color)
        self.delegate.select_new_color(option=AvatarLayer.head, new_color=(255, 186, 152, 100))
