'''
Title: functions.py
Author: Martin Ngoh
Date: 08/09/2024
'''

# Imports
import matplotlib.pyplot as plt
import seaborn as sns

# Histogram
def histplot(data, variable, bins=10, color='skyblue'):
    sns.set(style="whitegrid")
    sns.histplot(data[variable], bins=bins, kde=False, color=color)  # Use data[variable] to select the column
    plt.title(f'Histogram for {variable}', fontsize=16)
    plt.xlabel(variable, fontsize=14)  # Label with the variable name
    plt.ylabel('Frequency', fontsize=14)
    plt.show()

# Groupby Statements
def gp_by(df, var1, var2, metric='mean'):
    if metric == 'mean':
        value = df.groupby(var1)[var2].mean()
    elif metric == 'median':
        value = df.groupby(var1)[var2].median()
    elif metric == 'sum':
        value = df.groupby(var1)[var2].sum()
    elif metric == 'count':
        value = df.groupby(var1)[var2].count()
    else:
        print('Error: Incorrect Metric Passed')
    print(value.sort_values(ascending=False))