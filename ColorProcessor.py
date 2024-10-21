def rgb2hex(rgb_color: tuple[int, int, int] | tuple[int, int, int, int]):
    if len(rgb_color) == 3:
        return "#{:02x}{:02x}{:02x}".format(rgb_color[0], rgb_color[1], rgb_color[2])
    else:
        return "#{:02x}{:02x}{:02x}{:02x}".format(rgb_color[0], rgb_color[1], rgb_color[2], rgb_color[3])
