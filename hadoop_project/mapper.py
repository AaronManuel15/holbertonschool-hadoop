#!/usr/bin/python2.7
"""mapper for hadoop project to print out the contents of the csv file
being passed in from the hadoop streaming job. Commented lines are used for
matching the tasks output"""
import sys

data = sys.stdin
# count = 0

for line in data:
    # count += 1
    # if count == 16:
    #     break
    line = line.split(',')
    print("{}\t{},{}".format(line[0], line[1], line[3]))
