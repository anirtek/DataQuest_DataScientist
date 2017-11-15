## 2. Built-In Functions ##

total = sum([6, 11])

## 3. Overwriting a Built-In Function ##

sum = sum(borrower_default_count_240)
print(sum)
test = sum(principal_outstanding_240)
print(test)

## 4. Scopes ##

def find_average(column):
    length = len(column)
    total = sum(column)
    return total / length

total = sum(borrower_default_count_240)
average = find_average(principal_outstanding_240)
print("average = ", average)
print("Total = ", total)

## 5. Scope Isolation ##

def find_average(column):
    length = len(column)
    total = sum(column)
    return total / length

def find_length(column):
    length = len(column)
    return length

length = len(borrower_default_count_240)
average = find_average(principal_outstanding_240)
principal_length = find_length(principal_outstanding_240)

## 6. Scope Inheritance ##

def find_average(column):
    total = sum(column)
    # In this function, we are going to pretend that we forgot to calculate the length
    return total / length

length = 10
average = find_average(principal_outstanding_240)
print(average, length)

## 7. Inheritance Limits ##

total = 10

def find_total(column):
    total = total + sum(column)
    return total

print(find_total(principal_outstanding_240))
print(total)

## 9. Global Variables ##

def my_function():
    global b
    b  = 20
my_function()
print(b)