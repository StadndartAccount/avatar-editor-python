from Avatar import Eyes, Mouth

class Face:
    def __init__(self, mouth: Mouth, eyes: Eyes):
        self.mouth: Mouth = mouth
        self.eyes: Eyes = eyes

class FaceSelectionModel:
    def __init__(self):
        self.options: list[Face] = [
            Face(Mouth.happy, Eyes.open),
            Face(Mouth.sad, Eyes.open),
            Face(Mouth.happy, Eyes.half_open),
            Face(Mouth.sad, Eyes.half_open),
        ]

        self.colors = [
            "#0C99BF",
            "#33B59B",
            "#DB4F50",
            "#E27F57",
            "#7966D9",
        ]

        self.selected_option = self.options[0]
        self.selected_color = self.colors[0]