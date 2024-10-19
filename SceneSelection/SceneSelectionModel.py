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


class SceneSelectionModel:
    def __init__(self):
        self.selected_option_index = 0

        self.options: list[Scene] = [
            Scene.solid,
            Scene.stripes,
        ]

        self.colors = [
            "#0C99BF",
            "#33B59B",
            "#DB4F50",
            "#E27F57",
            "#7966D9",
        ]