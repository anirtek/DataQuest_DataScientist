## 2. Sets ##

print(type(legislators)) #for confirmation
gender = [] #defined an empty list
for each in legislators : #looping over the dataset
    gender.append(each[3])
gender = set(gender) #converted gender list into a set
print(gender)

## 3. Exploring the Dataset ##

party = []
for each in legislators :
    party.append(each[6])
party = set(party)
print(party)
print("Unique Parties: ",len(party))
print("Total Dataset Entries: ",len(legislators))
print("Average contribution of each party = ", len(legislators)/len(party))
for each in legislators:
    print(each)

## 4. Missing Values ##

for each in legislators:
    if each[3] == '':
        each[3] = 'M'
print(legislators)

## 5. Parsing Birth Years ##

#create and empty list birth years
birth_years = []
for each in legislators :
    parts = each[2].split("-") #parts contains the list of splitted data
    birth_years.append(parts[0])
print(birth_years)

## 6. Try/except Blocks ##

try:
    float('hello')
except Exception:
    print("Error converting to float.")

## 7. Exception Instances ##

try :
    int('')
except Exception as e :
    print(type(e))
    print(str(e))

## 8. The Pass Keyword ##

converted_years = []
for each in birth_years :
    year = each
    try:
        year = int(year)
    except Exception:
        pass
    converted_years.append(year)

## 9. Convert Birth Years to Integers ##

for row in legislators:
    birthday = row[2].split('-')
    birth_year = birthday[0]
    try:
        birth_year = int(birth_year)
    except Exception:
        birth_year = 0
    row.append(birth_year)
for each in legislators :
    print(each)

## 10. Fill in Years Without a Value ##

last_value = 1
for row in legislators :
    if row[7] == 0 :
        row[7] = last_value
    last_value = row[7]
for each in legislators :
    print(each)