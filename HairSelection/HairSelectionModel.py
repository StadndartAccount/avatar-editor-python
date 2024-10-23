from Avatar import HairFront, HairBack
import Colors


class HairContainer:
    def __init__(self, front: HairFront, back: HairBack):
        self.front = front
        self.back = back


class HairSelectionModel:
    def __init__(self):

        self.options: list[HairContainer] = [
            HairContainer(HairFront.hair_7, HairBack.none),
            HairContainer(HairFront.hair_2, HairBack.hair_1),
            HairContainer(HairFront.hair_2, HairBack.hair_2),
            HairContainer(HairFront.hair_2, HairBack.hair_3),
            HairContainer(HairFront.hair_3, HairBack.hair_1),
            HairContainer(HairFront.hair_3, HairBack.hair_2),
            HairContainer(HairFront.hair_4, HairBack.hair_1),
            HairContainer(HairFront.hair_4, HairBack.hair_2),
            HairContainer(HairFront.hair_4, HairBack.hair_3),
            HairContainer(HairFront.hair_5, HairBack.none),
            HairContainer(HairFront.hair_6, HairBack.none),
            HairContainer(HairFront.none, HairBack.none),
        ]

        self.colors = Colors.hair_colors
        
        self.selected_option = self.options[0]
        self.selected_color = self.colors[0]
