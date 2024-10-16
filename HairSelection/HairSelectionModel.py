import os

class HairSelectionModel:
    def __init__(self):
        self.images = []
        self.colors = [
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