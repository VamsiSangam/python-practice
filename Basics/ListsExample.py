# Take names for a party as input and display in sorted order

names = []  # empty list
print('Enter the person''s name who is attending the party (''DONE'' if finished) -')
name = input()

while name != 'DONE':
    if name != 'DONE':
        names.append(name)

    print('Enter the person''s name who is attending the party (''DONE'' if finished) -')
    name = input()

names.sort()

print('Here''s a sorted list of all the people attending the party!')
for name in names:
    print(name)