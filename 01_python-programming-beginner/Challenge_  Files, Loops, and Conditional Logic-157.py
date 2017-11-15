## 3. Read the File Into a String ##

fp = open("dq_unisex_names.csv", "r")
names = fp.read()
print(names)

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split("\n")
first_five = names_list[:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = [] # empty list created
for each in names_list :
    split_each = each.split(",")
    print(type(split_each))
    nested_list.append(split_each)
print(nested_list)

## 6. Convert Numerical Values ##

numerical_list = [] #empty list
for each in nested_list :
    name = each[0]
    val = each[1]
    temp_list = [name, float(val)]
    numerical_list.append(temp_list)
print(numerical_list)

## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater = [] # empty list created
for each in numerical_list :
    if each[1] >= 1000 :
        thousand_or_greater.append(each[0])
print(thousand_or_greater[:11])