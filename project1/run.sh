#!/bin/sh

py main.py inspect --pdes 1P
py main.py inspect --name Halley
py main.py inspect --verbose --name Halley

py main.py query --date 1969-07-29
py main.py query --start-date 2020-01-01 --end-date 2020-01-31 --max-distance 0.025
py main.py query --start-date 2050-01-01 --min-distance 0.2 --min-velocity 50
py main.py query --date 2020-03-14 --max-velocity 25 --min-diameter 0.5 --hazardous
py main.py query --start-date 2000-01-01 --max-diameter 0.1 --not-hazardous
py main.py query --hazardous --max-distance 0.05 --min-velocity 30

