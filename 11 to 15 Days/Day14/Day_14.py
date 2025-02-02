################################## Day 14: 69 Days of Python #####################################

# Pandas
# Pandas is a Python library.
# Pandas is used to analyze data.
# Pandas is used to manipulate data.
# Pandas is used to create dataframes.
# Pandas is used to read and write data from/to Excel files.
# Pandas is used to read and write data from/to CSV files.

# Install Pandas
# pip install pandas

# Import Pandas
import pandas as pd

# Create a DataFrame
data = {'Name': ['Tom', 'Nick', 'John'],
    'Age': [20, 21, 19]}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Pandas Series
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
# Labels

print(myvar[0])

# Create Labels
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)


# Key/Value Objects as Series
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

# DataFrames
import pandas as pd

data = {"calories": [420, 380, 390],
        "duration": [50, 40, 45]}

myvar = pd.DataFrame(data)

print(myvar)

# Locate Row
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar["day1"]) 
# Named Indexes

print(myvar)

# Read CSV Files
import pandas as pd

# df = pd.read_csv("Day14/project_data.csv")

print(df.to_string()) 

# max_rows

import pandas as pd

# df = pd.read_csv("Day14/project_data.csv", max_rows=5)

print(pd.options.display.max_rows)


# Read JSON Files
import pandas as pd

# df = pd.read_json("Day14/projects.json")

print(df.to_string())

# Analyzing DataFrames
import pandas as pd
import numpy as np

# df = pd.read_csv("Day14/project_data.csv")
print(df.head())

# Empty Cells
# Remove Rows

import pandas as pd

# df = pd.read_csv("Day14/project_data.csv")

new_df = df.dropna()

print(new_df.to_string())

# Replace Empty Values

import pandas as pd

# df = pd.read_csv("Day14/project_data.csv")

df.fillna(130, inplace = True)

print(df.to_string())

# Convert Into a Correct Format

import pandas as pd

# df = pd.read_csv("Day14/project_data.csv")

# df["Date"] = pd.to_datetime(df["submission_datetime"])

print(df.to_string())

# Replacing Values

import pandas as pd
import numpy as np

# df = pd.read_csv("Day14/project_data.csv")


df.loc[7, 'Duration'] = 45

print(df.to_string())

# Removing Duplicates

import pandas as pd

df = pd.read_csv("Day14/data.csv")
df.drop_duplicates(inplace=True)
df.corr()
print(df.to_string())


# Plotting

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Day14/data.csv")

# df.plot()

# plt.show()

# Scatter Plot
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Day14/data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

# plt.show()

# Histogram
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Day14/data.csv')

df.plot(kind = 'hist', x = 'Duration')

plt.show()

''' Next Topic SciPy ---> Day_15 '''