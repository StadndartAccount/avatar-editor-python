from AvatarLayer import *
from ImageProcessor import *

class CharacterSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CharacterSingleton, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance
    
    def initialize(self):
        self.image_processor = ImageProcessor()

        self.colors = {
            AvatarLayer.scene: "black",
            AvatarLayer.body: "orange",
            AvatarLayer.head: "gray",
            AvatarLayer.eyes: "blue",
            AvatarLayer.mouth: "red",
            AvatarLayer.hair: "brown",
        }

        self.layers = {
            AvatarLayer.scene: "Assets/Scene/square scene.svg",
            AvatarLayer.body: "Assets/Body/triangle body.svg",
            AvatarLayer.head: "Assets/Head/default square head.svg",
            AvatarLayer.eyes: "Assets/Eyes/default eyes open.svg",
            AvatarLayer.mouth: "Assets/Mouth/happy mouth.svg",
            AvatarLayer.hair: "Assets/Hair/medium length hair.svg",
        }

    def set_color(self, layer: AvatarLayer, new_color: str):
        self.colors[layer] = new_color

    def get_color(self, layer: AvatarLayer) -> str:
        return self.colors[layer]

    def set_image(self, layer: AvatarLayer, new_image: str):
        self.layers[layer] = new_image

    def get_image(self, layer: AvatarLayer) -> str:
        return self.layers[layer]
    
    def get_layer_as_png(self, layer: AvatarLayer):
        color = self.colors[layer]
        image_path = self.layers[layer]

        return self.image_processor.process_image(image_path, new_color=color)