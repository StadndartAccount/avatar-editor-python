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

        rows_number = int((len(self.model.body_images) + columns_number - 1) / columns_number)

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

        for index, image_path in enumerate(self.model.body_images):
            image = Image.open(f"Assets/Body/{image_path}").resize((146, 146))
            photo = ImageTk.PhotoImage(image)

            item_frame = tk.Button(content_frame, image=photo, height=146, width=146, command=lambda img=image_path: self.item_selected(img))
            item_frame.image = photo
            row = int(index / columns_number)
            column = int(index % columns_number)
            item_frame.grid(row=row, column=column)


    def item_selected(self, new_value):
        self.delegate.select_new_option(option=AvatarLayer.body, new_image=new_value)

    def handle_clicked_color(self, new_color):
        self.delegate.select_new_color(option=AvatarLayer.body, new_color=new_color)
