a = 10
b = 20
c = 30
d = 4

print(a)		# 10
print(a + b)	# 30
print(b - c)	# -10
print(c * a)	# 300
print(c / a)	# 3.0
print(a ** d)   # 10000
print(c % a)	# 0

# Order of Operations
# () parantheses
# ** exponent
# */ multiplication, division
# +- addition, subtraction

# Formatting numbers
print('I have %d bats' % 2)		# I have 2 bats
print('I have %3d bats' % 2)	# I have   2 bats
print('I have %03d bats' % 2)	# I have 002 bats
print('I have %f bats' % 2)		# I have 2.000000 bats
print('I have %.2f bats' % 2)	# I have 2.00 bats

print('I have {0:d} bats'.format(2))		# I have 2 bats
print('I have {0:3d} bats'.format(2))		# I have   2 bats
print('I have {0:03d} bats'.format(2))		# I have 002 bats
print('I have {0:f} bats'.format(2))		# I have 2.000000 bats
print('I have {0:.2f} bats'.format(2))		# I have 2.00 bats

# Here are three numbers! The first is 4 The second is    6 and 8
print('Here are three numbers! The first is {0:d} The second is {1:4d} and {2:d}'.format(4, 6, 8))

# Sometimes commands are too long to fit in a line
# use \ to indicate command continues on next line
result = 1 + 2 + 3 \
    + 4 + 5		# indentation for this line is mandatory
print(result)	# 15

# But you can't use \ in strings, so break them first
print('Here are three numbers! The first is ' + \
    '{0:d} The second is {1:4d} and {2:d}'.format(4, 6, 8))	# indentation for this line is mandatory

# Functions to convert one data type to another
salary = input('Enter your salary - ')	# say 5000
bonus = input('Enter your bonus - ')	# say 50
payCheck = salary + bonus				# salary and bonus are 2 strings here!
print(payCheck)							# 500050

salary = int(salary)
bonus = int(bonus)
payCheck = salary + bonus				# salary and bonus are 2 ints here
print(payCheck)							# 5050

# other conversion functions
intValue = int('12345')
floatValue = float('3.14')
strValue = str(55)

print(intValue)
print(floatValue)
print(strValue)