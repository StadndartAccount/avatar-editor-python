from Avatar import Scene

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