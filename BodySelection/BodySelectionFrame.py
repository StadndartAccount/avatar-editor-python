import tkinter as tk
from Components.ScrollableFrame import *
from PIL import ImageTk, ImageColor
from BodySelection.BodySelectionModel import *
from AvatarLayer import *
from Components.PaletteFrame import *
from ImageProcessor import *
from CharacterSingleton import *
from ColorProcessor import *
from Tools import split_into_chunks


class BodyPaletteDelegate:
    def handle_clicked_color(self, new_color):
        self.delegate.select_new_color(option=AvatarLayer.body, new_color=new_color)


class HeadPaletteDelegate:
    def handle_clicked_color(self, new_color):
        self.delegate.select_new_color(option=AvatarLayer.head, new_color=new_color)
 

class BodyCollection(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.character_singleton = CharacterSingleton()

        self.model = BodySelectionModel()
        self.image_processor = ImageProcessor()

        self.body_palette_delegate = BodyPaletteDelegate()
        self.body_palette_delegate.delegate = self
        self.head_palette_delegate = HeadPaletteDelegate()
        self.head_palette_delegate.delegate = self

        self.item_selected(self.model.selected_option)
        self.select_new_color(AvatarLayer.head, self.model.selected_head_color)
        self.select_new_color(AvatarLayer.body, self.model.selected_body_color)


    def update_content(self): 
        for widget in self.winfo_children():
            widget.destroy()

        self.content_frame = tk.Frame(self)
        self.content_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        palette_container_frame = tk.Frame(self)
        palette_container_frame.pack(fill=tk.X, expand=True, side=tk.RIGHT, anchor=tk.NE)

        head_color_label = tk.Label(palette_container_frame, text="Head")
        head_color_label.pack(fill=tk.X, expand=True)

        head_palette_frame = PaletteFrame(palette_container_frame, colors=self.model.head_colors, columns_number=3, selected_color=self.model.selected_head_color)
        head_palette_frame.pack(fill=tk.X, expand=True)
        head_palette_frame.delegate = self.head_palette_delegate

        body_color_label = tk.Label(palette_container_frame, text="Clothes")
        body_color_label.pack(fill=tk.X, expand=True)

        body_palette_frame = PaletteFrame(palette_container_frame, colors=self.model.body_colors, columns_number=3, selected_color=self.model.selected_body_color)
        body_palette_frame.pack(fill=tk.X, expand=True)
        body_palette_frame.delegate = self.body_palette_delegate

        columns_number = 3
        cell_side = 132
        border_width = 2
        margin = 4

        rows = split_into_chunks(self.model.options, columns_number)

        for row in rows:
            row_frame = tk.Frame(self.content_frame)
            row_frame.pack(fill=tk.X, side=tk.TOP)

            for option in row:
                hair_image = self.character_singleton.get_layer_as_png(AvatarLayer.hair).resize((cell_side, cell_side))
                head_image = self.image_processor.process_image(option.head.get_image_path(), self.character_singleton.get_color(AvatarLayer.head)).resize((cell_side, cell_side))
                body_image = self.image_processor.process_image(option.body.get_image_path(), self.character_singleton.get_color(AvatarLayer.body)).resize((cell_side, cell_side))

                overlay_image = self.image_processor.overlay_png_images([
                    body_image,
                    head_image,
                    hair_image,
                ])

                photo = ImageTk.PhotoImage(overlay_image)
                
                if option == self.model.selected_option:
                    item_border = tk.Frame(row_frame, bg="white")
                    item_frame = tk.Button(item_border, image=photo, height=cell_side - border_width*2, width=cell_side - border_width*2)
                    item_frame.image = photo
                    item_border.pack(padx=margin, pady=margin, side=tk.LEFT)
                    item_frame.pack(padx=border_width, pady=border_width)
                else:
                    item_frame = tk.Button(row_frame, image=photo, height=cell_side, width=cell_side, command=lambda combination=option: self.item_selected(combination))
                    item_frame.image = photo
                    item_frame.pack(padx=margin, pady=margin, side=tk.LEFT)

    
    def item_selected(self, silhouette: Silhouette):
        self.model.selected_option = silhouette
        self.character_singleton.set_image(AvatarLayer.body, silhouette.body.get_image_path())
        self.character_singleton.set_image(AvatarLayer.head, silhouette.head.get_image_path())
        self.update_content()


    def select_new_color(self, option, new_color):
        match option:
            case AvatarLayer.head:
                rgb_color = ImageColor.getrgb(new_color)
                mouth_color = (rgb_color[0] - 30, rgb_color[1] - 30, rgb_color[2] - 30, 255)
                self.character_singleton.set_color(AvatarLayer.mouth, rgb2hex(mouth_color))  
                self.character_singleton.set_color(AvatarLayer.head, new_color)  
                self.model.selected_head_color = new_color    
            case AvatarLayer.body:
                self.character_singleton.set_color(option, new_color)
                self.model.selected_body_color = new_color    
            case _:
                print("unknown case")    
                
        
        self.update_content()