

```python
f = open("US_births_1994-2003_CDC_NCHS.csv", "r")
data = f.read()
rows = data.split("\n")
print(rows[:10])
```

    ['year,month,date_of_month,day_of_week,births', '1994,1,1,6,8096', '1994,1,2,7,7772', '1994,1,3,1,10142', '1994,1,4,2,11248', '1994,1,5,3,11053', '1994,1,6,4,11406', '1994,1,7,5,11251', '1994,1,8,6,8653', '1994,1,9,7,7910']



```python
def read_csv(input_file) :
    f = open(input_file, "r")
    data = f.read()
    rows = data.split('\n') # data saved as list of lists
    string_list = rows[1:] # removed the header
    final_list = [] # final list
    for each in string_list :
        int_fields = [] # empty list
        string_fields = each.split(',') # splitted over ','
        for i in string_fields :
            int_fields.append(int(i))
        final_list.append(int_fields)
    return final_list

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
print(cdc_list[:10]) # printing just first 10 lines 
```

    [[1994, 1, 1, 6, 8096], [1994, 1, 2, 7, 7772], [1994, 1, 3, 1, 10142], [1994, 1, 4, 2, 11248], [1994, 1, 5, 3, 11053], [1994, 1, 6, 4, 11406], [1994, 1, 7, 5, 11251], [1994, 1, 8, 6, 8653], [1994, 1, 9, 7, 7910], [1994, 1, 10, 1, 10498]]



```python
def month_births(input_list) :
    births_per_month = {} # empty dictionary created
    for each in input_list :
        month = each[1] # extracted the month number
        births = each[4] # extracted the births 
        if month in births_per_month :
            births_per_month[month] += int(births)
        else :
            births_per_month[month] = int(births)
    return births_per_month

#calling the function above
cdc_month_births = month_births(cdc_list)
print(cdc_month_births)
```

    {1: 3232517, 2: 3018140, 3: 3322069, 4: 3185314, 5: 3350907, 6: 3296530, 7: 3498783, 8: 3525858, 9: 3439698, 10: 3378814, 11: 3171647, 12: 3301860}



```python
def dow_births(input_list) :
    births_per_week = {} # empty dictionary created
    for each in input_list :
        month = each[3] # extracted the month number
        births = each[4] # extracted the births 
        if month in births_per_week :
            births_per_week[month] += int(births)
        else :
            births_per_week[month] = int(births)
    return births_per_week

#calling the function above
cdc_day_births = dow_births(cdc_list)
print(cdc_day_births)
```

    {1: 5789166, 2: 6446196, 3: 6322855, 4: 6288429, 5: 6233657, 6: 4562111, 7: 4079723}



```python
# more generalized function
def calc_counts(data, column):
    number_of_births = {}
    for each in data :
        #print(each[column])
        
        if each[column] in number_of_births :
            number_of_births[each[column]] += int(each[4])
        else :
            number_of_births[each[column]] = int(each[4])
    return number_of_births

#calling the function
cdc_year_births = calc_counts(cdc_list, 0)
print(cdc_year_births)
cdc_month_births = calc_counts(cdc_list, 1)
print(cdc_month_births)
cdc_dom_births = calc_counts(cdc_list, 2)
print(cdc_dom_births)
cdc_dow_births = calc_counts(cdc_list, 3)
print(cdc_dow_births)
```

    {2000: 4058814, 2001: 4025933, 2002: 4021726, 2003: 4089950, 1994: 3952767, 1995: 3899589, 1996: 3891494, 1997: 3880894, 1998: 3941553, 1999: 3959417}
    {1: 3232517, 2: 3018140, 3: 3322069, 4: 3185314, 5: 3350907, 6: 3296530, 7: 3498783, 8: 3525858, 9: 3439698, 10: 3378814, 11: 3171647, 12: 3301860}
    {1: 1276557, 2: 1288739, 3: 1304499, 4: 1288154, 5: 1299953, 6: 1304474, 7: 1310459, 8: 1312297, 9: 1303292, 10: 1320764, 11: 1314361, 12: 1318437, 13: 1277684, 14: 1320153, 15: 1319171, 16: 1315192, 17: 1324953, 18: 1326855, 19: 1318727, 20: 1324821, 21: 1322897, 22: 1317381, 23: 1293290, 24: 1288083, 25: 1272116, 26: 1284796, 27: 1294395, 28: 1307685, 29: 1223161, 30: 1202095, 31: 746696}
    {1: 5789166, 2: 6446196, 3: 6322855, 4: 6288429, 5: 6233657, 6: 4562111, 7: 4079723}



```python
def calc_min(input_dict, key) :
    min = input_dict[key]
    for each in input_dict :
        if min >= input_dict[each] :
            min = input_dict[each]
    return min

def calc_max(input_dict, key) :
    max = input_dict[key]
    for each in input_dict :
        if max <= input_dict[each] :
            max = input_dict[each]
    return max

cdc_year_min = calc_min(cdc_year_births, 1994)
print(cdc_year_min)
cdc_year_max = calc_max(cdc_year_births, 1994)
print(cdc_year_max)
```

    3880894
    4089950

