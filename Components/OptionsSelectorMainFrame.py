import tkinter as tk
from Components.TabGroup import *
from BodySelection.BodySelectionFrame import *
from HairSelection.HairSelectionFrame import *
from FaceSelection.FaceCollectionFrame import *
from SceneSelection.SceneSelectionFrame import *
from HistorySelection.HistoryCollectionFrame import *
from Tab import *

class OptionsSelectorMainFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.selected_tab = Tab.body

        self.tab_container_frame = tk.Frame(self)
        self.tab_container_frame.pack(fill=tk.X)

        scroll_frame = ScrollableFrame(self)
        scroll_frame.pack(fill=tk.BOTH, expand=True)

        tab_content_frame = tk.Frame(scroll_frame.scrollable_frame)
        tab_content_frame.pack(fill=tk.BOTH, expand=True)

        self.body_options_frame = BodyCollection(tab_content_frame)
        self.hair_options_frame = HairCollection(tab_content_frame)
        self.face_options_frame = FaceCollection(tab_content_frame)
        self.scene_options_frame = SceneCollection(tab_content_frame)
        self.history_frame = HistoryCollection(tab_content_frame)

        self.tabs = {
            Tab.body: self.body_options_frame,
            Tab.hair: self.hair_options_frame,
            Tab.face: self.face_options_frame,
            Tab.scene: self.scene_options_frame,
            Tab.history: self.history_frame,
        }

        self.select_tab(Tab.body)
        self.update_tabs()


    def select_tab(self, selected_option):
        self.selected_tab = selected_option
        self.update_tabs()
        
        for option in self.tabs:
            if option == selected_option: continue
            self.tabs[option].pack_forget()
            
        self.tabs[selected_option].pack(fill=tk.BOTH, expand=True)
        self.tabs[selected_option].update_content()
                

    def update_tabs(self):
        for widget in self.tab_container_frame.winfo_children():
            widget.destroy()

        selector_frame = TabGroup(self.tab_container_frame, selected_tab=self.selected_tab, bg="white")
        selector_frame.pack(fill=tk.X)
        selector_frame.delegate = self


    def update_content(self):
        self.tabs[self.selected_tab].update_content()