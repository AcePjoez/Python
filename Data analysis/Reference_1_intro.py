import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')

web_stats = {'Day':[1, 2, 3, 4, 5, 6],                      # Making a Dictionary
             'Visitors':[43, 53, 34, 45, 64, 34],
             'Bounce_Rate':[65, 72, 62, 64, 54, 66]}

df = pd.DataFrame(web_stats)                                # Making a DataFrame of the Dictionary

print(df)                                                   # Printing the DataFrame
print(df.head())                                            # Printing the first 5 rows
print(df.tail())                                            # Printing the last 5 rows
print(df.tail(2))                                           # Printing the last 2 rows

print(df.set_index('Day'))                                  # Setting the index to 'day'
print(df.head())                                            # Index is gone

df = df.set_index('Day')                                    # One way of maintaining the index
print(df.head())

df.set_index('Day', inplace=True)                           # Second way of maintaining the index
print(df.head())

print(df['Bounce_Rate'])                                    # Printing one column in 2 ways
print(df.Visitors)

print(df[['Bounce_Rate', 'Visitors']])                      # Printing multiple columns

print(df.Visitors.tolist())                                 # Converting column to list
print(np.array(df[['Bounce_Rate', 'Visitors']]))            # Converting array to list

df2 = pd.DataFrame(np.array(df[['Bounce_Rate', 'Visitors']]))
print(df2)
