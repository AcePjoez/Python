import pandas as pd

df = pd.read_csv('Tutorial.csv')                                                # reads from a csv file
print(df.head())
df.set_index('Date', inplace=True)
df.to_csv('Tutorial2.csv')                                                      # creates a csv file

df = pd.read_csv('Tutorial2.csv')
print(df.head())                                                                # index isn't saved

df = pd.read_csv('Tutorial2.csv', index_col=0)                                  # creates index
print(df.head())

df.columns = ['Austin_HPI']                                                     # Renames all columns
print(df.head())

df.to_csv('Tutorial3.csv')
df.to_csv('Tutorial4.csv', header=False)                                        # Removes headers

df = pd.read_csv('Tutorial4.csv', names=['Date', 'Austin_HPI'], index_col=0)    # Creates headers
print(df.head())

df.to_html('Tutorial.html')                                                     # Creates html

df = pd.read_csv('Tutorial4.csv', names=['Date', 'Austin_HPI'])
print(df.head())

df.rename(columns={'Austin_HPI':'77006_HPI'}, inplace=True)                     # Renames 1 column
print(df.head())