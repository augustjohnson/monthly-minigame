#Hill Attack v1
#This is the code used to determine the points scored by each entry.
#Expects the CSV to have at least 3 columns.

import itertools
import csv
import fileinput
import sys

#Read in input, a filename.
filename = sys.argv[1]
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}



#Read in the entries.
entries = []
with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        entries.append({'name': row[1], 'word': row[2], 'wordscore': 0})
f.close()

#Delete the column headers.
del entries[0]

#Adjust the soldiers from strings to ints, and value check them.
print('There are ' + str(len(entries)) + ' entrants.')
for entry in entries:
    word = entry.get('word').lower()
    entry['wordscore'] = sum(score[letter] for letter in word.lower())


print('Word Scores')
for entry in entries:
	print(entry.get('name') + ": " + str(entry.get('word')) + ": " + str(entry.get('wordscore')))
