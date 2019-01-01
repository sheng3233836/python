from PIL import Image
import autopy


def resize_image(image_path, w_scale=1.0, h_scale=1.0):
    """
    Scale up the image
    :param image_path: image path
    :param w_scale: width scale
    :param h_scale: height scale
    :return: image
    """
    image = Image.open(image_path)
    width, height = image.size
    return image.resize((round(width * w_scale), round(height * h_scale)), Image.ANTIALIAS)


def format_color(rgb_color):
    """
    format rgb to hex
    :param rgb_color:
    :return:
    """
    return hex(autopy.color.rgb_to_hex(rgb_color[0], rgb_color[1], rgb_color[2]))
