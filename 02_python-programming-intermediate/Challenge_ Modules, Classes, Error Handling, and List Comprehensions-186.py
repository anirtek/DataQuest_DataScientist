## 2. Introduction to the Data ##

import csv
nfl_suspensions = list(csv.reader(open("nfl_suspensions_data.csv")))
header = nfl_suspensions[0]
print(header)
nfl_suspensions  = nfl_suspensions[1:]
years = {}
for each in nfl_suspensions :
    if each[5] not in years :
        years[each[5]] = 1
    else :
        years[each[5]] += 1
print(years)

## 3. Unique Values ##

unique_teams = set([each[1] for each in nfl_suspensions])
unique_games = set([each[2] for each in nfl_suspensions])
print(unique_teams)
print(unique_games)

## 4. Suspension Class ##

class Suspension :
    def __init__(self, input_list) :
        self.name = input_list[0]
        self.team = input_list[1]
        self.games = input_list[2]
        self.year = input_list[5]
third_suspension = Suspension(nfl_suspensions[2])

## 5. Tweaking the Suspension Class ##

class Suspension():
    def __init__(self,row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        try :
            self.year = int(row[5])
        except Exception :
            self.year = 0
    def get_year(self):
        return self.year
missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()
print(twenty_third_year)