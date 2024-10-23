import enum

class AvatarLayer(enum.Enum):
    scene = 0
    back_hair = 1
    body = 2
    head = 3
    eyes = 4
    mouth = 5
    front_hair = 6


class Layer:
    def __init__(self, image_path: str, color: str):
        self.image_path = image_path
        self.color = color