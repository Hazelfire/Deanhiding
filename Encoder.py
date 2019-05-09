from PIL import Image
from io import BytesIO


def fix_image(filename):
    with open(filename, "rb") as f:
        b = BytesIO()
        f.seek(15, 0)

        b.write(f.read())

        im = Image.open(b)
        return im


def split(number):
    segments = [number >> 4, number % 16]
    return segments


def flatten(pixel_array):
    return [rgb_value for pixel in pixel_array for rgb_value in pixel]


message = Image.open("tomdean.png")
cover = Image.open("part1.png")

result = Image.new("RGB", cover.size)

message_data = iter(message.getdata())

message_ended = False
current_pixel_data = []
result_data = []
i = 0
for pixel in cover.getdata():
    new_tuple = []
    if not message_ended:
        try:
            for value in pixel:
                parts_cover = split(value)

                if len(current_pixel_data) == 0:
                    message_pixel = message_data.__next__()
                    current_pixel_data = flatten(
                        [split(value) for value in message_pixel]
                    )

                parts_cover[1] = current_pixel_data[0]
                current_pixel_data = current_pixel_data[1:]

                new_tuple.append(parts_cover[0] * 16 + parts_cover[1])
            result_data.append(tuple(new_tuple))
        except StopIteration:
            message_ended = True
            for value in pixel[len(new_tuple) :]:
                new_tuple.append(value)
            result_data.append(tuple(new_tuple))
    else:
        result_data.append(pixel)
    i += 1
    print(i)

result.putdata(result_data)
result.save("tomdean.png")

print("Done!")
