from Avatar import Head, Clothes
import Colors
from Options import Body, body_options
from CharacterSingleton import *

class BodySelectionModel:
    def __init__(self):
        self.options: list[Body] = body_options
        
        self.clothes_colors = Colors.clothes_colors        
        self.head_colors = Colors.head_colors


    def get_selected_option(self) -> Body:
        for option in self.options:
            if (
                CharacterSingleton().get_image(AvatarLayer.body) == option.clothes.get_image_path() and
                CharacterSingleton().get_image(AvatarLayer.head) == option.head.get_image_path()
            ):
                return option
            
    
    def get_selected_clothes_color(self) -> str:
        for color in self.clothes_colors:
            if CharacterSingleton().get_color(AvatarLayer.body) == color:
                return color   
                
    
    def get_selected_head_color(self) -> str:
        for color in self.head_colors:
            if CharacterSingleton().get_color(AvatarLayer.head) == color:
                return color
            
            