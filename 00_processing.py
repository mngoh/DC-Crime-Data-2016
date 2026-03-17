'''
Title: Processing of felony arrest charges in DC for the year 2016
Author: Martin Ngoh 
Date: 08/09/2024
'''

# Load Libraries 
import pandas as pd
from functions import gp_by

# Load Data Frame
df_arrest = pd.read_csv('Felony_Arrest_Charges_in_2016.csv')
df_incidents = pd.read_csv('Felony_Crime_Incidents_in_2016.csv')

# Rename all columns lowercase
df_arrest.columns = [x.lower() for x in df_arrest]
df_incidents.columns = [x.lower() for x in df_incidents]

# Combine the data
df = pd.merge(df_arrest, df_incidents, on='ccn')
# Drop the ys
df = df.drop(columns=[x for x in df if '_y' in x], axis=1)
# Remove the _x
df.columns = [x[:-2] if '_x' in x else x for x in df.columns]

# Drop Columns Not Needed: editor, edited, creator, created, person_type, year,
df = df.drop(columns=['editor', 'edited', 'creator', 'created', 'year', 'top_charge', 'person_type'], axis=1)

# Nas
#print(df.isna().sum())

# Unique Values
for x in df:
    result = df[x].value_counts()
    if len(result) < 20:
        print(result)

# Save Out DF
df.to_csv('combined_cleaned_data.csv', index=False)