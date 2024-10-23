from Avatar import Eyes, Mouth
import os 
from AvatarLayer import AvatarLayer, Layer
from DataProcessor import *

class HisotryItem:
    def __init__(self, id, data):
        self.id = id
        self.layers: dict[AvatarLayer, Layer] = self.map_dictionary_to_object(data)

    def map_dictionary_to_object(self, data: dict[str, dict[str, str]]) -> dict[AvatarLayer, Layer]:
        new_dictionary: dict[AvatarLayer, Layer] = {}
        
        for layer_name, params in data.items():
            layer = AvatarLayer.__getitem__(layer_name)
            layer_params = Layer(params["image_path"], params["color"])

            new_dictionary[layer] = layer_params

        return new_dictionary


class HistorySelectionModel:
    def __init__(self):
        self.update_options()
        

    def update_options(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        history_directory_path = os.path.join(current_directory, "../History")

        files = os.listdir(history_directory_path)
        files_without_extension = list(map(lambda file: os.path.splitext(file)[0], files))
        
        self.options: list[HisotryItem] = list(map(lambda id: HisotryItem(id, load_object(id)), files_without_extension))
