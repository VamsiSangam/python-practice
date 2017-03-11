import turtle

def printPolygon(sides, sideLength):
    for steps in range(sides):
        turtle.forward(sideLength)
        turtle.right(360 / sides)
    return

def main():
    length = 128
    sides = 3

    while length != 1:
        printPolygon(sides, length)
        turtle.forward(length / 4)
        sides += 1
        length /= 2

    return

# main()