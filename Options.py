from Avatar import *

class Body:
    def __init__(self, clothes: Clothes, head: Head):
        self.clothes: Clothes = clothes
        self.head: Head = head


class Face:
    def __init__(self, mouth: Mouth, eyes: Eyes):
        self.mouth: Mouth = mouth
        self.eyes: Eyes = eyes


class Hair:
    def __init__(self, front: HairFront, back: HairBack):
        self.front = front
        self.back = back


body_options: list[Body] = [
    Body(Clothes.slim_body_3, Head.square_head),
    Body(Clothes.slim_body_1, Head.square_head),
    Body(Clothes.slim_body_2, Head.square_head),
    Body(Clothes.wide_body_1, Head.wide_square_head),            
    Body(Clothes.wide_body_2, Head.wide_square_head),            
    Body(Clothes.wide_body_3, Head.square_head),
]

face_options: list[Face] = [
    Face(Mouth.happy, Eyes.open),
    Face(Mouth.sad, Eyes.open),
    Face(Mouth.happy, Eyes.half_open),
    Face(Mouth.sad, Eyes.half_open),
]

hair_options: list[Hair] = [
    Hair(HairFront.hair_7, HairBack.none),
    Hair(HairFront.hair_2, HairBack.hair_1),
    Hair(HairFront.hair_2, HairBack.hair_2),
    Hair(HairFront.hair_2, HairBack.hair_3),
    Hair(HairFront.hair_3, HairBack.hair_1),
    Hair(HairFront.hair_3, HairBack.hair_2),
    Hair(HairFront.hair_4, HairBack.hair_1),
    Hair(HairFront.hair_4, HairBack.hair_2),
    Hair(HairFront.hair_4, HairBack.hair_3),
    Hair(HairFront.hair_5, HairBack.none),
    Hair(HairFront.hair_6, HairBack.none),
    Hair(HairFront.none, HairBack.none),
]

scene_options: list[Scene] = [
    Scene.solid,
    Scene.stripes,
    Scene.circles,
    Scene.paw,
    Scene.paws,
]
