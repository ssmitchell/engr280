from file_utils import loadWithJSON
from covid_dataset import CovidDataset
import constants

## Will load all Harrisonburg and Rockingham data into a list of lists
## Each element in the main list will contain a list of two items, the 
## str:date and int:cases
harrisonburg_data = loadWithJSON('harrisonburg.json')
rockingham_data = loadWithJSON('rockingham.json')

harrisonburg_dataset = CovidDataset(harrisonburg_data)
rockingham_dataset = CovidDataset(rockingham_data)

print('\n\nWhen was the first positive COVID case in Rockingham County and'
    ' Harrisonburg?\n\nHarrisonburg: %s\nRockingham County: %s\n' %
    (harrisonburg_dataset.get_first_positive(), 
    rockingham_dataset.get_first_positive()))

print('What day was the maximum number of cases recorded in Harrisonburg'
' and Rockingham County?\n\nHarrisonburg: %s\nRockingham County: %s\n' %
    (harrisonburg_dataset.get_max_case_day(), 
    rockingham_dataset.get_max_case_day()))

print('What was the worst week in the city/county for new COVID cases? '
      'When was the rise in cases the fastest over a seven day period?'
      '\n\nHarrisonburg: %s through %s\nRockingham County: %s through %s\n' % 
      (harrisonburg_dataset.get_worst_n_days(constants.DAYS_IN_WEEK)[0], 
      harrisonburg_dataset.get_worst_n_days(constants.DAYS_IN_WEEK)[1], 
      rockingham_dataset.get_worst_n_days(constants.DAYS_IN_WEEK)[0], 
      rockingham_dataset.get_worst_n_days(constants.DAYS_IN_WEEK)[1]))