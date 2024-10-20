from Avatar import Hair


class HairSelectionModel:
    def __init__(self):

        self.options: list[Hair] = [
            Hair.short_messy_hair,
            Hair.bang_hair,
            Hair.medium_length_hair,
            Hair.short_hair,
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
