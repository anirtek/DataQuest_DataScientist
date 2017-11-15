## 2. Defining the Dataset Class ##

class Dataset :
    def __init__(self) :
        self.type = "csv" # type attribute
        
dataset = Dataset() # instance of the class = object using initializer Dataset()
print(dataset.type)

## 3. Passing Additional Arguments to the Initializer ##

import csv
class Dataset:
    def __init__(self, data): #always keep 'safe' as the first argument
        self.data = data # set value to the attribute "data"

f = open("nfl.csv")
csvreader = csv.reader(f)
nfl_data = list(csvreader) # data stored into the list of lists
nfl_dataset = Dataset(nfl_data) # creating the instance of the class
dataset_data = nfl_dataset.data
print(dataset_data)

## 4. Adding Additional Behavior ##

class Dataset:
    def __init__(self, data):
        self.data = data 
    # Your method goes here
    def print_data(self, num_rows):
        print(self.data[:num_rows])

nfl_dataset = Dataset(nfl_data) 
nfl_dataset.print_data(5)

## 5. Enhancing the Initializer ##

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:] # also works as the header extracter

nfl_dataset = Dataset(nfl_data)
nfl_header = nfl_dataset.header
print(nfl_header)

## 6. Grabbing Column Data ##

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
        
    # Add your method here.
    def column(self, label):
        if label in self.header :
            index = 0
            for idx, value in enumerate(self.header) :
                if value == label :
                    index = idx
            column_data = []
            for each in self.data :
                column_data.append(each[index])
            return column_data
        else :
            return None
        #return column_data
        
# calling the function        
nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')
print(year_column)
player_column = nfl_dataset.column('player')
print(player_column)

## 7. Count Unique Method ##

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def column(self, label):
        if label not in self.header:
            return None
        
        #get the index of the required column
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        #extract the required column data
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
    # Add your count unique method here
    def count_unique(self, label):
        data = self.column(label)
        counter = 0
        unique_items_list = []
        for each in data :
            if each not in unique_items_list :
                unique_items_list.append(each)
                counter += 1
        return counter

nfl_dataset = Dataset(nfl_data)
total_years = nfl_dataset.count_unique('year')

## 8. Make Objects Human Readable ##

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    # Add the special method here
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
        
    def count_unique(self, label):
        count = 0
        for item in set(self.column(label)):
            count += 1
        return count
    
    def __str__(self):
        return str(self.data[:10])

nfl_dataset = Dataset(nfl_data)
print(nfl_dataset)