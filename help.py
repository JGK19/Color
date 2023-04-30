ALTURA, LARGURA = 800, 600
rgb_max = 255

def get_color(x, max, min):
    x = x - min
    color = (x/max) * rgb_max
    if color > rgb_max:
        return rgb_max
    elif color < 0:
        return 0
    return int(color)

def get_color_rgb(x, max, min, actual_rgb):
    rgb = actual_rgb
    range = max - min
    range_scale = range/7
    setores = (range_scale * 1.5, range_scale * 3, range_scale * 4.5,
     range_scale * 6, range_scale * 7.5, range_scale*9)

    if x < ((setores[0]) + min):
        color = get_color(x, setores[0], min)
        return (rgb[0], color, rgb[2])
        

    elif x < ((setores[1]) + min):
        color = get_color(x, setores[1], setores[0])
        return (rgb_max - color, rgb[1], rgb[2])
        


    elif x < ((setores[2]) + min):
        color = get_color(x, setores[2], setores[1])
        return (rgb[0], rgb[1], color)
        


    elif x < ((setores[3]) + min):
        color = get_color(x, setores[3], setores[2])
        return (rgb[0], rgb_max - color, rgb[2])


    elif x < ((setores[4]) + min):
        color = get_color(x, setores[4], setores[3])
        return (color, rgb[1], rgb[2])


    elif x < ((setores[5]) + min):
        color = get_color(x, setores[5], setores[4])
        return (rgb[0], rgb[1], rgb_max - color)



    return rgb