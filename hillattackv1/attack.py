#Hill Attack v1
#This is the code used to determine the points scored by each entry.
#Expects the CSV to have at least 3 columns.

import itertools
import csv
import fileinput
import sys
import random
import leather

#Global Settings
hillcount = 5
soldiercount = 50


#Read in input, a filename.
filename = sys.argv[1]

#Read in the entries.
entries = []
with open(filename, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        entries.append({'name': row[1], 'soldiers': row[2:7], 'score': 0})
f.close()

#Delete the column headers.
del entries[0]

#Adjust the soldiers from strings to ints, and value check them.
print('There are ' + str(len(entries)) + ' entrants.')
for entry in entries:
    soldierints = []
    for soldier in entry.get('soldiers'):
        soldierints.append(int(soldier))

    #Max soldiers is 50.  Negative validation happens on the form, so 0 is the lowest value.
    if sum(soldierints) > soldiercount:
        print(entry.get('name') + '\'s soldiers have been smitten because they entered ' +  str(sum(soldierints)) + '.')
        for i in range(len(soldierints)): soldierints[i]=0 #SMITE THEM

    #Replace the list of strings with a list of ints.
    entry['soldiers']=soldierints

#Create matchups using built in combinations function.
matchups = list(itertools.combinations(entries, 2))

print('Running ' + str(len(matchups)) + ' matchups.')
#Play the matchups.
for matchup in matchups:
    leftpoints = 0
    rightpoints = 0
    #Iterate 5 times, for 5 hills.
    for i in range(0, hillcount):
        hillpoints = i + 1
        if matchup[0].get('soldiers')[i] > matchup[1].get('soldiers')[i]:
            leftpoints += hillpoints
        if matchup[0].get('soldiers')[i] == matchup[1].get('soldiers')[i]:
            leftpoints += hillpoints//2
            rightpoints += hillpoints//2
        if matchup[0].get('soldiers')[i] < matchup[1].get('soldiers')[i]:
            rightpoints += hillpoints

    entries[entries.index(matchup[0])]['score'] += leftpoints
    entries[entries.index(matchup[1])]['score'] += rightpoints

    print(matchup[0].get('name') + " vs " + matchup[1].get('name') + ": " + matchup[0].get('name') + " gained " + str(leftpoints) + ", and " + matchup[1].get('name') + " gained " + str(rightpoints))

print('Final Scores')
for entry in entries:
    print(entry.get('name') + ": " + str(entry.get('score')))

# analytics
def greenerizer(d):
    return 'rgb(%i, %i, %i)' % (d.x*5, 180, d.x*5)

def rederizer(d):
    return 'rgb(%i, %i, %i)' % (180, d.x*5, d.x*5)

def bluerizer(d):
    return 'rgb(%i, %i, %i)' % (d.x*5, d.x*5, 180)

def randorizer(d):
    return 'rgb(%i, %i, %i)' % (random.randint(0,250), random.randint(0,250), random.randint(0,250))


def getname(row, index):
    return row['name']

def getEntryScore(entry):
    return entry['score']

def getscore(row, index):
    return row['score']

def gethillsoldiers(row, index):
    return row

def gethillname(row, index):
    return "Hill " + str(index+1)

def gethillnum(row, index):
    return index+1

sortedentries = sorted(entries, key=getEntryScore)

# http://leather.readthedocs.io/en/0.3.3/

#Winning strategies by points allocated per hill
for entry in sortedentries:
    if entry['score'] == sortedentries[-1]['score']:
        winchart = leather.Chart('Winning Hill Points Allocation for ' + entry.get('name'))
        winchart.add_bars(entry.get('soldiers')[::-1], x=gethillsoldiers, y=gethillname, fill_color=randorizer)
        filename = "winchart-" + entry.get('name') + ".svg"
        winchart.to_svg(filename)


#Ordered entrants by total score.
chart = leather.Chart('Total Scores (Higher is better)')
chart.add_bars(sortedentries, x=getscore, y=getname, fill_color=randorizer)
chart.to_svg('scores.svg')

#Ordered hills by total alotted points.

#Winning strategy's win percentage per hill
