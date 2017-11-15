## 2. Parsing the File ##

file = open("la_weather.csv", "r")
data = file.read()
rows = data.split("\n")
weather_data = []
for each in rows :
    split_each = each.split(',')
    weather_data.append(split_each)
print(weather_data)

## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []
for each in weather_data :
    weather.append(each[1])

## 4. Counting the Items in a List ##

count = 0
for each in weather :
    count += 1
print(count)

## 5. Removing the Header ##

new_weather = weather[1:]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = "cat" in animals
space_monster_found = "space_monster" in animals

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for each in weather_types :
    weather_type_found.append(each in new_weather)
print(weather_type_found)    