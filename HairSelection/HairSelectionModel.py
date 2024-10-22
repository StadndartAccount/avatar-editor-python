from Avatar import HairFront, HairBack

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

        self.colors = [
            "#2D2623",
            "#7F6343",
            "#DDD39E",
            "#D2B065",
            "#C6812A",
            "#A75C19",
            "#90100A",
            "#E96E45",
            "#CA3528",
            "#A72111",
        ]
        
        self.selected_option = self.options[0]
        self.selected_color = self.colors[0]
