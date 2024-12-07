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

# Load Files Into a DataFrame
import pandas as pd
import os

df = pd.read_csv("project_data.csv")

print(df)