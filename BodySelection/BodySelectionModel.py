import os
import enum


class Body(enum.Enum):
    triangle_body = 0
    wide_rectangle_body = 1

    def get_image_path(self):
        match self:
            case Body.triangle_body:
                return "Assets/Body/triangle body.png"
            case Body.wide_rectangle_body:
                return "Assets/Body/wide rectangle body.png"


class Head(enum.Enum):
    circle_head = 0
    square_head = 1
    wide_square_head = 2

    def get_image_path(self):
        match self:
            case Head.circle_head:
                return "Assets/Head/default circle head.png"
            case Head.square_head:
                return "Assets/Head/default square head.png"
            case Head.wide_square_head:
                return "Assets/Head/wide square head.png"
            

class BodySelectionModel:
    def __init__(self):
        
        self.body_head_combinations: list[tuple[Body, Head]] = [
            (Body.triangle_body, Head.circle_head),
            (Body.triangle_body, Head.square_head),
            (Body.wide_rectangle_body, Head.wide_square_head),            
        ]
        
        self.body_colors = [
            (255, 0, 0, 255), 
            (128, 0, 0, 255), 
            (255, 255, 0, 255),
            (128, 128, 0, 255), 
            (255, 255, 255, 255), 
            (128, 128, 128, 255), 
            (255, 128, 0, 255), 
            (0, 128, 128, 255), 
            (255, 0, 128, 255),
        ]        

        self.head_colors = [
            (255, 0, 0, 255), 
            (128, 0, 0, 255), 
            (255, 255, 0, 255),
            (128, 128, 0, 255), 
            (255, 255, 255, 255), 
            (128, 128, 128, 255), 
            (255, 128, 0, 255), 
            (0, 128, 128, 255), 
            (255, 0, 128, 255),
        ]