from file_utils import loadWithJSON
from covid_dataset import CovidDataset
import constants

# Dictionary of names of counties and corresponding filenames with county data.
# Edit update_county_data to analyze data from additional counties
files = {
    'Harrisonburg':'harrisonburg.json', 
    'Rockingham':'rockingham.json', 
    'Newport News':'newportnews.json',
    }

# Make dictionary with key="COUNTY_NAME" and value=COVID_DATASET_OBJECT
data = {}
for key in files:
    try:
        data[key] = CovidDataset(loadWithJSON(files[key]))
    except:
        print("\nFile %s does not exist" % (files[key]))
    
print('\nWhen was the first positive COVID cases in each county?\n')

for key in data:
    print("%s: %s" % (key, data[key].get_first_positive()))

print('\nWhat day was the maximum number of cases recorded in each county?\n')

for key in data:
    print("%s: %s" % (key, data[key].get_max_case_day()))

print('\nWhat was the worst week in each city/county for new COVID cases? '
      'When was the rise in cases the fastest over a seven day period?'
      '\n')

for key in data:
    print("%s: %s through %s" % (key, 
        data[key].get_worst_n_days(constants.DAYS_IN_WEEK)[0], 
        data[key].get_worst_n_days(constants.DAYS_IN_WEEK)[1]))

print('\n')