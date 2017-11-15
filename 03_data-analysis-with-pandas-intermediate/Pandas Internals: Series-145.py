## 1. Data Structures ##

import pandas as pd
fandango = pandas.read_csv("fandango_score_comparison.csv")
print(type(fandango))
print(fandango.head(2))

## 2. Integer Indexes ##

fandango = pd.read_csv('fandango_score_comparison.csv')
# column is taken out
series_film = fandango["FILM"]
print(type(series_film))
# column is taken out
series_rt = fandango["RottenTomatoes"]
print(type(series_rt))

## 3. Custom Indexes ##

# Import the Series object from pandas
from pandas import Series
#print(series_rt)
film_names = series_film.values
print(film_names)
rt_scores = series_rt.values
print(rt_scores)
series_custom = Series(rt_scores, index = film_names)

## 4. Integer Index Preservation ##

series_custom = Series(rt_scores , index=film_names)
series_custom[['Minions (2015)', 'Leviathan (2014)']]
# Assign the values in series_custom at indexes 5 through 10 to the variable fiveten. 
#Then, print fiveten to verify that you can still use integer values for selection.
fiveten = series_custom[5:11]
print(fiveten)

## 5. Reindexing ##

original_index = series_custom.index
print(type(original_index))

original_index_list = original_index.tolist()
sorted_index = sorted(original_index_list)
print("sorted_index is of type ", type(sorted_index))
sorted_by_index = series_custom.reindex(sorted_index)
print(sorted_by_index)

## 6. Sorting ##

sc2 = series_custom.sort_index()
sc3 = series_custom.sort_values()
print(sc2[0:10], sc3[0:10])

## 7. Transforming Columns With Vectorized Operations ##

rt_norm = fandango["RT_norm"]
print("RT_norm : ", rt_norm)
series_normalized = series_custom / 20
print("Normalized Series : ", series_normalized)

## 8. Comparing and Filtering ##

criteria_one = series_custom > 50
criteria_two = series_custom < 75
both_criteria = series_custom[criteria_one & criteria_two]

## 9. Alignment ##

rt_critics = Series(fandango['RottenTomatoes'].values, index=fandango['FILM'])
rt_users = Series(fandango['RottenTomatoes_User'].values, index=fandango['FILM'])

print(rt_critics, rt_users)

rt_mean = Series((rt_critics + rt_users)/2, index = fandango['FILM'])
print(rt_mean)