#!/bin/bash
# Converts us-counties.csv into harrisonburg.json and rockingham.json

function parse_nyt {
    ## Parses the New York Times's covid data us-counties.csv and creates a
    ## .json file for the specified county.
    ##
    ## USAGE:   parse_nyt (County,State) (County) (Filename)
    ##

    # Greps for COUNTY,STATE 
    cat us-counties.csv | grep -i "$1" > smaller_csv.csv 

    # Replace DATE,COUNTY,STATE,NUMBER,CASES,DEATHS with ["DATE",CASES]
    regex="s/([[:digit:]]+-[[:digit:]]+-[[:digit:]]+),[$2]+,Virginia,[[:digit:]]+,([[:digit:]]+),[[:digit:]]+/[\"\1\", \2],/ig"
    sed -r "$regex" smaller_csv.csv > temp.json 

    # Replace first [ with [[ to make it valid json 
    # The -i.bak is for OSX compatability
    sed -i.bak "1 s/^\[/[[/" temp.json && rm temp.json.bak 

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