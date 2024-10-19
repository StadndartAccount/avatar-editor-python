import enum


class Body(enum.Enum):
    triangle_body = 0
    wide_rectangle_body = 1

    def get_image_path(self):
        match self:
            case Body.triangle_body:
                return "Assets/Body/triangle body.svg"
            case Body.wide_rectangle_body:
                return "Assets/Body/wide rectangle body.svg"


class Head(enum.Enum):
    circle_head = 0
    square_head = 1
    wide_square_head = 2

    def get_image_path(self):
        match self:
            case Head.circle_head:
                return "Assets/Head/default circle head.svg"
            case Head.square_head:
                return "Assets/Head/default square head.svg"
            case Head.wide_square_head:
                return "Assets/Head/wide square head.svg"
            

class BodySelectionModel:
    def __init__(self):
        
        self.selected_option_index = 0
        self.selected_body_color_index = 0
        self.selected_head_color_index = 0

        self.body_head_combinations: list[tuple[Body, Head]] = [
            (Body.triangle_body, Head.circle_head),
            (Body.triangle_body, Head.square_head),
            (Body.wide_rectangle_body, Head.wide_square_head),            
        ]
        
        self.body_colors = [
            "#F25764",
            "#4183D9",
            "#F2C744",
            "#F27052",
            "#F2F2F2",
            "#8773A5",
            "#181828",
            "#0B4048",
            "#C9D9C3",
            "#F4ECE0",
        ]        

        self.head_colors = [
            "#F2AF88",
            "#D98E73",
            "#8C4A3B",
            "#A65746",
            "#BF5F56",
            "#FBDDCE",
            "#F5D3BF",
            "#E2B29E",
            "#F6D6C3",
            "#ECA894",
        ]