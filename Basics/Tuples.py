# tuple is a sequence of 'immutable' objects
# unlike lists, elements of tuple cannot be modified
tuple = ('C', 'Java', 'C++', 'Python', 1, 2, 3)

print(tuple[1])     # Java
print(tuple[1:5])   # ('Java', 'C++', 'Python', 1)

tuple1 = (1, 2, 3)
tuple2 = ('Hello', 'World')
tuple3 = tuple1 + tuple2
print(tuple3)       # (1, 2, 3, 'Hello', 'World')

# Deleting inidividual tuple elements is not allowed
# del tuple1        # deletes entire tuple

# Tuple operations
print(len(tuple3))              # 5                     # Length
print(('Hi! ') * 4)             # Hi! Hi! Hi! Hi!       # Repetition
print(3 in (1, 2, 3))           # True                  # Membership
for x in (1, 2, 3): print(x)    # 1 2 3                 # Iteration
print(tuple3[3:])               # ('Hello', 'World')    # Slicing

# tuple inside a tuple
tuple4 = (tuple1, tuple2, tuple3, 4, '5')
print(tuple4)   # ((1, 2, 3), ('Hello', 'World'), (1, 2, 3, 'Hello', 'World'), 4, '5')
print(len(tuple4))  # 5