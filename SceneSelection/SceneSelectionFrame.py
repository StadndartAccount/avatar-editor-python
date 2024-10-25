import tkinter as tk
from Components.ScrollableFrame import *
from PIL import ImageTk
from SceneSelection.SceneSelectionModel import *
from AvatarLayer import *
from Components.PaletteFrame import *
from ImageProcessor import *
from CharacterSingleton import *
from Tools import split_into_chunks

class ScenePaletteDelegate:
    def handle_clicked_color(self, new_color):
        self.delegate.select_new_color(option=AvatarLayer.scene, new_color=new_color)


class SceneCollection(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.character_singleton = CharacterSingleton()
        
        self.model = SceneSelectionModel()
        self.image_processor = ImageProcessor()

        self.scene_palette_delegate = ScenePaletteDelegate()
        self.scene_palette_delegate.delegate = self
        
        self.item_selected(self.model.options[0])
        self.select_new_color(AvatarLayer.scene, self.model.colors[0])


    def update_content(self): 
        for widget in self.winfo_children():
            widget.destroy()

        self.content_frame = tk.Frame(self)
        self.content_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        palette_container_frame = tk.Frame(self)
        palette_container_frame.pack(fill=tk.X, expand=False, side=tk.LEFT, anchor=tk.N)

        scene_color_label = tk.Label(palette_container_frame, text="Scene")
        scene_color_label.pack(fill=tk.X, expand=False)

        scene_palette_frame = PaletteFrame(palette_container_frame, colors=self.model.colors, selected_color=self.model.get_selected_color(), columns_number=3)
        scene_palette_frame.pack(fill=tk.X, expand=False)
        scene_palette_frame.delegate = self.scene_palette_delegate

        columns_number = 3
        cell_side = 132
        border_width = 2
        margin = 4

        rows = split_into_chunks(self.model.options, columns_number)

        for row in rows:
            row_frame = tk.Frame(self.content_frame)
            row_frame.pack(fill=tk.X, expand=True, side=tk.TOP)

            for option in row:
                scene_image = self.image_processor.process_image(option.get_image_path(), self.character_singleton.get_color(AvatarLayer.scene)).resize((cell_side, cell_side))
                photo = ImageTk.PhotoImage(scene_image)
                
                if option == self.model.get_selected_option():
                    item_border = tk.Frame(row_frame, bg="black")
                    item_frame = tk.Button(item_border, image=photo, height=cell_side - border_width*2, width=cell_side - border_width*2)
                    item_frame.image = photo
                    item_border.pack(padx=margin, pady=margin, side=tk.LEFT)
                    item_frame.pack(padx=border_width, pady=border_width)
                else:
                    item_frame = tk.Button(row_frame, image=photo, height=cell_side, width=cell_side, command=lambda scene=option: self.item_selected(scene))
                    item_frame.image = photo
                    item_frame.pack(padx=margin, pady=margin, side=tk.LEFT)


    def item_selected(self, scene: Scene):
        self.model.selected_option = scene
        self.character_singleton.set_image(AvatarLayer.scene, scene.get_image_path())
        self.update_content()


    def select_new_color(self, option, new_color):
        self.model.selected_color = new_color
        self.character_singleton.set_color(option, new_color)        
        self.update_content()