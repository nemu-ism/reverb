import random

class colors:
    # RED = '\033[0;31m'
    # GREEN = '\033[0;32m'
    # YELLOW = '\033[0;33m'
    # BLUE = '\033[0;34m'
    # PURPLE = '\033[1;35m'
    # CYAN = '\033[0;36m'
    # WHITE = '\033[0;37m'

    INVISIBLE = '\033[08m'
    END = '\033[0m'

    def __init__(self):
        pass

    def random_color(self):
        color_palette = [
        '\033[0;31m',
        '\033[1;32m',
        '\033[0;33m',
        '\033[0;34m',
        '\033[1;35m',
        '\033[0;36m',
        '\033[0;37m'
        ]
        color = random.choice(color_palette)
        return color