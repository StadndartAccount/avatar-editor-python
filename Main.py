import tkinter as tk
from Components.HeaderFrame import *
from Components.AvatarFrame import *
from Components.OptionsSelectorMainFrame import *
from EditorModel import *
import os
from Components.AvatarFrame import AvatarLayer

class Main:
    def __init__(self):
        root = tk.Tk()
        root.title("Avatar Creator")
        root.geometry("560x720")
        root.resizable(False, False)

        header_frame = HeaderFrame(root, background="white")
        header_frame.pack(fill=tk.X)
        header_frame.delegate = self

        self.avatar_frame = AvatarFrame(root)
        self.avatar_frame.pack(fill=tk.X)
        self.avatar_frame.configure(height=280) # temp

        options_selector_frame = OptionsSelectorMainFrame(root, background="white")
        options_selector_frame.pack(fill=tk.BOTH, expand=True)
        options_selector_frame.delegate = self

        self.setup_initial_avatar()

        root.mainloop()


    def export(self):
        self.model.export_avatar()


    def setup_initial_avatar(self):
        self.update_scene("scene.png")
        self.update_body("body.png")
        self.update_face("face.png")
        self.update_hair("hair.png")


    def update_scene(self, new_value):
        image_path = f"Assets/Scene/{new_value}"
        self.avatar_frame.set_new_option_value(AvatarLayer.scene, image_path)
        

    def update_body(self, new_value):
        image_path = f"Assets/Body/{new_value}"
        self.avatar_frame.set_new_option_value(AvatarLayer.body, image_path)


    def update_face(self, new_value):
        image_path = f"Assets/Face/{new_value}"
        self.avatar_frame.set_new_option_value(AvatarLayer.mouth, image_path)


    def update_hair(self, new_value):
        image_path = f"Assets/Hair/{new_value}"
        self.avatar_frame.set_new_option_value(AvatarLayer.hair, image_path)


    def select_new_option(self, option, new_image):
        match option:
            case AvatarLayer.scene:
                self.update_scene(new_image)
            case AvatarLayer.body:
                self.update_body(new_image)
            case AvatarLayer.hair:
                self.update_hair(new_image)
            case AvatarLayer.face:
                self.update_face(new_image)


    def select_new_color(self, option, new_color):
        self.avatar_frame.update_option_color(option, new_color)


Main()