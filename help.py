ALTURA, LARGURA = 800, 600
rgb_max = 255

def get_color(x, max, min):
    print(f'max:{max}')
    print(f'min:{min}')
    print(f'x:{x}')
    x = x - min
    color = (x/max) * rgb_max
    if color > rgb_max:
        return rgb_max
    elif color < 0:
        return 0
    return int(color)

def get_color_rgb(x, max, min, actual_rgb):
    x = x - min
    rgb = actual_rgb
    range = max - min
    range_scale = range/7
    setores = (range_scale * 1.5, range_scale * 2.5, range_scale * 3.5,
     range_scale * 4.5, range_scale * 5.5, range_scale * 7)

    if x < setores[0]:
        color = get_color(x, setores[0], 0)
        return (rgb[0], color, rgb[2])
    elif x < setores[1]:
        color = get_color(x, setores[1], setores[0])
        return (rgb_max - color, rgb[1], rgb[2])
    elif x < setores[2]:
        pass
    elif x < setores[3]:
        pass
    elif x < setores[4]:
        pass
    elif x < setores[5]:
        pass
    return rgb