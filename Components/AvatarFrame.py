import tkinter as tk
from PIL import ImageTk, Image, ImagePalette
import enum
import random
from ImageProcessor import *

class AvatarLayer(enum.Enum):
    scene = 1
    body = 2
    head = 3
    eyes = 4
    mouth = 5
    hair = 6

class AvatarFrame(tk.Frame):
    def __init__(self, master = None, *args, **kvargs):
        super().__init__(master, *args, **kvargs)

        self.image_processor = ImageProcessor()

        self.colors = {
            AvatarLayer.scene: (0,0,0,0),
            AvatarLayer.body: (0,0,0,0),
            AvatarLayer.head: (0,0,0,0),
            AvatarLayer.eyes: (0,0,0,0),
            AvatarLayer.mouth: (0,0,0,0),
            AvatarLayer.hair: (0,0,0,0),
        }

        self.layers = {
            AvatarLayer.scene: "Assets/Scene/circle scene.png",
            AvatarLayer.body: "Assets/Body/triangle body.png",
            AvatarLayer.head: "Assets/Head/default square head.png",
            AvatarLayer.eyes: "Assets/Eyes/default eyes open.png",
            AvatarLayer.mouth: "Assets/Mouth/happy mouth.png",
            AvatarLayer.hair: "Assets/Hair/medium length hair.png",
        }

        self.width = 162
        self.height = 162

        self.canvas = tk.Canvas(self, width=320, height=320)
        self.canvas.pack()


    def set_new_option_value(self, option, new_image_path):
        self.layers[option] = new_image_path
        self.update_avatar()


    def update_option_color(self, option, new_color):
        self.colors[option] = new_color
        self.update_avatar()


    def update_avatar(self):
        self.canvas.delete(tk.ALL)

        self.image_references = []
        
        layers_png = []

        for layer in AvatarLayer:
            scene_color = self.colors[layer]  
            scene_img = Image.open(self.layers[layer])
            new_png = self.change_color(scene_img, scene_color)
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