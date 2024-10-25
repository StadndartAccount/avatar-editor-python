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
        self.delegate.select_new_color(new_color=new_color)


class HairCollection(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.character_singleton = CharacterSingleton()

        self.model = HairSelectionModel()
        self.image_processor = ImageProcessor()

        self.hair_palette_delegate = HairPaletteDelegate()
        self.hair_palette_delegate.delegate = self

        self.item_selected(self.model.options[0])
        self.select_new_color(self.model.colors[0])


    def update_content(self): 
        for widget in self.winfo_children():
            widget.destroy()

        self.content_frame = tk.Frame(self)
        self.content_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        palette_container_frame = tk.Frame(self)
        palette_container_frame.pack(fill=tk.X, expand=True, side=tk.LEFT, anchor=tk.N)

        hair_color_label = tk.Label(palette_container_frame, text="Hair")
        hair_color_label.pack(fill=tk.X, expand=True)

        hair_palette_frame = PaletteFrame(palette_container_frame, colors=self.model.colors, selected_color=self.model.get_selected_color(), columns_number=3)
        hair_palette_frame.pack(fill=tk.X, expand=True)
        hair_palette_frame.delegate = self.hair_palette_delegate

        columns_number = 3
        cell_side = 132
        border_width = 2
        margin = 4

        rows = split_into_chunks(self.model.options, columns_number)

        for row in rows:
            row_frame = tk.Frame(self.content_frame)
            row_frame.pack(fill=tk.X, side=tk.TOP)

            for option in row:
                back_hair_image = self.image_processor.process_image(option.back.get_image_path(), self.character_singleton.get_color(AvatarLayer.back_hair)).resize((cell_side, cell_side))
                head_image = self.image_processor.process_image(Head.square_head.get_image_path(), self.character_singleton.get_color(AvatarLayer.head)).resize((cell_side, cell_side))
                front_hair_image = self.image_processor.process_image(option.front.get_image_path(), self.character_singleton.get_color(AvatarLayer.front_hair)).resize((cell_side, cell_side))

                overlay_image = self.image_processor.overlay_png_images([
                    back_hair_image,
                    head_image,
                    front_hair_image,
                ])
                
                photo = ImageTk.PhotoImage(overlay_image)
                
                if option == self.model.get_selected_option():
                    item_border = tk.Frame(row_frame, bg="black")
                    item_frame = tk.Button(item_border, image=photo, height=cell_side - border_width*2, width=cell_side - border_width*2)
                    item_frame.image = photo
                    item_border.pack(padx=margin, pady=margin, side=tk.LEFT)
                    item_frame.pack(padx=border_width, pady=border_width)
                else:
                    item_frame = tk.Button(row_frame, image=photo, height=cell_side, width=cell_side, command=lambda hair=option: self.item_selected(hair))
                    item_frame.image = photo
                    item_frame.pack(padx=margin, pady=margin, side=tk.LEFT)


    def item_selected(self, hair_container: Hair):
        self.model.selected_option = hair_container
        self.character_singleton.set_image(AvatarLayer.front_hair, hair_container.front.get_image_path())
        self.character_singleton.set_image(AvatarLayer.back_hair, hair_container.back.get_image_path())
        self.update_content()


    def select_new_color(self, new_color):
        self.model.selected_color = new_color
        self.character_singleton.set_color(AvatarLayer.front_hair, new_color)        
        self.character_singleton.set_color(AvatarLayer.back_hair, new_color)        
        self.update_content()
