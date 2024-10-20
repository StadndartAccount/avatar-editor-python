from AvatarLayer import *
from ImageProcessor import *
from Avatar import *


class CharacterSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CharacterSingleton, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance
    
    
    def initialize(self):
        self.image_processor = ImageProcessor()

        self.event_observers = []

        self.colors = {
            AvatarLayer.scene: "black",
            AvatarLayer.body: "black",
            AvatarLayer.head: "black",
            AvatarLayer.eyes: "black",
            AvatarLayer.mouth: "black",
            AvatarLayer.hair: "black",
        }

        self.layers = {
            AvatarLayer.scene: Scene.solid.get_image_path(),
            AvatarLayer.body: Body.triangle_body.get_image_path(),
            AvatarLayer.head: Head.square_head.get_image_path(),
            AvatarLayer.eyes: Eyes.open.get_image_path(),
            AvatarLayer.mouth: Mouth.happy.get_image_path(),
            AvatarLayer.hair: Hair.short_messy_hair.get_image_path(),
        }


    def set_color(self, layer: AvatarLayer, new_color: str):
        self.colors[layer] = new_color
        self.notify_observers()


    def get_color(self, layer: AvatarLayer) -> str:
        return self.colors[layer]
    

    def set_image(self, layer: AvatarLayer, new_image: str):
        self.layers[layer] = new_image
        self.notify_observers()


    def get_image(self, layer: AvatarLayer) -> str:
        return self.layers[layer]
    

    def get_layer_as_png(self, layer: AvatarLayer):
        color = self.colors[layer]
        image_path = self.layers[layer]

        return self.image_processor.process_image(image_path, new_color=color)
    

    def add_observer(self, new_observer):
        self.event_observers.append(new_observer)


    def notify_observers(self):
        for observer in self.event_observers:
            observer.handle_character_changes()