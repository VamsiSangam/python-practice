import Functions

def main():
    print('How many sides should the polygon have? ')
    sides = input()

    print('What should be the length of each side? ')
    sideLength = input()
    
    try:
        sides = int(sides)
        sideLength = int(sideLength)
        Functions.printPolygon(sides, sideLength)
    except ValueError:
        print('Size must be an integer')

main()