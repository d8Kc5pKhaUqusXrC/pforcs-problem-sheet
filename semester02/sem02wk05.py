# sem02wk05.py
# A program to visualise COVID-19 County by County data in a heatmap
# Mark Brislane, G00398781

# This program uses data from the Irish Government COVID-19 Public Dataset :-
# COVID-19 HPSC County Statistics Historic Data
# https://data.gov.ie/en_GB/dataset/covid-19-hpsc-county-statistics-historic-data?package_type=dataset

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import the Data Set - if unable to use the latest online one due to an error, try the local version.
# Start to clean the data while importing, i.e. only read required columns &
# convert TimeStampDate to an actual datetime.
try:
    df = pd.read_csv(
        'https://opendata.arcgis.com/datasets/d9be85b30d7748b5b7c09450b8aede63_0.csv',
        usecols=[2, 4, 11],
        # nrows=1040,  # Read in 40 days (40 x 26) just for testing purposes
        parse_dates=['  TimeStamp']
    )
except:  # Something went wrong accessing the latest version.
    print("There was an issue accessing the online version of the COVID-19 data, trying a local versions...")
    try:  # Try the local cached version from 18/11 instead
        df = pd.read_csv(
            'COVID-19_HPSC_County_Statistics_Historic_Data.csv',
            usecols=[2, 4, 11],
            parse_dates=['TimeStamp']
        )
    except:
        print("There was an issue accessing the local version also. Ending program")
        raise

# Clean the data
# Convert the TimeStamp to a Date only, all the times are midnight anyway
df['TimeStamp'] = df['TimeStamp'].dt.date
# On some days, rows have duplicates for unknown reasons so remove them
df.drop_duplicates(inplace=True)
# Sort by Date ascending, then by County alphabetically - sometimes required depending on the data.
df.sort_values(by=['TimeStamp', 'CountyName'])
# PopulationProportionCovidCases is cumulative which makes no sense on a heatmap.
# Solution found here:
# https://stackoverflow.com/questions/62194100/how-to-convert-cumulative-data-to-daily-data-for-multiple-indexes-in-python
df['PopulationProportionCovidCases'] = df.groupby(['CountyName'])['PopulationProportionCovidCases']\
    .transform(lambda s: s.sub(s.shift().fillna(0)).abs())

# Create a pivot table of the data so we can create a heatmap from it.
df_pivoted = df.pivot('CountyName', 'TimeStamp', 'PopulationProportionCovidCases')

# yticklabels = 1 is so all the counties are listed on the Y axis.
ax = sns.heatmap(df_pivoted, yticklabels=1)
plt.xlabel('Date')
plt.ylabel('County')
plt.title('COVID-19 Daily Case Heatmap by County (normalised by population)')
plt.get_current_fig_manager().window.state('zoomed')  # Open full screen
plt.show()
