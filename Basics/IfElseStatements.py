# sample movie tickets code
movie = input('Which movie to you want to see? ')
amount = 0

if movie == 'Logan':
    ageCheck = input('Are all the persons above 18 years? (Y/N) ')
    ageCheck = (ageCheck == 'Y')	# True or False
    
if not ageCheck:
	print('Sorry people above 18 only are allowed!')
else:
	seats = int(input('How many seats do you want? '))
	
	if movie == 'Avengers':
		amount = 150 * seats
	
	if movie == 'Suicide Squad':
		amount = 200 * seats
		
	if movie == 'Logan':
		amount = 150 * seats
	
	print('Total amount = %d' % amount)

