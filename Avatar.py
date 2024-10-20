import enum


class Scene(enum.Enum):
    solid = 0
    stripes = 1

    def get_image_path(self):
        match self:
            case Scene.solid:
                return "Assets/Scene/square scene.svg"
            case Scene.stripes:
                return "Assets/Scene/stripes square scene.svg"


class Body(enum.Enum):
    triangle_body = 0
    wide_rectangle_body = 1

    def get_image_path(self):
        match self:
            case Body.triangle_body:
                return "Assets/Body/triangle body.svg"
            case Body.wide_rectangle_body:
                return "Assets/Body/wide rectangle body.svg"


class Head(enum.Enum):
    circle_head = 0
    square_head = 1
    wide_square_head = 2

    def get_image_path(self):
        match self:
            case Head.circle_head:
                return "Assets/Head/default circle head.svg"
            case Head.square_head:
                return "Assets/Head/default square head.svg"
            case Head.wide_square_head:
                return "Assets/Head/wide square head.svg"
            

class Mouth(enum.Enum):
    happy = 0
    sad = 1

    def get_image_path(self):
        match self:
            case Mouth.happy:
                return "Assets/Mouth/happy mouth.svg"
            case Mouth.sad:
                return "Assets/Mouth/sad mouth.svg"


class Eyes(enum.Enum):
    half_open = 0
    open = 1

    def get_image_path(self):
        match self:
            case Eyes.half_open:
                return "Assets/Eyes/default eyes half-open.svg"
            case Eyes.open:
                return "Assets/Eyes/default eyes open.svg"


class Hair(enum.Enum):
    bang_hair = 0
    medium_length_hair = 1
    short_hair = 2
    short_messy_hair = 3

    def get_image_path(self):
        match self:
            case Hair.bang_hair:
                return "Assets/Hair/bang hair.svg"
            case Hair.medium_length_hair:
                return "Assets/Hair/medium length hair.svg"
            case Hair.short_hair:
                return "Assets/Hair/short hair.svg"
            case Hair.short_messy_hair:
                return "Assets/Hair/short messy hair.svg"


class Avatar():
    def __init__(self):
        self.scene: Scene = Scene.solid
        self.body: Body = Scene.solid
        self.head: Head = Scene.solid
        self.eyes: Eyes = Scene.solid
        self.mouth: Mouth = Mouth.happy
        self.hair: Hair = Hair.short_messy_hair
      