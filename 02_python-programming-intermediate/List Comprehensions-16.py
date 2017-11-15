## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]
for ship, car in enumerate(ships) :
    print(ships[ship])
    print(cars[ship])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]
for idx, thing in enumerate(things):
    thing.append(trees[idx])
print(things)

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [2 * each for each in apple_prices]
apple_prices_lowered = [each - 100 for each in apple_prices]
print(apple_prices_doubled, apple_prices_lowered)

## 5. Counting Female Names ##

name_counts = {}
for each in legislators :
    if each[3] == 'F' and each[7] > 1940 :
        name = each[1]
        if name in name_counts :
            name_counts[name] += 1
        else :
            name_counts[name] = 1
print(name_counts)

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []
for value in values:
    status = value is not None and value > 30
    checks.append(status)
print(checks) 

## 8. Highest Female Name Count ##

max_value  = None
for each in name_counts :
    count = name_counts[each]
    if max_value is None or count > max_value :
        max_value = count
print(name_counts)
print(max_value)

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for name, plant_type in plant_types.items():
    print(name)
    print(plant_type)

## 10. Finding the Most Common Female Names ##

top_female_names = []
for key, value in name_counts.items() :
    if value == 2 :
        top_female_names.append(key)

## 11. Finding the Most Common Male Names ##

male_name_counts = {}
for each in legislators :
    if each[3] == "M" and each[7] > 1940 :
        name = each[1]
        if name in male_name_counts :
            male_name_counts[name] += 1
        else :
            male_name_counts[name] = 1
print(male_name_counts) #printing dictionary that is ready now

#finding higest male count of names
highest_male_count = None
for key, value in male_name_counts.items() :
    if highest_male_count is None or value > highest_male_count :
        highest_male_count = value
print(highest_male_count)

#defining list for holding most common name
top_male_names = []
for key, value in male_name_counts.items() :
    if value == highest_male_count :
        top_male_names.append(key)
print(top_male_names)