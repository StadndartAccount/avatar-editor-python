import tkinter as tk
from tkinter import messagebox

from Components.HeaderFrame import *
from Components.AvatarFrame import *
from Components.OptionsSelectorMainFrame import *
from CharacterSingleton import *
from ImageProcessor import *
from datetime import datetime
import os
import platform
from DataProcessor import *
import Colors
import random
from Options import *

class Main:
    def __init__(self):
        self.character_singleton = CharacterSingleton()
        self.image_processor = ImageProcessor()

        root = tk.Tk()
        root.title("Avatar Creator")
        root.geometry("616x720")
        root.resizable(False, False)

        header_frame = HeaderFrame(root, bg="white")
        header_frame.pack(fill=tk.X)
        header_frame.delegate = self

        self.avatar_frame = AvatarFrame(root, bg="white")
        self.avatar_frame.pack(fill=tk.X)
        self.avatar_frame.configure(height=280) # temp

        self.options_selector_frame = OptionsSelectorMainFrame(root)
        self.options_selector_frame.pack(fill=tk.BOTH, expand=True)

        root.mainloop()


    def randomize_character(self):
        head_color = random.choice(Colors.head_colors)
        hair_color = random.choice(Colors.hair_colors)

        body_random_option = random.choice(body_options)
        hair_random_option = random.choice(hair_options)
        face_random_option = random.choice(face_options)
        scene_random_option = random.choice(scene_options)


        for layer in AvatarLayer:
            match layer:
                case AvatarLayer.scene:
                    self.character_singleton.set_color(layer, random.choice(Colors.scene_colors))
                    self.character_singleton.set_image(layer, scene_random_option.get_image_path())
                case AvatarLayer.back_hair: 
                    self.character_singleton.set_color(layer, hair_color)
                    self.character_singleton.set_image(layer, hair_random_option.back.get_image_path())
                case AvatarLayer.body: 
                    self.character_singleton.set_color(layer, random.choice(Colors.clothes_colors))
                    self.character_singleton.set_image(layer, body_random_option.clothes.get_image_path())
                case AvatarLayer.head: 
                    self.character_singleton.set_color(layer, head_color)
                    self.character_singleton.set_image(layer, body_random_option.head.get_image_path())
                case AvatarLayer.eyes: 
                    self.character_singleton.set_color(layer, random.choice(Colors.eyes_colors))
                    self.character_singleton.set_image(layer, face_random_option.eyes.get_image_path())
                case AvatarLayer.mouth: 
                    rgb_color = ImageColor.getrgb(head_color)
                    mouth_color = (rgb_color[0] - 30, rgb_color[1] - 30, rgb_color[2] - 30, 255)
                    self.character_singleton.set_color(AvatarLayer.mouth, rgb2hex(mouth_color))  
                    self.character_singleton.set_image(layer, face_random_option.mouth.get_image_path())
                case AvatarLayer.front_hair: 
                    self.character_singleton.set_color(layer, hair_color)
                    self.character_singleton.set_image(layer, hair_random_option.front.get_image_path())
        
        self.options_selector_frame.update_content()


    def add_to_history(self):
        save_object({
            AvatarLayer.scene.name : self.character_singleton.get_layer_info(AvatarLayer.scene).__dict__,
            AvatarLayer.back_hair.name: self.character_singleton.get_layer_info(AvatarLayer.back_hair).__dict__,
            AvatarLayer.body.name: self.character_singleton.get_layer_info(AvatarLayer.body).__dict__,
            AvatarLayer.head.name: self.character_singleton.get_layer_info(AvatarLayer.head).__dict__,
            AvatarLayer.eyes.name: self.character_singleton.get_layer_info(AvatarLayer.eyes).__dict__,
            AvatarLayer.mouth.name: self.character_singleton.get_layer_info(AvatarLayer.mouth).__dict__,
            AvatarLayer.front_hair.name: self.character_singleton.get_layer_info(AvatarLayer.front_hair).__dict__,
        })


    def export(self):
        png_layers = list(map(lambda layer: self.character_singleton.get_layer_as_png(layer), AvatarLayer))
        final_image = self.image_processor.overlay_png_images(png_layers)

        now = datetime.now()
        file_name = f"{now.strftime("%d-%m-%Y %H:%M:%S")}.png"
        
        current_directory = os.path.dirname(os.path.abspath(__file__))
        directory_name = 'Exports'
        export_directory_path = os.path.join(current_directory, directory_name)

        file_path = os.path.join(export_directory_path, file_name)

        os.makedirs(export_directory_path, exist_ok=True)
        final_image.save(file_path)

        self.show_export_alert(export_directory_path, file_name)


    def show_export_alert(self, directory, file_name):
        def open_folder():
            match platform.system():
                case "Windows": os.startfile(directory)
                case "Darwin": os.system(f'open "{directory}"')
                case _: os.system(f'xdg-open "{directory}"')

        response = messagebox.askyesno(message=f"Изображение экспортировано.\nХотите открыть папку?")
        if response: open_folder()


Main()