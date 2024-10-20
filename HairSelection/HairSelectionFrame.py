import tkinter as tk
from Components.ScrollableFrame import *
from PIL import ImageTk
from HairSelection.HairSelectionModel import *
from AvatarLayer import *
from Components.PaletteFrame import *
from ImageProcessor import *
from CharacterSingleton import *
from Tools import split_into_chunks


class HairPaletteDelegate:
    def handle_clicked_color(self, new_color):
        self.delegate.select_new_color(option=AvatarLayer.hair, new_color=new_color)


class HairCollection(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.character_singleton = CharacterSingleton()

        self.model = HairSelectionModel()
        self.image_processor = ImageProcessor()

        hair_palette_delegate = HairPaletteDelegate()
        hair_palette_delegate.delegate = self

        self.content_frame = tk.Frame(self)
        self.content_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.update_content()

        palette_container_frame = tk.Frame(self)
        palette_container_frame.pack(fill=tk.X, expand=True, side=tk.LEFT, anchor=tk.N)

        hair_color_label = tk.Label(palette_container_frame, text="Hair")
        hair_color_label.pack(fill=tk.X, expand=True)

        hair_palette_frame = PaletteFrame(palette_container_frame, colors=self.model.colors, columns_number=3)
        hair_palette_frame.pack(fill=tk.X, expand=True)
        hair_palette_frame.delegate = hair_palette_delegate


    def update_content(self): 
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        columns_number = 3
        
        rows = split_into_chunks(self.model.options, columns_number)
        cell_side = 132

        for row_index, row in enumerate(rows):
            row_frame = tk.Frame(self.content_frame)
            row_frame.pack(fill=tk.X, side=tk.TOP)

            for option_index, option in enumerate(row):
                hair_image = self.image_processor.process_image(option.get_image_path(), self.character_singleton.get_color(AvatarLayer.hair)).resize((cell_side, cell_side))
                head_image = self.character_singleton.get_layer_as_png(AvatarLayer.head).resize((cell_side, cell_side))

                overlay_image = self.image_processor.overlay_png_images([
                    head_image,
                    hair_image,
                ])
                
                photo = ImageTk.PhotoImage(overlay_image)

                current_index = (row_index * columns_number) + option_index
                
                if current_index == self.model.selected_option_index:
                    item_border = tk.Frame(row_frame, height=cell_side, width=cell_side, bg="red")
                    item_frame = tk.Button(item_border, image=photo, height=cell_side, width=cell_side, command=lambda combination=option, index=current_index: self.item_selected(combination, index))
                    item_frame.image = photo
                    item_border.pack(padx=1, pady=1, side=tk.LEFT)
                    item_frame.pack(padx=2, pady=2)
                else:
                    item_frame = tk.Button(row_frame, image=photo, height=cell_side, width=cell_side, command=lambda combination=option, index=current_index: self.item_selected(combination, index))
                    item_frame.image = photo
                    item_frame.pack(padx=1, pady=1, side=tk.LEFT)


    def item_selected(self, hair: Hair, index):
        self.model.selected_option_index = index
        self.character_singleton.set_image(AvatarLayer.hair, hair.get_image_path())
        self.update_content()


    def select_new_color(self, option, new_color):
        self.character_singleton.set_color(option, new_color)        
        self.update_content()
