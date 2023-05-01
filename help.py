ALTURA, LARGURA = 800, 600
rgb_max = 255

def get_color(x, max, min):
    x = x - min
    color = (x/(max-min)) * rgb_max
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
        color = get_color(x, setores[2], setores[1])
        return (rgb[0], rgb[1], color)
    elif x < setores[3]:
        color = get_color(x, setores[3], setores[2])
        return (rgb[0], rgb_max - color, rgb[2])
    elif x < setores[4]:
        color = get_color(x, setores[4], setores[3])
        return (color, rgb[1], rgb[2])
    elif x < setores[5]:
        color = get_color(x, setores[5], setores[4])
        return (rgb[0], rgb[1], rgb_max - color)
    return rgb

def delta_sat(rgb):
    saturationPU = ((rgb - 127)/-127) * 127
    if saturationPU > 127:
        return 127
    return saturationPU

def get_sat_value(x, max, min, actual_rgb):
    x = x - min
    max = max - min
    rgb = actual_rgb
    sat_R = delta_sat(rgb[0])
    sat_G = delta_sat(rgb[1])
    sat_B = delta_sat(rgb[2])

    sat_R = rgb[0] + ((x/max) * sat_R)
    sat_G = rgb[1] + ((x/max) * sat_G)
    sat_B = rgb[2] + ((x/max) * sat_G)

    return (int(sat_R), int(sat_B), int(sat_G))