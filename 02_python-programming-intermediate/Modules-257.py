## 1. Introduction to Modules ##

import math
root = math.sqrt(99)
flr = math.floor(89.9)
print(root, flr)

## 2. Importing Using An Alias ##

import math as m
root = m.sqrt(33)

## 3. Importing A Specific Object ##

from math import *
root = math.sqrt(1001)
print(root)

## 4. Variables Within Modules ##

import math
a = math.sqrt(math.pi)
b = math.ceil(math.pi)
c = math.floor(math.pi)
print(a, b, c)

## 5. The CSV Module ##

import csv
#open the file
f = open("nfl.csv")
#call the module's reader() function
csvreader = csv.reader(f)
# convert the result into a list of lists
nfl = list(csvreader)
for each in nfl :
    print(each)

## 6. Counting How Many Times a Team Won ##

import csv
f = open("nfl.csv")
csv_reader = csv.reader(f)
nfl = list(csv_reader)
patriots_wins = 0
for each in nfl :
    if each[2] == "New England Patriots" :
        patriots_wins += 1
print(patriots_wins)

## 7. Making a Function that Counts Wins ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here.
def nfl_wins(name) :
    wins = 0
    for each in nfl :
        if each[2] == name :
            wins += 1
    return wins
# calling the functions
cowboys_wins = nfl_wins("Dallas Cowboys")
falcons_wins = nfl_wins("Atlanta Falcons")