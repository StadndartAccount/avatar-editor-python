from Avatar import Head, Body
import Colors

class Silhouette:
    def __init__(self, body: Body, head: Head):
        self.body: Body = body
        self.head: Head = head


class BodySelectionModel:
    def __init__(self):
        self.options: list[Silhouette] = [
            Silhouette(Body.slim_body_3, Head.square_head),
            Silhouette(Body.slim_body_1, Head.square_head),
            Silhouette(Body.slim_body_2, Head.square_head),
            Silhouette(Body.wide_body_1, Head.wide_square_head),            
            Silhouette(Body.wide_body_2, Head.wide_square_head),            
            Silhouette(Body.wide_body_3, Head.square_head),            
        ]
        
        self.body_colors = Colors.clothes_colors        
        self.head_colors = Colors.head_colors

        self.selected_option = self.options[0]
        self.selected_body_color = self.body_colors[0]
        self.selected_head_color = self.head_colors[0]