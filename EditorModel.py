from Components.TabGroup import *
from Components.AvatarFrame import *

class EditorModel():
    def __init__(self):
        self.avatar_properties = {
            AvatarLayer.body: "",
            AvatarLayer.hair: "",
            AvatarLayer.face: "",
            AvatarLayer.scene: "",
        }

    def update_avatar_properties(self, customization_option):
        pass

    def export_avatar(self):
        print("export")