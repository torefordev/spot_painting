from colorgram import extract
ext = extract('image.jpg',26)
colors = []
for color in ext:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r,g,b)
    colors.append(rgb)


print(colors)