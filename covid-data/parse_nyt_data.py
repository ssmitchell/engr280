import re
from file_utils import loadWithJSON

"""

Example:
    $ python parse_nyt_data.py "Harrisonburg city,Virginia" "harrisonburg.json"

"""

def ParseNytData(county_name, output_file): 
    """
    Translate us-counties.csv into output_file.json
    containing data from the specified county

    Args:
        county_name (str): County and state name as it appears
        in us-counties.csv (i.e. Harrisonburg city,Virginia)
        output_file (str): Name of file to save new data to
        (i.e. harrisonburg.json)

    Returns:
        None

    """

    # Open counties.csv for reading
    data = open('us-counties.csv', "r")

    # Open COUNTY_NAME.json for writing
    output = open(output_file, "w+")

    # Compile regular expression
    reg = re.compile(r"(\d+-\d+-\d+)," + county_name + r",\d+,(\d+),\d+")

    # First [ to make COUNTY_NAME.json valid json
    output.write("[")

    # Hacky way of making sure there's not an extra comma
    i = 0
    for line in data:
        match = reg.search(line)
        if match: # If line matches regex, write to new file in new format
            if i == 0:
                output.write(reg.sub("[\"" + match.group(1) + "\"," 
                + match.group(2) + "]", line))
                i = 1
            else:
                output.write(reg.sub(",[\"" + match.group(1) + "\"," 
                + match.group(2) + "]", line))

    # Last ] to make COUNTY_NAME.json valid json
    output.write("]")

    data.close()
    output.close()





if __name__ == "__main__":
    counties = loadWithJSON('counties.json')
    for i in counties:
        ParseNytData(i[1], i[2])