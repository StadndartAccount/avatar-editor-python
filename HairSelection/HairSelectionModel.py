from Avatar import Hair


class HairSelectionModel:
    def __init__(self):
        self.selected_option_index = 0

        self.options: list[Hair] = [
            Hair.bang_hair,
            Hair.medium_length_hair,
            Hair.short_hair,
            Hair.short_messy_hair,
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