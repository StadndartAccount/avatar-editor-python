from Avatar import Head, Body


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

        self.selected_option = self.options[0]
        self.selected_body_color = self.body_colors[0]
        self.selected_head_color = self.head_colors[0]