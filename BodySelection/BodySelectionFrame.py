import tkinter as tk
from Components.ScrollableFrame import *
from PIL import Image, ImageTk
from BodySelection.BodySelectionModel import *
from AvatarLayer import *
from Components.PaletteFrame import *
from ImageProcessor import *

class BodyPaletteDelegate:
    def handle_clicked_color(self, new_color):
        self.delegate.select_new_color(option=AvatarLayer.body, new_color=new_color)
 
class HeadPaletteDelegate:
    def handle_clicked_color(self, new_color):
        self.delegate.select_new_color(option=AvatarLayer.head, new_color=new_color)
 

class BodyCollection(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.image_processor = ImageProcessor()

        self.model = BodySelectionModel()

        body_palette_delegate = BodyPaletteDelegate()
        body_palette_delegate.delegate = self
        head_palette_delegate = HeadPaletteDelegate()
        head_palette_delegate.delegate = self

        columns_number = 3
        rows_number = int((len(self.model.body_head_combinations) + columns_number - 1) / columns_number)

        rows = np.array_split(self.model.body_head_combinations, rows_number)

        content_frame = tk.Frame(self)
        content_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        cell_side = 132

        for row in rows:
            row_frame = tk.Frame(content_frame)
            row_frame.pack(fill=tk.X, side=tk.TOP)

            for option in row:
                body_image = Image.open(option[1].get_image_path()).resize((cell_side, cell_side))
                head_image = Image.open(option[0].get_image_path()).resize((cell_side, cell_side))

                overlay_image = self.image_processor.overlay_png_images([
                    body_image,
                    head_image
                ])

                photo = ImageTk.PhotoImage(overlay_image)

                item_frame = tk.Button(row_frame, image=photo, height=cell_side, width=cell_side, command=lambda combination=option: self.item_selected(combination))
                item_frame.image = photo
                item_frame.pack(padx=1, pady=1, side=tk.LEFT)

        palette_container_frame = tk.Frame(self)
        palette_container_frame.pack(fill=tk.X, expand=True, side=tk.LEFT, anchor=tk.N)

        body_color_label = tk.Label(palette_container_frame, text="Body")
        body_color_label.pack(fill=tk.X, expand=True)

        body_palette_frame = PaletteFrame(palette_container_frame, colors=self.model.body_colors, columns_number=3)
        body_palette_frame.pack(fill=tk.X, expand=True)
        body_palette_frame.delegate = body_palette_delegate

        head_color_label = tk.Label(palette_container_frame, text="Head")
        head_color_label.pack(fill=tk.X, expand=True)

        head_palette_frame = PaletteFrame(palette_container_frame, colors=self.model.head_colors, columns_number=3)
        head_palette_frame.pack(fill=tk.X, expand=True)
        head_palette_frame.delegate = head_palette_delegate


    def item_selected(self, body_head: tuple[Body, Head]):
        self.delegate.select_new_option(option=AvatarLayer.body, new_image=body_head[0].get_image_path())
        self.delegate.select_new_option(option=AvatarLayer.head, new_image=body_head[1].get_image_path())

    def select_new_color(self, option, new_color):
        self.delegate.select_new_color(option=option, new_color=new_color)

        match option:
            case AvatarLayer.body:
                self.body_color = new_color
            case AvatarLayer.head:
                self.head_color = new_color