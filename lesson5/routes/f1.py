import csv
import json

import helper

ext = "dat"

"""
$ python3 routes.py SFO BOS
$ python3 routes.py SFO BOS --max-segments 3
"""

def read_airlines(filename='airlines.' + ext):
    airlines = {}  # Map from code -> name
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            airlines[line[4]] = line[1]
    return airlines


def read_airports(filename='airports.' + ext):
    # Return a map of code -> name
    airports = {}
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            airports[line[4]] = line[1]
    return airports


def read_routes(filename='routes.' + ext):
    # Return a map from source -> list of destinations
    routes = {}
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            source = line[2]
            dest = line[4]
            if source not in routes:
                routes[source] = []
            if dest not in routes[source]:
                routes[source].append(dest)
    return routes


def find_paths_helper(routes, dest, max_segments, current_path):
    source = current_path[-1]
    if len(current_path) == max_segments + 1:
        if source == dest:
            return [current_path]
        return []
        
    neighbours = routes.get(source, [])
    paths = []
    for n in neighbours:
        if n in current_path:
            continue
        extended_path = current_path.copy()
        extended_path.append(n)
        if n == dest:
            paths.append(extended_path.copy())
        else:
            paths += find_paths_helper(routes, dest, max_segments, extended_path)
    return paths

def find_paths(routes, source, dest, max_segments):
    return find_paths_helper(routes, dest, max_segments, [source])

def rename_path(path, airports):
    return tuple(map(airports.get, path))


def main(source, dest, max_segments):
    airlines = read_airlines()
    airports = read_airports()
    routes = read_routes()
    paths = find_paths(routes, source, dest, max_segments)
    output = {}
    for path in paths:
        key = len(path)
        if key in output:
            output[key].append(path)
        else:
            output[key] = [path]
    with open('output.json', 'w') as outfile:
        json.dump(output, outfile, indent=4, sort_keys=True)
        

if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.source, args.dest, args.max_segments)
