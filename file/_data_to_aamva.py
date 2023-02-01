import json

from dlgen.composer import Composer


with open('input.json', 'r') as fp:
    data_chad = json.load(fp)
composer = Composer()
aamva = composer.compose(data_chad)

# I/O: Write to stdout
print(aamva)
