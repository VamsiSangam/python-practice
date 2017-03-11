# import statement gives us access to
# the functionalities of datetime class
import datetime

# today is a function that returns today's date
currentDate = datetime.date.today()

print(currentDate)
print(currentDate.day)
print(currentDate.month)
print(currentDate.year)

# formatting dates
print(currentDate.strftime('%d %b, %Y'))	# strftime() means stringFromTime()

# %d is day of the month
# %b is the month abbreviation
# %B is the month full name
# %y is two digit year
# %Y is four digit year
# %a is the day of the week abbreviated
# %A is the day of the week

# another example of formatting date
print(currentDate.strftime('Please attend our event %A, %B %d in the year %Y'))

# taking input from user
userInput = input('When is your next birthday? (mm/dd/yyyy) ')
nextBirthday = datetime.datetime.strptime(userInput, '%m/%d/%Y').date()
# Why did we list datetime twice?
# because we are calling the strptime() function
# which is a part of the datetime class
# which is in the datetime module
print('Your birth month is ' + nextBirthday.strftime('%B'))

# date arithmetic
difference = nextBirthday - currentDate
print('%d days left for your birthday!' % difference.days)

# printing time time part
currentTime = datetime.datetime.now()
print(currentTime)
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)

# formatting time
print(datetime.datetime.strftime(currentTime, '%I:%M:%S %p'))

# %H for hours - 24hr clock
# %I for hours - 12hr clock
# %p for AM or PM
# %m for minutes
# %S for seconds