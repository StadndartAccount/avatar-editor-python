import os

class FaceSelectionModel:
    def __init__(self):
        self.images = list(filter(lambda file_name: file_name.split(".")[-1] == "png", os.listdir("Assets/Face")))
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