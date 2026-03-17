'''
Title: EDA Felony Arrest
Author: Martin Ngoh
Date: 08/09/2024
'''

# Libraries
import pandas as pd
from functions import histplot

# Load data
df = pd.read_csv('../data/combined_cleaned_data.csv')

# Histplot
for x in df:
    histplot(data=df, variable=x, bins=10)