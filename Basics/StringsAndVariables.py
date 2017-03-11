# use input(prompt_message) to take input from user
name = input('What is your name? ')
print(name)

# if you want the input to be on next line
print('What is your name?')
name = input()
print(name)

# use + to combine variables and strings
firstName = input('What is your first name? ')
lastName = input('What is your last name? ')
print('Hello ' + firstName + ' ' + lastName)

# a fun story teller program
animal = input('What is your favourite animal? ')					# say 'lion'
building = input('Name a famous building: ')						# say 'Empire State Building'
color = input('What is your favourite color? ')						# say 'blue'
print('Hickory Dickory Dock!')
print('The ' + color + ' ' + animal + ' ran up the ' + building)	# The blue Lion ran up the Empire State Building

# string functions
message = 'hElLo woRld!'
print(message.lower())					# hello world!
print(message.upper())					# HELLO WORLD!
print(message.swapcase())				# HeLlo WOrLD!
print(message.find('woRld'))			# 6
print(message.count('o'))				# 2
print(message.capitalize())				# Hello world! --> interesting!
print(message.replace('hElLo', 'Hi'))	# Hi woRld!

# Have a user enter their postal code and then display that  postal
# code in upper case letters even if the user typed it in lowercase
postalCode = input('Please enter your postal code: ') #	say '530016ap'
print(postalCode.upper())	# 530016AP