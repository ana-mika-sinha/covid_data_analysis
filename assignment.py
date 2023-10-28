##########################################
#1. Import data set and necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cpy_df = pd.read_excel("owid-covid-data.xlsx")
df = cpy_df.copy()

##########################################
#2. Show the first 5 rows
df.head()


##########################################
#3. Show the basic summary of data
df.describe()
df,info()


##########################################
#4. Find total countries where total_deaths is greater than 1000000.
death_count_per_country = df.groupby('location', as_index=False).sum()
new_df = death_count_per_country[death_count_per_country["total_deaths"]>1000000]
print(len(new_df))

##########################################
#5. plot for total countries where total_deaths is greater than 1000000.
plt.figure(figsize=(8, 6))
plt.plot(new_df['location'], new_df['total_deaths'], marker='o', color='b', label='Total Deaths')
plt.xlabel('Countries')
plt.ylabel('Total Deaths')
plt.title('Total Deaths by Country')
plt.legend()
plt.show()


##########################################
#6. plot for numbers of cases Globally(total_cases, total_deaths, total_vaccinations) 
# vs Number of days since first suspect

new_df = df.copy()
# Convert 'date' column to datetime
new_df['date'] = pd.to_datetime(new_df['date'])

# Calculate the minimum date in the 'date' column
min_date = new_df['date'].min()

# Calculate the number of days since the minimum date and create a new column
new_df['days_since_first_suspect'] = (new_df['date'] - min_date).dt.days

df_world = new_df.groupby('days_since_first_suspect', as_index=False).sum()

plt.figure(figsize=(8, 6))
plt.plot(df_world['days_since_first_suspect'], df_world['total_cases'], marker='o', linestyle='', color='b', label='total_cases')
plt.plot(df_world['days_since_first_suspect'], df_world['total_deaths'], marker='o', linestyle='', color='r', label='total_deaths')
plt.plot(df_world['days_since_first_suspect'], df_world['total_vaccinations'], marker='o', linestyle='', color='g', label='total_vaccinations')
plt.xlabel('Number of days since first suspect')
plt.ylabel('Number of cases')
plt.title('World')
plt.legend()
plt.show()


##########################################
#7. plot for numbers of cases in Upper middle income bracket(total_cases, total_deaths, total_vaccinations) 
# vs Number of days since first suspect

new_df = df.copy()
#filter out entries that are for "Upper middle income" bracket
new_df=new_df[new_df["location"]=="Upper middle income"]

# Convert 'date' column to datetime
new_df['date'] = pd.to_datetime(new_df['date'])

# Calculate the minimum date in the 'date' column
min_date = new_df['date'].min()

# Calculate the number of days since the minimum date and create a new column
new_df['days_since_first_suspect'] = (new_df['date'] - min_date).dt.days

df_upper_middle_income = new_df.groupby('days_since_first_suspect', as_index=False).sum()

plt.figure(figsize=(8, 6))
plt.plot(df_upper_middle_income['days_since_first_suspect'], df_upper_middle_income['total_cases'], marker='o', linestyle='', color='b', label='total_cases')
plt.plot(df_upper_middle_income['days_since_first_suspect'], df_upper_middle_income['total_deaths'], marker='o', linestyle='', color='r', label='total_deaths')
plt.plot(df_upper_middle_income['days_since_first_suspect'], df_upper_middle_income['total_vaccinations'], marker='o', linestyle='', color='g', label='total_vaccinations')
plt.xlabel('Number of days since first suspect')
plt.ylabel('Number of cases')
plt.title('Upper middle income')
plt.legend()
plt.show()


##########################################
#8. plot for numbers of cases in High income bracket(total_cases, total_deaths, total_vaccinations) 
# vs Number of days since first suspect

new_df = df.copy()
#filter out entries that are for "High income" bracket
new_df=new_df[new_df["location"]=="High income"]

# Convert 'date' column to datetime
new_df['date'] = pd.to_datetime(new_df['date'])

# Calculate the minimum date in the 'date' column
min_date = new_df['date'].min()

# Calculate the number of days since the minimum date and create a new column
new_df['days_since_first_suspect'] = (new_df['date'] - min_date).dt.days

df_high_income = new_df.groupby('days_since_first_suspect', as_index=False).sum()

