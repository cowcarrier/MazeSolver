from PIL import Image

img = Image.open(r'C:\Users\braid200.png')
width, height = img.size
pixels = img.load()


# the main function
def solver(pixel):
    # finding the star and the end of the maze
    start = find_start(width, pixels)
    end = find_end(width, height, pixels)
    position = start
    split = []
    last_pos = []
    while position != end:
        last_pos.append(position[:])
        # checking where can be the next step
        x_right = check_x_right(pixel, position, last_pos)
        x_left = check_x_left(pixel, position, last_pos)
        y_up = check_y_up(pixel, position, last_pos)
        y_down = check_y_down(pixel, position, last_pos)
        # checks if it is a split, if so adding it to split list
        if x_right + x_left + y_down + y_up >= 2:
            split.append(position[:])
            if x_right:
                position[0] += 1
            elif x_left:
                position[0] -= 1
            elif y_up:
                position[1] += 1
            elif y_down:
                position[1] -= 1


        elif x_left + x_right + y_down + y_up == 1:
            if x_right:
                position[0] += 1
            elif x_left:
                position[0] -= 1
            elif y_up:
                position[1] += 1
            elif y_down:
                position[1] -= 1

        # if it is a dead end it goes back to the last split
        elif x_left + x_right + y_down + y_up == 0:
            position = split[-1]
            split = split[0:-1]

        print("pos", end=" ")
        print(position)


# checks if you can move to the right
def check_x_right(pixel, position, last):
    try:
        place = pixel[position[0] + 1, position[1]]
        pos = [position[0] + 1, position[1]]
        if place and pos not in last:
            return True
        else:
            return False
    except IndexError:
        return False


# checks if you can move to the left
def check_x_left(pixel, position, last):
    try:
        place = pixel[position[0] - 1, position[1]]
        pos = [position[0] - 1, position[1]]

        if place and pos not in last:
            return True
        else:
            return False
    except IndexError:
        return False


# checks if you can move up
def check_y_up(pixel, position, last):
    try:
        place = pixel[position[0], position[1] + 1]
        pos = [position[0], position[1] + 1]
        if place and pos not in last:
            return True
        else:
            return False
    except IndexError:
        return False


# checks if you can move down
def check_y_down(pixel, position, last):
    try:
        place = pixel[position[0], position[1] - 1]
        pos = [position[0], position[1] - 1]
        if place and pos not in last:
            return True
        else:
            return False
    except IndexError:
        return False


# finds the start
def find_start(width, pixel):
    for i in range(0, width):
        if pixel[i, 0]:
            return [i, 0]


# finds the end
def find_end(width, height, pixel):
    for i in range(0, width):
        if pixel[i, height - 1]:
            return [i, height - 1]


solver(pixels)
