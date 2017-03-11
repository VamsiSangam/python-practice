import turtle

# no. of sides of polygon element
sides = 5

# drawing a nested polygon
for steps in range(sides):
    turtle.forward(100)
    turtle.right(360 / sides)
    
    for innerSteps in range(sides):
        turtle.forward(50)
        turtle.right(360 / sides)