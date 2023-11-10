#!/usr/bin/python2.7
"""reducer for the hadoop project. gives top ten salaries from mapper output"""
import sys
import re

reduced_data = sys.stdin
top10 = []

for line in reduced_data:

    line = line.strip()
    line = re.split('\t|,', line)

    try:
        id, company, Salary = line

        if len(top10) < 10:
            top10.append((int(id), float(Salary), company))
        else:
            if float(Salary) > top10[-1][1]:
                top10.pop(-1)
                top10.append((int(id), float(Salary), company))
                top10.sort(key=lambda x: x[1], reverse=True)
    except Exception as e:
        continue

print("id\tSalary\tcompany")
for i in top10:
    print("{}\t{}\t{}".format(i[0], i[1], i[2]))
