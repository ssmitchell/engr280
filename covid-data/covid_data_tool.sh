#!/bin/bash
#
# Updates county file if it has been longer than 24 hours since the last one
# has been downloaded; Splits data for Harrisonburg city and Rockingham
# county into own separate csv files and then uses regular expressions
# and sed to convert csvs into valid json.

# If the timestamp file doesn't exist, creates it with a value of 0
if [[ ! -f last_timestamp ]] ; then
    echo "0" > last_timestamp
fi

# Reads last time data was downloaded
old_time=`cat last_timestamp`

# Reads current time
now_time=`date +%s`

# Checks if it has been more than 24 hours since data was last downloaded
if [ `(echo "$now_time-$old_time") | bc` -gt 86400 ] # 86400 seconds in 24 hours
then
    printf "\nGreater than 24 hours since last update. Downloading new data... \n\n"

    # Download new data into a csv
    curl https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv > us-counties.csv
    date +%s > last_timestamp

    # Greps for Harrisonburg city and Rockingham and puts lines 
    cat us-counties.csv | grep -i "Harrisonburg city" > harrisonburg-city.csv
    cat us-counties.csv | grep -i "Rockingham,Virginia" > rockingham.csv

    # Replace 2020-03-22,Rockingham,Virginia,51165,2,0 with ["2020-03-22",2]
    sed -r "s/([[:digit:]]+-[[:digit:]]+-[[:digit:]]+),[Rockingham|Harrisonburg city]+,Virginia,[[:digit:]]+,([[:digit:]]+),[[:digit:]]+/[\"\1\", \2],/ig" rockingham.csv > rockingham_temp.json
    # Replace first [ with [[ to make it valid json
    sed -i "1 s/^\[/[[/" rockingham_temp.json
    # Replace last , with a ] to make it valid json
    sed -i "$ s/,$/]/" rockingham_temp.json
    # Replace newlines with spaces to make it look nicer
    tr '\n' ' ' < rockingham_temp.json > rockingham.json
    # Remove temp file

    # Repeat above process for Harrisonburg city
    sed -r "s/([[:digit:]]+-[[:digit:]]+-[[:digit:]]+),[Rockingham|Harrisonburg city]+,Virginia,[[:digit:]]+,([[:digit:]]+),[[:digit:]]+/[\"\1\", \2],/ig" harrisonburg-city.csv > harrisonburg_temp.json
    sed -i "1 s/^\[/[[/" harrisonburg_temp.json
    sed -i "$ s/,$/]/" harrisonburg_temp.json
    tr '\n' ' ' < harrisonburg_temp.json > harrisonburg.json

    # Removes temp files
    rm harrisonburg-city.csv rockingham.csv rockingham_temp.json harrisonburg_temp.json us-counties.csv

    printf "\nNew files created\n\n"
else
    printf "\nData is up to date\n\n"
fi

# Runs python tool

../env/bin/python student_template.py