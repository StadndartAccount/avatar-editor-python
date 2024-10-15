import tkinter as tk
from Components.TabGroup import *
from BodySelection.BodySelectionFrame import *
from HairSelection.HairSelectionFrame import *
from FaceSelection.FaceCollectionFrame import *
from SceneSelection.SceneSelectionFrame import *
from Components.AvatarFrame import AvatarLayer

class OptionsSelectorMainFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        selector_frame = TabGroup(self, background="orange")
        selector_frame.pack(fill=tk.X)
        selector_frame.delegate = self

        scroll_frame = ScrollableFrame(self)
        scroll_frame.pack(fill=tk.BOTH, expand=True)

        tab_content_frame = tk.Frame(scroll_frame.scrollable_frame, background="gray", width=700)
        tab_content_frame.pack(fill=tk.BOTH, expand=True)

        body_options_frame = BodyCollection(tab_content_frame)
        body_options_frame.delegate = self

        hair_options_frame = HairCollection(tab_content_frame)
        hair_options_frame.delegate = self

        face_options_frame = FaceCollection(tab_content_frame)
        face_options_frame.delegate = self

        scene_options_frame = SceneCollection(tab_content_frame)
        scene_options_frame.delegate = self

        self.tabs = {
            AvatarLayer.body: body_options_frame,
            AvatarLayer.hair: hair_options_frame,
            AvatarLayer.eyes: face_options_frame,
            AvatarLayer.scene: scene_options_frame
        }

    def select_tab(self, selected_option):
        for option in self.tabs:
            if option == selected_option: continue
            self.tabs[option].pack_forget()
            
        self.tabs[selected_option].pack(fill=tk.BOTH, expand=True)

    def select_new_option(self, option, new_image):
        self.delegate.select_new_option(option, new_image)
    
    def select_new_color(self, option, new_color):
        self.delegate.select_new_color(option, new_color)
                
