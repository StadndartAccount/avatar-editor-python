from Avatar import Scene
import Colors
from Options import scene_options
from CharacterSingleton import CharacterSingleton
from AvatarLayer import AvatarLayer

class SceneSelectionModel:
    def __init__(self):
        self.options: list[Scene] = scene_options
        self.colors = Colors.scene_colors


    def get_selected_option(self) -> Scene:
        for option in self.options:
            if CharacterSingleton().get_image(AvatarLayer.scene) == option.get_image_path():
                return option
            
    
    def get_selected_color(self) -> str:
        for color in self.colors:
            if CharacterSingleton().get_color(AvatarLayer.scene) == color:
                return color 