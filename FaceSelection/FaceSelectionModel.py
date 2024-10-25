from Avatar import Eyes, Mouth
import Colors
from Options import Face, face_options
from CharacterSingleton import CharacterSingleton
from AvatarLayer import AvatarLayer

class FaceSelectionModel:
    def __init__(self):
        self.options: list[Face] = face_options
        self.colors = Colors.eyes_colors


    def get_selected_option(self) -> Face:
        for option in self.options:
            if (
                CharacterSingleton().get_image(AvatarLayer.eyes) == option.eyes.get_image_path() and
                CharacterSingleton().get_image(AvatarLayer.mouth) == option.mouth.get_image_path()
            ):
                return option
            
    
    def get_selected_color(self) -> str:
        for color in self.colors:
            if CharacterSingleton().get_color(AvatarLayer.eyes) == color:
                return color   