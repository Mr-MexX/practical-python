# pcost.py
#
# Exercise 1.33
import sys

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    import csv
    total_cost = 0.0

    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows) # optional print
    print(headers)
    for row in rows:
        try:
            total_cost += int(row[1]) * float(row[2])
            print(row) # optional print
        except ValueError:
            print("Couldn't parse", row)
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)

