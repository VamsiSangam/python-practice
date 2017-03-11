list = [178, 53, 7, 54, 97]

print(list[0])  # 178
print(list[-1]) # 97
print(list[-5]) # 178
# print(list[-6]) # IndexError - list index out of range

list[1] = 11        # modifying a list
list.append(-20)    # adding a value to end of list
print(list[-1])     # -20

print(list[0])      # 178
list.remove(178)    # Deleting a particular value
print(list[0])      # 11

del list[0]         # delete element in a list based on index
print(list[0])      # 7

# get index of an element in a list
print(list.index(54))   # 1

# Printing list items by length of list
length = len(list)

for index in range(length):
    print(list[index])  # 7, 54, 97, -20

# Printing list items by foreach style loop
for item in list:
    print(item)         # 7, 54, 97, -20

# Sorting items in a list
list.sort()

for item in list:
    print(item)         # -20, 7, 54, 97
