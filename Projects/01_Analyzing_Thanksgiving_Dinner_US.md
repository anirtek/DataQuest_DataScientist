

```python
# Analyzing Thanksgiving Dinner
```


```python
import pandas as p
data = p.read_csv("thanksgiving.csv", encoding = "Latin-1")
print(data.head())
print(data.column)
```

       RespondentID Do you celebrate Thanksgiving?  \
    0    4337954960                            Yes   
    1    4337951949                            Yes   
    2    4337935621                            Yes   
    3    4337933040                            Yes   
    4    4337931983                            Yes   
    
      What is typically the main dish at your Thanksgiving dinner?  \
    0                                             Turkey             
    1                                             Turkey             
    2                                             Turkey             
    3                                             Turkey             
    4                                           Tofurkey             
    
      What is typically the main dish at your Thanksgiving dinner? - Other (please specify)  \
    0                                                NaN                                      
    1                                                NaN                                      
    2                                                NaN                                      
    3                                                NaN                                      
    4                                                NaN                                      
    
      How is the main dish typically cooked?  \
    0                                  Baked   
    1                                  Baked   
    2                                Roasted   
    3                                  Baked   
    4                                  Baked   
    
      How is the main dish typically cooked? - Other (please specify)  \
    0                                                NaN                
    1                                                NaN                
    2                                                NaN                
    3                                                NaN                
    4                                                NaN                
    
      What kind of stuffing/dressing do you typically have?  \
    0                                        Bread-based      
    1                                        Bread-based      
    2                                         Rice-based      
    3                                        Bread-based      
    4                                        Bread-based      
    
      What kind of stuffing/dressing do you typically have? - Other (please specify)  \
    0                                                NaN                               
    1                                                NaN                               
    2                                                NaN                               
    3                                                NaN                               
    4                                                NaN                               
    
      What type of cranberry saucedo you typically have?  \
    0                                               None   
    1                             Other (please specify)   
    2                                           Homemade   
    3                                           Homemade   
    4                                             Canned   
    
      What type of cranberry saucedo you typically have? - Other (please specify)  \
    0                                                NaN                            
    1                    Homemade cranberry gelatin ring                            
    2                                                NaN                            
    3                                                NaN                            
    4                                                NaN                            
    
              ...          \
    0         ...           
    1         ...           
    2         ...           
    3         ...           
    4         ...           
    
      Have you ever tried to meet up with hometown friends on Thanksgiving night?  \
    0                                                Yes                            
    1                                                 No                            
    2                                                Yes                            
    3                                                Yes                            
    4                                                Yes                            
    
      Have you ever attended a "Friendsgiving?"  \
    0                                        No   
    1                                        No   
    2                                       Yes   
    3                                        No   
    4                                        No   
    
      Will you shop any Black Friday sales on Thanksgiving Day?  \
    0                                                 No          
    1                                                Yes          
    2                                                Yes          
    3                                                 No          
    4                                                 No          
    
      Do you work in retail? Will you employer make you work on Black Friday?  \
    0                     No                                              NaN   
    1                     No                                              NaN   
    2                     No                                              NaN   
    3                     No                                              NaN   
    4                     No                                              NaN   
    
      How would you describe where you live?      Age What is your gender?  \
    0                               Suburban  18 - 29                 Male   
    1                                  Rural  18 - 29               Female   
    2                               Suburban  18 - 29                 Male   
    3                                  Urban  30 - 44                 Male   
    4                                  Urban  30 - 44                 Male   
    
      How much total combined money did all members of your HOUSEHOLD earn last year?  \
    0                                 $75,000 to $99,999                                
    1                                 $50,000 to $74,999                                
    2                                       $0 to $9,999                                
    3                                    $200,000 and up                                
    4                               $100,000 to $124,999                                
    
                US Region  
    0     Middle Atlantic  
    1  East South Central  
    2            Mountain  
    3             Pacific  
    4             Pacific  
    
    [5 rows x 65 columns]



    

    AttributeErrorTraceback (most recent call last)

    <ipython-input-2-95f6b01ad902> in <module>()
          2 data = p.read_csv("thanksgiving.csv", encoding = "Latin-1")
          3 print(data.head())
    ----> 4 print(data.column)
    

    /dataquest/system/env/python3/lib/python3.4/site-packages/pandas/core/generic.py in __getattr__(self, name)
       2742             if name in self._info_axis:
       2743                 return self[name]
    -> 2744             return object.__getattribute__(self, name)
       2745 
       2746     def __setattr__(self, name, value):


    AttributeError: 'DataFrame' object has no attribute 'column'



```python
## Filtering out rows from a dataframe 
```


```python
count = data["Do you celebrate Thanksgiving?"].value_counts()
print(count)
```

    Yes    980
    No      78
    Name: Do you celebrate Thanksgiving?, dtype: int64



```python
yesData = data[data["Do you celebrate Thanksgiving?"] == "Yes"]
```


```python
## Using value_counts to explore main dishes
```


```python

data["What is typically the main dish at your Thanksgiving dinner?"].value_counts()
```




    Turkey                    859
    Other (please specify)     35
    Ham/Pork                   29
    Tofurkey                   20
    Chicken                    12
    Roast beef                 11
    I don't know                5
    Turducken                   3
    Name: What is typically the main dish at your Thanksgiving dinner?, dtype: int64




```python
gravyCount = data[data["What is typically the main dish at your Thanksgiving dinner?"] == "Tofurkey"]["Do you typically have gravy?"]
print(gravyCount)
```

    4      Yes
    33     Yes
    69      No
    72      No
    77     Yes
    145    Yes
    175    Yes
    218     No
    243    Yes
    275     No
    393    Yes
    399    Yes
    571    Yes
    594    Yes
    628     No
    774     No
    820     No
    837    Yes
    860     No
    953    Yes
    Name: Do you typically have gravy?, dtype: object



```python
## Figuring out what pies people eat
```


```python
apple_count = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"].value_counts()
print(apple_count)
```

    Apple    514
    Name: Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple, dtype: int64



```python
pumpkin_count = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"].value_counts()
print(pumpkin_count)
```

    Pumpkin    729
    Name: Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin, dtype: int64



```python
pecan_count = data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"].value_counts()
print(pecan_count)
```

    Pecan    342
    Name: Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan, dtype: int64



```python
apple_isnull = p.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple"])
pumpkin_isnull = p.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin"])
pecan_isnull = p.isnull(data["Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan"])

pie_ate = apple_isnull & pumpkin_isnull & pecan_isnull
```


```python
print(pie_ate.value_counts())
```

    False    876
    True     182
    dtype: int64



```python
## Converting age to numeric
```


```python
ageData = data["Age"]
ageCounts = ageData.value_counts()
print(ageCounts)
```

    45 - 59    286
    60+        264
    30 - 44    259
    18 - 29    216
    Name: Age, dtype: int64



```python
def convertAgeToInt(ageStr) :
    if p.isnull(ageStr) : 
        return None
    ageStr = ageStr.split(" ")
    ageStr = ageStr[0]
    ageStr = ageStr.replace("+", "")
    return int(ageStr)
    
intAge = data["Age"].apply(convertAgeToInt)
data["int_age"] = intAge
print(data["int_age"].describe())
```

    count    1025.000000
    mean       39.383415
    std        15.398493
    min        18.000000
    25%        30.000000
    50%        45.000000
    75%        60.000000
    max        60.000000
    Name: int_age, dtype: float64



```python
## Findings :

* Total number of people preferring meat  = 39%
* 
```
