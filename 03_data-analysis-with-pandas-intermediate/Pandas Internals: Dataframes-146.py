## 1. Shared Indexes ##

import pandas as pd
fandango = pd.read_csv("fandango_score_comparison.csv")
print(fandango.head(2))
print(fandango.index)

## 2. Using Integer Indexes to Select Rows ##

fandango = pd.read_csv('fandango_score_comparison.csv')
# First five rows
fandango[0:5]
# From row at 140 and higher
fandango[140:]
# Just row at index 50
fandango.iloc[50]
# Just row at index 45 and 90
fandango.iloc[[45,90]]
# Just first and last row
first_last = fandango.iloc[[0,-1]]

## 3. Using Custom Indexes ##

fandango = pd.read_csv('fandango_score_comparison.csv')
print(type(fandango))
fandango_films = fandango.set_index('FILM', drop=False)
print(fandango_films.index)

## 4. Using a Custom Index for Selection ##

# Slice using either bracket notation or loc[]
fandango_films["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]
fandango_films.loc["Avengers: Age of Ultron (2015)":"Hot Tub Time Machine 2 (2015)"]

# Specific movie
fandango_films.loc['Kumiko, The Treasure Hunter (2015)']

# Selecting list of movies
movies = ['Kumiko, The Treasure Hunter (2015)', 'Do You Believe? (2015)', 'Ant-Man (2015)']
fandango_films.loc[movies]

# Select the following movies from fandango_films (in the order in which they appear), and assign them to best_movies_ever:
# "The Lazarus Effect (2015)"
# "Gett: The Trial of Viviane Amsalem (2015)"
# "Mr. Holmes (2015)"
movies = ["The Lazarus Effect (2015)", "Gett: The Trial of Viviane Amsalem (2015)", "Mr. Holmes (2015)"]
best_movies_ever = fandango_films.loc[movies]

## 5. Apply() Logic Over the Columns in a Dataframe ##

import numpy as np

# returns the data types as a Series
types = fandango_films.dtypes

# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
print(type(float_columns))
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]

# `x` is a Series object representing a column
deviations = float_df.apply(lambda x: np.std(x))

print(deviations)

## 6. Apply() Logic Over Columns: Practice ##

double_df = float_df.apply(lambda x: x*2)
print(double_df.head(1))
halved_df = float_df.apply(lambda x: x/2)
print(halved_df.head(1))

## 7. Apply() Over Dataframe Rows ##

rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_deviations = rt_mt_user.apply(lambda x: np.std(x), axis=1)
print(rt_mt_deviations[0:5])
rt_mt_means = rt_mt_user.apply(lambda x: np.mean(x), axis=1)
print(rt_mt_means)