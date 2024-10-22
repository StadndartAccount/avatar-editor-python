import enum


class Scene(enum.Enum):
    solid = 0
    stripes = 1
    circles = 2
    paw = 3
    paws = 4

    def get_image_path(self):
        match self:
            case Scene.solid: return "Assets/Scene/square scene.svg"
            case Scene.stripes: return "Assets/Scene/stripes square scene.svg"
            case Scene.circles: return "Assets/Scene/circles scene.svg"
            case Scene.paw: return "Assets/Scene/paw.svg"
            case Scene.paws: return "Assets/Scene/paws.svg"


class Body(enum.Enum):
    slim_body_1 = 0
    slim_body_2 = 1
    slim_body_3 = 2
    wide_body_1 = 3
    wide_body_2 = 4
    wide_body_3 = 5

    def get_image_path(self):
        match self:
            case Body.slim_body_1: return "Assets/Body/slim body 1.svg"
            case Body.slim_body_2: return "Assets/Body/slim body 2.svg"
            case Body.slim_body_3: return "Assets/Body/slim body 3.svg"
            case Body.wide_body_1: return "Assets/Body/wide body 1.svg"
            case Body.wide_body_2: return "Assets/Body/wide body 2.svg"
            case Body.wide_body_3: return "Assets/Body/wide body 3.svg"


class Head(enum.Enum):
    square_head = 0
    wide_square_head = 1

    def get_image_path(self):
        match self:
            case Head.square_head: return "Assets/Head/square head.svg"
            case Head.wide_square_head: return "Assets/Head/wide square head.svg"
            

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


class HairFront(enum.Enum):
    none = 0
    hair_1 = 1
    hair_2 = 2
    hair_3 = 3
    hair_4 = 4
    hair_5 = 5
    hair_6 = 6
    hair_7 = 7

    def get_image_path(self):
        match self:
            case HairFront.none: return "Assets/Hair/none.svg"
            case HairFront.hair_1: return "Assets/Hair/Front/front hair 1.svg"
            case HairFront.hair_2: return "Assets/Hair/Front/front hair 2.svg"
            case HairFront.hair_3: return "Assets/Hair/Front/front hair 3.svg"
            case HairFront.hair_4: return "Assets/Hair/Front/front hair 4.svg"
            case HairFront.hair_5: return "Assets/Hair/Front/front hair 5.svg"
            case HairFront.hair_6: return "Assets/Hair/Front/front hair 6.svg"
            case HairFront.hair_7: return "Assets/Hair/Front/front hair 7.svg"
            

class HairBack(enum.Enum):
    none = 0
    hair_1 = 1
    hair_2 = 2
    hair_3 = 3

    def get_image_path(self):
        match self:
            case HairBack.none: return "Assets/Hair/none.svg"
            case HairBack.hair_1: return "Assets/Hair/Back/back hair 1.svg"
            case HairBack.hair_2: return "Assets/Hair/Back/back hair 2.svg"
            case HairBack.hair_3: return "Assets/Hair/Back/back hair 3.svg"
