import pandas as pd
from file_utils import saveWithJSON,saveWithPickle

def parse_nyt_data(harrisonburg_data,rockingham_data):
    print("Begin reading a long file...")

    # read the whole file into DataFrame
    df = pd.read_csv("us-counties.csv", header=0)

    print("Done reading...Now iterating...")
    # trim the header row
    df.head(1)

    # iterate over the DataFrame to build it out. There is surely a better way to do this...
    for it in df.iterrows():
        series = it[1]
        date = series['date']  # this data will be a literal string!
        county = series['county']
        state = series['state']
        cases = series['cases']

        if county == 'Rockingham' and state == 'Virginia':
            data = (date, cases)  # turn the data into a tuple
            rockingham_data.append(data)

        elif county == 'Harrisonburg city' and state == 'Virginia':
            data = (date, cases)  # turn the data into a tuple
            harrisonburg_data.append(data)


if __name__ == "__main__":

    # create two lists to hold tuples of data ('date','cases')
    harrisonburg_data = list()
    rockingham_data = list()

    parse_nyt_data(harrisonburg_data,rockingham_data)

    saveWithJSON('harrisonburg.json',harrisonburg_data,)
    saveWithJSON('rockingham.json',rockingham_data,)

    print("Done reading a really long file...Bonus points for making this faster....")

    print('When was the first positive COVID case in Rockingham County and Harrisonburg?')

    print('What day was the maximum number of cases recorded in Harrisonburg and Rockingham County?')

    print('What was the worst week in the city/county for new COVID cases? '
          'When was the rise in cases the fastest over a seven day period?')
