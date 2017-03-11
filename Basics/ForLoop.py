import turtle

# basic for loop
for steps in range(1, 5):   # [1, 5)
    print(steps)

# range(start, end, stepSize)
for steps in range(1, 10, 2):   # [1, 10)
    print(steps)

# range() is actually returning a list
for steps in [1, 2, 3, 4, 5]:
    print(steps)

for color in ['red', 'blue', 'green', 'yellow']:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)