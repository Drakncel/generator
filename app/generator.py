import random
import os

def random_rgb():
    return [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]

def generate_icon(cube_size=1):
    icon = []
    for _ in range (cube_size*cube_size):
        icon.append(random_rgb())
    return icon

fields = {
    "name": "string",
    "atk": "number",
    "hp": "number",
    "icon": "icon",
}

def get_syllables():
    PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
    syllables = []
    f = open(PROJECT_ROOT + "/syllables.csv", "r")
    while True:
        line = f.readline()
        if line == "":
            break
        syllables.append(line.replace("\n", ""))
    return syllables

def generate_string():
    syllables = get_syllables()
    nb_syllables = random.randint(2, 3)
    string = ""
    for _ in range (nb_syllables):
        new_syllable = syllables[random.randint(0, len(syllables) - 1)]
        string = string + new_syllable
    return string

def generate_number():
    return random.randint(0, 10)

type_generators = {
    "string": generate_string,
    "number": generate_number,
    "icon": generate_icon,
}

def generate_item():
    item = {}
    for key in fields:
        item[key] = type_generators[fields[key]]()
    return item

def generateCreatures(amount=20):
    items = []
    for _ in range(amount):
        item = generate_item()
        items.append(item)
    return items