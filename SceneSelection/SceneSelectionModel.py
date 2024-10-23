from Avatar import Scene
import Colors

class SceneSelectionModel:
    def __init__(self):
        self.options: list[Scene] = [
            Scene.solid,
            Scene.stripes,
            Scene.circles,
            Scene.paw,
            Scene.paws,
        ]

        self.colors = Colors.scene_colors

        self.selected_option = self.options[0]
        self.selected_color = self.colors[0]