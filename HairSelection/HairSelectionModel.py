import enum


class Hair(enum.Enum):
    bang_hair = 0
    medium_length_hair = 1
    short_hair = 2
    short_messy_hair = 3

    def get_image_path(self):
        match self:
            case Hair.bang_hair:
                return "Assets/Hair/bang hair.svg"
            case Hair.medium_length_hair:
                return "Assets/Hair/medium length hair.svg"
            case Hair.short_hair:
                return "Assets/Hair/short hair.svg"
            case Hair.short_messy_hair:
                return "Assets/Hair/short messy hair.svg"


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