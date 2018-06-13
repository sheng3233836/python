from PIL import Image
import autopy


def resize_image(image_path, w_scale=1.0, h_scale=1.0):
    image = Image.open(image_path)
    width, height = image.size
    return image.resize((round(width * w_scale), round(height * h_scale)), Image.ANTIALIAS)


def format_color(rgb_color):
    return hex(autopy.color.rgb_to_hex(rgb_color[0], rgb_color[1], rgb_color[2]))
