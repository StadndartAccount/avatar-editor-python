import enum

class Tab(enum.Enum):
    body = 0
    hair = 1
    face = 2
    scene = 3
    history = 4

    def get_name(self) -> str:
        match self:
            case Tab.body: return "BODY"
            case Tab.hair: return "HAIR"
            case Tab.face: return "FACE"
            case Tab.scene: return "SCENE"            
            case Tab.history: return "HISTORY"            