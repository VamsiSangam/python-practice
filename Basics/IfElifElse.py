# Just trying to say Hi to all
country = input('Where are you from? ').upper()

if country == 'INDIA':
	print('Namaste')
elif country == 'GERMANY':
	print('Guten Tag')
elif country == 'FRANCE':
	print('Bonjour')
else:
	print('Hello / Aloha / Ciao / G''day')

# Let's cheer for team India!
sport = input('Enter your favourite sport - ').capitalize()
player = input('Enter your favourite player - ').capitalize()

if sport == 'Cricket' and player == 'Kohli':
	print('Yeaaah! Go Kohli!!')


# writing long conditions
favMovie = input('What is your favourite movie? ')
favBook = input('What is your favourite book? ')
favColor = input('What is your favourite color? ')

# and takes precedence over or
# to override, use parantheses
if favMovie == 'Harry Potter' and \
	(favBook == 'Harry Potter' or favBook == 'Sherlock Holmes') and \
	(favColor == 'Blue' or favColo == 'Black'):
	print('You and I should hang out!')
else:
	print('I got nothing to say to you :P') 