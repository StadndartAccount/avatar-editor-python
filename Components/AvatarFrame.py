import tkinter as tk
from PIL import ImageTk, Image, ImagePalette
import enum
import random

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

        self.colors = {
            AvatarLayer.scene: (0,0,0,0),
            AvatarLayer.body: (0,0,0,0),
            AvatarLayer.head: (0,0,0,0),
            AvatarLayer.eyes: (0,0,0,0),
            AvatarLayer.mouth: (0,0,0,0),
            AvatarLayer.hair: (0,0,0,0),
        }

        self.layers = {
            AvatarLayer.scene: "Assets/Scene/scene.png",
            AvatarLayer.body: "Assets/Body/body.png",
            AvatarLayer.head: "Assets/Body/face.png",
            AvatarLayer.eyes: "Assets/Face/face.png",
            AvatarLayer.mouth: "Assets/Face/face.png",
            AvatarLayer.hair: "Assets/Hair/hair.png",
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

        scene_color = self.colors[AvatarLayer.scene]  
        scene_img = Image.open(self.layers[AvatarLayer.scene])
        self.scene_image = ImageTk.PhotoImage(self.change_color(scene_img, scene_color))
        self.canvas.create_image(self.width, self.height, image=self.scene_image)

        body_color = self.colors[AvatarLayer.body]  
        body_img = Image.open(self.layers[AvatarLayer.body])
        self.body_image = ImageTk.PhotoImage(self.change_color(body_img, body_color))
        self.canvas.create_image(self.width, self.height, image=self.body_image)

        face_color = self.colors[AvatarLayer.eyes]  
        face_img = Image.open(self.layers[AvatarLayer.eyes])
        self.face_image = ImageTk.PhotoImage(self.change_color(face_img, face_color))
        self.canvas.create_image(self.width, self.height, image=self.face_image)

        hair_color = self.colors[AvatarLayer.hair]  
        hair_img = Image.open(self.layers[AvatarLayer.hair])
        self.hair_image = ImageTk.PhotoImage(self.change_color(hair_img, hair_color))
        self.canvas.create_image(self.width, self.height, image=self.hair_image)


    def change_color(self, image, replacement_color):
        image = image.convert("RGBA")
        data = image.getdata()

        new_data = []
        for item in data:
            if item[3] > 0:
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