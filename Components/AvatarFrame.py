import tkinter as tk
from PIL import ImageTk, Image, ImagePalette
from ImageProcessor import *
from CharacterSingleton import *


class AvatarFrame(tk.Frame):
    def __init__(self, master = None, *args, **kvargs):
        super().__init__(master, *args, **kvargs)

        self.image_processor = ImageProcessor()
        self.character_singleton = CharacterSingleton()
        self.character_singleton.add_observer(self)

        self.width = 162
        self.height = 162

        self.canvas = tk.Canvas(self, width=320, height=320)
        self.canvas.pack()


    def update_avatar(self):
        self.canvas.delete(tk.ALL)
        
        layers_png = []
        for layer in AvatarLayer:
            scene_color = self.character_singleton.get_color(layer)  
            scene_img = self.character_singleton.get_image(layer)
            new_png = self.image_processor.process_image(scene_img, new_color=scene_color)
            layers_png.append(new_png)        
        
        overlay_image = self.image_processor.overlay_png_images(layers_png)
        self.result_image = ImageTk.PhotoImage(overlay_image)

        self.canvas.create_image(self.width, self.height, image=self.result_image)


    def change_color(self, image, replacement_color):
        image = image.convert("RGBA")
        data = image.getdata()

        new_data = []
        for item in data:
            if item[0] < 100 and item[0] < 100 and item[2] < 100 and item[3] > 0:
                new_color = (
                    replacement_color[0],
                    replacement_color[1],
                    replacement_color[2],
                    item[3]                    
                )

                new_data.append(new_color)
            else:
                new_data.append(item)

        image.putdata(new_data)
        return image
    
    
    def handle_character_changes(self):
        self.update_avatar()