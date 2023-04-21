ALTURA, LARGURA = 800, 600

def get_color(x):
    x = x-100
    color = (x/540) * 255

    if color > 255:
        return 255
    return int(color)
