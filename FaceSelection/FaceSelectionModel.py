import enum


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


class Face:
    def __init__(self, mouth: Mouth, eyes: Eyes):
        self.mouth: Mouth = mouth
        self.eyes: Eyes = eyes

class FaceSelectionModel:
    def __init__(self):
        self.selected_option_index = 0

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