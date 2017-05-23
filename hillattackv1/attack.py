#Hill Attack v1
#This is the code used to determine the points scored by each entry.
#Expects the CSV to have at least 3 columns.

import itertools
import csv
import fileinput
import sys

#Read in input
filename = sys.argv[1]

#Read in the entries.
entries = []
with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        entries.append({'timestamp': row[0], 'name': row[1], 'soldiers': row[2:], 'score': 0})
f.close()

#Delete the column headers.
del entries[0]

#Adjust the soldiers from strings to ints, and value check them.
for entry in entries:
	soldierints = []
	for soldier in entry.get('soldiers'):
		soldierints.append(int(soldier))
	
	#Max soldiers is 50.  Negative validation happens on the form, so 0 is the lowest value.
	if sum(soldierints) > 50:
		print(entry.get('name') + '\'s soldiers have been smitten because they entered ' +  str(sum(soldierints)) + '.')
		for i in range(len(soldierints)): soldierints[i]=0 #SMITE THEM
	
	#Replace the list of strings with a list of ints.
	entry['soldiers']=soldierints

#Create matchups using built in combinations function.
matchups = list(itertools.combinations(entries, 2))

#Play the matchups.
for matchup in matchups:
	leftpoints = 0
	rightpoints = 0
	#Iterate 5 times, for 5 hills.
	for i in range(1,6):
		if matchup[0].get('soldiers')[i-1] > matchup[1].get('soldiers')[i-1]:
			leftpoints += i
		if matchup[0].get('soldiers')[i-1] == matchup[1].get('soldiers')[i-1]:
			leftpoints += i//2
			rightpoints += i//2
		if matchup[0].get('soldiers')[i-1] < matchup[1].get('soldiers')[i-1]:
			rightpoints += i

	entries[entries.index(matchup[0])]['score'] += leftpoints
	entries[entries.index(matchup[1])]['score'] += rightpoints
	
#	print(matchup[0].get('name') + " vs " + matchup[1].get('name') + ": " + matchup[0].get('name') + " gained " + str(leftpoints) + ", and " + matchup[1].get('name') + " gained " + str(rightpoints))
		
print('Final Scores')
for entry in entries:
	print(entry.get('name') + ": " + str(entry.get('score')))