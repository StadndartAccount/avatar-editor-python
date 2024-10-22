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


class Main:
    def __init__(self):
        self.character_singleton = CharacterSingleton()
        self.image_processor = ImageProcessor()

        root = tk.Tk()
        root.title("Avatar Creator")
        root.geometry("584x720")
        root.resizable(False, False)

        header_frame = HeaderFrame(root, bg="white")
        header_frame.pack(fill=tk.X)
        header_frame.delegate = self

        self.avatar_frame = AvatarFrame(root, bg="white")
        self.avatar_frame.pack(fill=tk.X)
        self.avatar_frame.configure(height=280) # temp

        options_selector_frame = OptionsSelectorMainFrame(root)
        options_selector_frame.pack(fill=tk.BOTH, expand=True)

        root.mainloop()


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