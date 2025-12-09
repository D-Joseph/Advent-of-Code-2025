from utils.box import Box

def read_boxes(path="./playground_input.txt"):
    boxes = []
    with open(path, 'r') as file:
        for line in file:
            boxes.append(Box(line.strip()))
    return boxes