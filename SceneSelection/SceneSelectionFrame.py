import tkinter as tk
from Components.ScrollableFrame import *
from AvatarLayer import *
from SceneSelection.SceneSelectionModel import *
from Components.PaletteFrame import *
from PIL import Image, ImageTk

class SceneCollection(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.model = SceneSelectionModel()

        columns_number = 3

        rows_number = int((len(self.model.images) + columns_number - 1) / columns_number)

        content_frame = tk.Frame(self)
        content_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        palette_frame = PaletteFrame(self, colors=self.model.colors)
        palette_frame.pack(fill=tk.X, expand=True, side=tk.LEFT, anchor=tk.N)
        palette_frame.delegate = self

        for column in range(columns_number): content_frame.columnconfigure(index=column, weight=1)
        for row in range(rows_number): content_frame.rowconfigure(index=row, weight=1)

        for index, image_path in enumerate(self.model.images):
            image = Image.open(f"Assets/Scene/{image_path}").resize((146, 146))
            photo = ImageTk.PhotoImage(image)

            item_frame = tk.Button(content_frame, image=photo, height=146, width=146, command=lambda img=image_path: self.item_selected(img))
            item_frame.image = photo
            row = int(index / columns_number)
            column = int(index % columns_number)
            item_frame.grid(row=row, column=column)


    def item_selected(self, new_value):
        self.delegate.select_new_option(option=AvatarLayer.scene, new_image=new_value)

    def handle_clicked_color(self, new_color):
        self.delegate.select_new_color(option=AvatarLayer.scene, new_color=new_color)