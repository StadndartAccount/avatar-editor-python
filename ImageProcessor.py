from xml.etree import ElementTree as ET
from PIL import Image
import io
import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

class ImageProcessor:
    def change_svg_color(self, input_svg, old_color, new_color):
        tree = ET.parse(input_svg)
        root = tree.getroot()

        ns = {'svg': 'http://www.w3.org/2000/svg'}

        for elem in root.findall(f'.//svg:*[@fill="{old_color}"]', ns):
            elem.set('fill', new_color)

        return ET.tostring(root, encoding='unicode')

    def convert_svg_to_png(self, svg_content):
        temp_svg_path = "temp.svg"
        with open(temp_svg_path, "w") as f:
            f.write(svg_content)

        drawing = svg2rlg(temp_svg_path)
        png_data = renderPM.drawToString(drawing, fmt='PNG')
        
        os.remove(temp_svg_path)

        return Image.open(io.BytesIO(png_data))

    def process_image(self, input_svg, old_color, new_color):
        svg_content = self.change_svg_color(input_svg, old_color, new_color)
        png_image = self.convert_svg_to_png(svg_content)
        return png_image

    def overlay_png_images(self, png_images):
        if not png_images:
            raise ValueError("Список PNG изображений не может быть пустым.")

        base_image = png_images[0].convert("RGBA")

        for overlay_image in png_images[1:]:
            base_image = Image.alpha_composite(base_image, overlay_image.convert("RGBA"))

        return base_image
    
    def overlay_svg_images(self, svg_images):
        png_images = map(lambda svg: self.convert_svg_to_png(svg), svg_images)
        
        return self.overlay_png_images(png_images)