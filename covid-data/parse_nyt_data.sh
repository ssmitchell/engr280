#!/bin/bash
# Converts us-counties.csv into harrisonburg.json and rockingham.json

function parse_nyt {
    ## Parses the New York Times's covid data us-counties.csv and creates a
    ## .json file for the specified county.
    ##
    ## USAGE:   parse_nyt (County,State) (County) (Filename)
    ##

    # Greps for Harrisonburg city and Rockingham and puts lines 
    cat us-counties.csv | grep -i "$1" > smaller_csv.csv 

    # Replace 2020-03-22,Rockingham,Virginia,51165,2,0 with ["2020-03-22",2]
    sed -r "s/([[:digit:]]+-[[:digit:]]+-[[:digit:]]+),[$2]+,Virginia,[[:digit:]]+,([[:digit:]]+),[[:digit:]]+/[\"\1\", \2],/ig" smaller_csv.csv > temp.json 

    # Replace first [ with [[ to make it valid json
    sed -i.bak "1 s/^\[/[[/" temp.json && rm temp.json.bak # The -i.bak is for OSX compatability

    # Replace last , with a ] to make it valid json
    sed -i.bak "$ s/,$/]/" temp.json && rm temp.json.bak

    # Replace newlines with spaces to make it look nicer
    cat temp.json > "$3.json"

    # Removes temp files
    rm smaller_csv.csv temp.json

    printf "New file created $3.json\n"
}

parse_nyt "Harrisonburg city,Virginia" "Harrisonburg city" "harrisonburg" 

parse_nyt "Rockingham,Virginia" "Rockingham" "rockingham"