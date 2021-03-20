# sessionid.py
#
# An introduction to Pandas
#
# To find which sessionId downloaded the most data
# 1. Read the access.log into a dataframe (see lab)
# 2. Set the date time to be the index (you will need to manipulate this data, see lab)
# 3. Use regular expressions to extract the session id from the URLs and store them in a different column
#    (use the apply function, see lab)
# 4. Use groupBy to get the sum of all the data downloaded by each sessionId.
# 5. Create a plot of this (type of your choice)
#
#  Extra:
#  Work out the amount of data each sessionId downloaded in any given day
#
# author: Mark Brislane
# date: 2021/03/19

import pandas as pd
import re
import matplotlib.pyplot as plt

# 1. Read the access.log into a dataframe

# File to open
# filename = "access.log"
filename = "small_access.log"

# Open the file for reading, error if it can't be found
try:
    file = open(filename, 'r', encoding='utf8')
except FileNotFoundError:
    print("The file " + filename + " was not found.")
    sys.exit(1)

# Add meaningful column names
colNames = ('ip',
            'dash',
            'user',
            'time',
            'request',
            'status code',
            'size of response',
            'referer',
            'user agent',
            'dunno'
            )

# Read the file into a dataframe, delimiter is " "
df = pd.read_csv(file, sep=' ', header=None, names=colNames)

# 2. Set the date time to be the index

# Remove the [ & ] from the time
df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())
# Convert time to a proper datetime timestamp
df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')
# Finally set the time column as the index, inplace otherwise will create a new df as the return object
df.set_index('time', inplace=True)


# 3. Use regular expressions to extract the session id from the URLs and store them in a different column

def extract_sessionid(x):
    wibble = re.search('(JSESSIONID=\S+)', x).group()
    id = re.split('=', wibble)[1]
    return id


df['sessionid'] = df['request'].apply(extract_sessionid)

# 4. Use groupBy to get the sum of all the data downloaded by each sessionId.
# Assistance from https://realpython.com/pandas-groupby/

print(df.groupby(by=['sessionid'])['size of response'].sum())

# 5. Create a plot of this (type of your choice)
# Assistance from https://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot

plt.figure(figsize=(8, 8))

plotdata = df.groupby(by=['sessionid'])[['size of response']].sum()
plotdata['size of response'].plot(kind='bar')
# Set the plot labels
plt.title("Data downloaded by SessionID")
plt.xlabel("SessionID")
plt.ylabel("Data downloaded (bytes)")
# Show the graph
plt.show()

#  Extra:
#  Work out the amount of data each sessionId downloaded in any given day

# meh