fileName = 'names.txt'
WRITE = 'w'

file = open(fileName, WRITE)    # by default open() opens a file with read access

# r - read
# w - write
# w+ - read & write
# a - append
# b - binary

file.write('Vamsi Sangam\n')            # write doesn't add \n at the end
file.write('Shanmukh Dundigalla\n')     # must add \n explicitly

file.close()

# reading a file
READ = 'r'

file = open(fileName, READ)

str = file.read()       # reads the whole file
print(str)

file.close()

# reading a file line by line
file = open(fileName, READ)

str = file.readline()   # reads a single line
print(str)
str = file.readline()
print(str)

file.close()