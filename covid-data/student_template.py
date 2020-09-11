from file_utils import loadWithJSON


## Will load all Harrisonburg and Rockingham data into a list of lists
## Each element in the main list will contain a list of two items, the str:date and int:cases
harrisonburg_data = loadWithJSON('harrisonburg.json')
rockingham_data = loadWithJSON('rockingham.json')

## Print all elements in the list as an example
for data in harrisonburg_data:
    date = data[0]
    cases = data[1]
    print('On '+date + ' there were '+ str(cases) +' cases in Harrisonburg')

print('When was the first positive COVID case in Rockingham County and Harrisonburg?')

print('What day was the maximum number of cases recorded in Harrisonburg and Rockingham County?')

print('What was the worst week in the city/county for new COVID cases? '
      'When was the rise in cases the fastest over a seven day period?')