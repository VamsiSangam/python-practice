# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# Author - Vamsi Sangam - https://github.com/VamsiSangam

line = input()
freq = {}
words = line.split(' ')	# splits on all whitespace if left unspecified

for word in words:
    if word in freq:
    	freq[word] = freq[word] + 1
    else:
    	freq[word] = 0

words = sorted(freq)

for word in words:
    print('Word -> %s    Freq -> %d\n' % (word, freq[word]))