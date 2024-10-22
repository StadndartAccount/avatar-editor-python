from Avatar import Scene

class SceneSelectionModel:
    def __init__(self):
        self.options: list[Scene] = [
            Scene.solid,
            Scene.stripes,
            Scene.circles,
            Scene.paw,
            Scene.paws,
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