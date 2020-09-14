import re

def parse_nyt_data(county_name, output_file): 

    data = open('us-counties.csv', "r")
    output = open(output_file, "w+")
    reg = re.compile(r"(\d+-\d+-\d+)," + county_name + r",\d+,(\d+),\d+")

    output.write("[")
    i = 0
    for line in data:
        match = reg.search(line)
        if match:
            if i == 0:
                output.write(reg.sub("[\"" + match.group(1) + "\"," + match.group(2) + "]", line))
                i = 1
            else:
                output.write(reg.sub(",[\"" + match.group(1) + "\"," + match.group(2) + "]", line))
    output.write("]")

parse_nyt_data("Harrisonburg city,Virginia", "harrisonburg.json")
parse_nyt_data("Rockingham,Virginia", "rockingham.json")