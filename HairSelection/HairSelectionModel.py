from Avatar import HairFront, HairBack
import Colors
from Options import Hair, hair_options
from CharacterSingleton import CharacterSingleton
from AvatarLayer import AvatarLayer

class HairSelectionModel:
    def __init__(self):
        self.options: list[Hair] = hair_options
        self.colors = Colors.hair_colors


    def get_selected_option(self) -> Hair:
        for option in self.options:
            if (
                CharacterSingleton().get_image(AvatarLayer.front_hair) == option.front.get_image_path() and
                CharacterSingleton().get_image(AvatarLayer.back_hair) == option.back.get_image_path()
            ):
                return option
            
    
    def get_selected_color(self) -> str:
        for color in self.colors:
            if CharacterSingleton().get_color(AvatarLayer.front_hair) == color:
                return color   