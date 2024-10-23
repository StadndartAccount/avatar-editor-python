import tkinter as tk
from Components.ScrollableFrame import *
from PIL import ImageTk
from HistorySelection.HistoryCollectionModel import *
from AvatarLayer import *
from Components.PaletteFrame import *
from ImageProcessor import *
from CharacterSingleton import *
from Tools import split_into_chunks
from DataProcessor import remove_object

class HistoryCollection(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.character_singleton = CharacterSingleton()

        self.model = HistorySelectionModel()
        self.image_processor = ImageProcessor()


    def update_content(self): 
        self.model.update_options()

        for widget in self.winfo_children():
            widget.destroy()

        self.content_frame = tk.Frame(self)
        self.content_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        columns_number = 4
        cell_side = 132
        margin = 4

        rows = split_into_chunks(self.model.options, columns_number)

        for row in rows:
            row_frame = tk.Frame(self.content_frame)
            row_frame.pack(fill=tk.X, side=tk.TOP)

            for option in row:
                images = list(map(lambda params: self.image_processor.process_image(params.image_path, params.color).resize((cell_side, cell_side)), option.layers.values()))

                overlay_image = self.image_processor.overlay_png_images(images)
                
                photo = ImageTk.PhotoImage(overlay_image)
                
                item_frame = tk.Button(row_frame, image=photo, height=cell_side, width=cell_side, command=lambda item=option: self.item_selected(item))
                item_frame.image = photo
                item_frame.pack(padx=margin, pady=margin, side=tk.LEFT)

                delete_button = tk.Label(item_frame, text="X")
                delete_button.place(x=8, y=8, anchor=tk.NW)
                delete_button.bind("<Button-1>", lambda e, item=option: self.delete_item(item))

    
    def item_selected(self, item: HisotryItem):
        for layer, params in item.layers.items():
            self.character_singleton.set_color(layer, params.color)
            self.character_singleton.set_image(layer, params.image_path)


    def delete_item(self, item: HisotryItem):
        remove_object(item.id)
        self.model.update_options()
        self.update_content()
