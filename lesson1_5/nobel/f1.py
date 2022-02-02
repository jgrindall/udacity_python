import json
import helper
import pathlib


"""
This program will print out information about Nobel prizes (in any format you'd like). 

If a year is specified (not None), only print information about Nobel prizes from that year. 

If a category is specified (not None), only print information about Nobel prizes from that category.

$ python3 nobel.py
...
$ python3 nobel.py --year 2020
...
$ python3 nobel.py --category Physics
...
$ python3 nobel.py --year 1901 --category Economics
...
"""
    
def filter_year(prizes, year):
    return list(filter(lambda p:p["year"] == year, prizes))
    
def filter_cat(prizes, category):
    return list(filter(lambda p:p["category"] == category, prizes))

def load_nobel_prizes(filename='prizes.json'):
    with open(filename, 'r') as file:
        return json.load(file)

def main(year, category):
    data = load_nobel_prizes()
    prizes = data["prizes"]
    if year and category:
        print(filter_cat(filter_year(prizes, year), category))
    elif year:
        print(filter_year(prizes, year))
    elif category:
        print(filter_cat(prizes, category))
    


parser = helper.build_parser()
args = parser.parse_args()
main(args.year, args.category)