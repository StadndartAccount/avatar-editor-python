from Avatar import Head, Body


class Silhouette:
    def __init__(self, body: Body, head: Head):
        self.body: Body = body
        self.head: Head = head


class BodySelectionModel:
    def __init__(self):
        
        self.selected_option_index = 0
        self.selected_body_color_index = 0
        self.selected_head_color_index = 0

        self.body_head_combinations: list[Silhouette] = [
            Silhouette(Body.triangle_body, Head.circle_head),
            Silhouette(Body.triangle_body, Head.square_head),
            Silhouette(Body.wide_rectangle_body, Head.wide_square_head),            
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