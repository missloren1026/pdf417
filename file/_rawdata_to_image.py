from pdf417 import render_image

from dlgen.encoding import encode


def data_to_list(data):
    while data[-1] == ',':
        data = data[:-1]
    return [int(x) for x in data.split(',')]


# I/O: Read from stdin
data = input()

data_words = data_to_list(data)
codes = encode(
    data_words,
    encoding="ascii",
    columns=13,
    security_level=5,
    numeric_compaction=True
)
image = render_image(codes)  # Pillow Image object
image.show()

# IO: Save as a file
image.save('output.png')