plt.figure(figsize=(8, 6))
plt.plot(df_high_income['days_since_first_suspect'], df_high_income['total_cases'], marker='o', linestyle='', color='b', label='total_cases')
plt.plot(df_high_income['days_since_first_suspect'], df_high_income['total_deaths'], marker='o', linestyle='', color='r', label='total_deaths')
plt.plot(df_high_income['days_since_first_suspect'], df_high_income['total_vaccinations'], marker='o', linestyle='', color='g', label='total_vaccinations')
plt.xlabel('Number of days since first suspect')
plt.ylabel('Number of cases')
plt.title('High income')
plt.legend()
plt.show()

##########################################
#9. plot for numbers of cases of Europe region(total_cases, total_deaths, total_vaccinations) 
# vs Number of days since first suspect

new_df = df.copy()
#filter out entries that belong to Europe
new_df=new_df[new_df["continent"]=="Europe"]

# Convert 'date' column to datetime
new_df['date'] = pd.to_datetime(new_df['date'])

# Calculate the minimum date in the 'date' column
min_date = new_df['date'].min()

# Calculate the number of days since the minimum date and create a new column
new_df['days_since_first_suspect'] = (new_df['date'] - min_date).dt.days

df_europe = new_df.groupby('days_since_first_suspect', as_index=False).sum()

plt.figure(figsize=(8, 6))
plt.plot(df_europe['days_since_first_suspect'], df_europe['total_cases'], marker='o', linestyle='', color='b', label='total_cases')
plt.plot(df_europe['days_since_first_suspect'], df_europe['total_deaths'], marker='o', linestyle='', color='r', label='total_deaths')
plt.plot(df_europe['days_since_first_suspect'], df_europe['total_vaccinations'], marker='o', linestyle='', color='g', label='total_vaccinations')
plt.xlabel('Number of days since first suspect')
plt.ylabel('Number of cases')
plt.title('Europe')
plt.legend()
plt.show()


##########################################
# 9. Group all countries where total_deaths is greater than 1000000.
new_df = df.copy()

##########################################
#10.group by location and sum up column values for each group
df_ = new_df.groupby('location', as_index=False).sum()
df_.loc[df_["total_deaths"]>1000000, ["location"]]


##########################################
#11. scatter plot for numbers of cases Globally(total_cases, total_deaths) 
# vs Number of days since first suspect

new_df = df.copy()

# Convert 'date' column to datetime
new_df['date'] = pd.to_datetime(new_df['date'])

# Calculate the minimum date in the 'date' column
min_date = new_df['date'].min()

# Calculate the number of days since the minimum date and create a new column
new_df['days_since_first_suspect'] = (new_df['date'] - min_date).dt.days

df_world = new_df.groupby('days_since_first_suspect', as_index=False).sum()

plt.figure(figsize=(8, 6))
plt.scatter(df_world['days_since_first_suspect'], df_world['total_cases'], marker='o', linestyle='', color='b', label='total_cases')
plt.scatter(df_world['days_since_first_suspect'], df_world['total_deaths'], marker='o', linestyle='', color='r', label='total_deaths')
plt.xlabel('Number of days since first suspect')
plt.ylabel('Number of cases')
plt.title('World')
plt.legend()
plt.show()

##########################################
# 12. How many dates we have in total where total_deaths is greater than 1000000
new_df = df.copy()

# Convert 'date' column to datetime
new_df['date'] = pd.to_datetime(new_df['date'])

# Calculate the minimum date in the 'date' column
min_date = new_df['date'].min()

# Calculate the number of days since the minimum date and create a new column
new_df['days_since_first_suspect'] = (new_df['date'] - min_date).dt.days

df_ = new_df.groupby('days_since_first_suspect', as_index=False).sum()

len(df_[df_["days_since_first_suspect"] > 1000000])

##########################################
# 13. plot for numbers of cases Globally(total_cases, total_deaths) 
# vs Number of days since first suspect

new_df = df.copy()

# Convert 'date' column to datetime
new_df['date'] = pd.to_datetime(new_df['date'])

# Calculate the minimum date in the 'date' column
min_date = new_df['date'].min()

# Calculate the number of days since the minimum date and create a new column
new_df['days_since_first_suspect'] = (new_df['date'] - min_date).dt.days

df_world = new_df.groupby('days_since_first_suspect', as_index=False).sum()

plt.figure(figsize=(8, 6))
plt.plot(df_world['days_since_first_suspect'], df_world['total_cases'], marker='o', linestyle='', color='b', label='total_cases')
plt.plot(df_world['days_since_first_suspect'], df_world['total_deaths'], marker='o', linestyle='', color='r', label='total_deaths')
plt.xlabel('Number of days since first suspect')
plt.ylabel('Number of cases')
plt.title('World')
plt.legend()
plt.show()


