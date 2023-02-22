# %%
import pandas as pd

# read the csv file
data = pd.read_csv("https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv")

# filter the dataframe to only include rows where the "name" column is equal to "Oliver" and year is between 1910 and 2015
filtered_data = data[(data["name"] == "Oliver") & (data["year"] >= 1910) & (data["year"] <= 2015)]

# sum the values in the "UT" column for all filtered years
total = filtered_data["UT"].sum()

print("Number of people named Oliver in Utah between 1910 and 2015:", total)

# %%
