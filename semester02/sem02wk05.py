# sem02wk05.py
# A program to analyse data from
# Mark Brislane, G00398781

# This program uses data from the Irish Government COVID-19 Public Dataset :-
# COVID-19 HPSC County Statistics Historic Data
# https://opendata.arcgis.com/datasets/d9be85b30d7748b5b7c09450b8aede63_0.csv


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import the Data Set
# Start to clean the data while importing, i.e. only read required columns &
# convert TimeStampDate to an actual datetime.
df = pd.read_csv(
    'https://opendata.arcgis.com/datasets/d9be85b30d7748b5b7c09450b8aede63_0.csv',
    usecols=[2, 4, 11],
    parse_dates=['TimeStamp']
    # nrows=1040  # Read in 40 days (40 x 26) just for testing purposes
)

# Clean the data
# Convert the TimeStamp to a Date only, all the times are midnight anyway
df['TimeStamp'] = df['TimeStamp'].dt.date
# PopulationProportionCovidCases is cumulative which makes no sense on a heatmap.
# Solution found here:
# https://stackoverflow.com/questions/62194100/how-to-convert-cumulative-data-to-daily-data-for-multiple-indexes-in-python
df['PopulationProportionCovidCases'] = df.groupby(['CountyName'])['PopulationProportionCovidCases']\
    .transform(lambda s: s.sub(s.shift().fillna(0)).abs())

# Create a pivot table of the data so we can
df_pivoted = df.pivot('CountyName', 'TimeStamp', 'PopulationProportionCovidCases')

# yticklabels = 1 is so all the counties are listed on the Y axis.
sns.heatmap(df_pivoted, yticklabels=1)
plt.xlabel('Date')
plt.ylabel('County')
plt.title('COVID-19 Daily Case Heatmap by County (normalised by population)')
plt.show()
