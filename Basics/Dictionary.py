# dictionary is created using {}
dict = {'Name' : 'Vamsi Sangam', 'Age' : 21, }  # can end with ','

# Key is supposed to be immutable, eg. strings, numbers etc.
# A list cannot be used as a Key - gives TypeError
# dict = {['Name'] : 'Vamsi'}   # TypeError: unhashable type: 'list'

print(dict['Name'])     # Accessed by using []
dict['Name'] = 'Vamsi'  # modifying values
print(dict['Name'])

dict['github'] = 'github.com/vamsisangam'   # creating new entry
print(dict['github'])
del dict['github']      # deleting an entry
# print(dict['github']) # gives 'KeyError'

del dict        # deletes entire dictionary

dict = {}       # re-initialise dictionary if deleted

dict[1] = 1
dict[2] = 4
dict[3] = 9
dict[4] = 16
dict[5] = 25

print(dict)     # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

dict.clear()    # deletes all entries, but dictionary still exists
dict[1] = 1     # you can't do this if you used 'del'
                # If you used 'del' you'd have to use 'dict = {}' first
print(dict)     # {1: 1}