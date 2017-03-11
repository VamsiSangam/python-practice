import csv

fileName = 'people.csv'
MODE = 'r'

with open(fileName, MODE) as myCSVFile: # automatic resource management, closes file
    data = csv.reader(myCSVFile)    # csv.reader(fileObject, delimeter = "'")
    # csv.reader() returns a list

    for row in data:
        # row is a list, we can access individual elements
        print('First Column = ' + row[0] + ', Second Column = ' + row[1])
        
        # or we can print the whole row
        print(row)
        
        # or we can format the row using join()
        print(', '.join(row))