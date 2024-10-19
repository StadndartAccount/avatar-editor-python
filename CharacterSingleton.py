from AvatarLayer import *
from PIL import ImageColor
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
            AvatarLayer.scene: ImageColor.getrgb("gray"),
            AvatarLayer.body: ImageColor.getrgb("gray"),
            AvatarLayer.head: ImageColor.getrgb("gray"),
            AvatarLayer.eyes: ImageColor.getrgb("gray"),
            AvatarLayer.mouth: ImageColor.getrgb("gray"),
            AvatarLayer.hair: ImageColor.getrgb("gray"),
        }

        self.images = {
            AvatarLayer.scene: "Assets/Scene/circle scene.png",
            AvatarLayer.body: "Assets/Body/triangle body.png",
            AvatarLayer.head: "Assets/Head/default square head.png",
            AvatarLayer.eyes: "Assets/Eyes/default eyes open.png",
            AvatarLayer.mouth: "Assets/Mouth/happy mouth.png",
            AvatarLayer.hair: "Assets/Hair/medium length hair.png",
        }

    def set_color(self, layer: AvatarLayer, new_color: str):
        self.colors[layer] = new_color

    def get_color(self, layer: AvatarLayer) -> str:
        return self.colors[layer]

    def set_image(self, layer: AvatarLayer, new_image: str):
        self.images[layer] = new_image

    def get_image(self, layer: AvatarLayer) -> str:
        return self.images[layer]
    
    def get_layer_as_png(self, layer: AvatarLayer):
        color = self.colors[layer]
        image = self.images[layer]