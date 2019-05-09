from PIL import Image

hidden = Image.open("part1.png")
dimensions = Image.open("mini_tom.png").size

result_data = []

i = 0

value_elements = []
rgb_tuple = []

for pixel in hidden.getdata():
    if i >= dimensions[0] * dimensions[1] * 2:
        break
    for value in pixel:
        message = value % 16
        value_elements.append(message)

        if len(value_elements) == 2:
            rgb_tuple.append(value_elements[0] * 16 + value_elements[1])
            value_elements = []

        if len(rgb_tuple) == 3:
            result_data.append(tuple(rgb_tuple))
            rgb_tuple = []
    i += 1

result_image = Image.new("RGB", dimensions)
result_image.putdata(result_data)
result_image.save("back.png")
