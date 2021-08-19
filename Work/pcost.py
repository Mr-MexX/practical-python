# pcost.py
#
# Exercise 1.32
def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0
    import csv
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

cost = portfolio_cost('Data/missing.csv')
print('Total cost', cost)

