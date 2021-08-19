# pcost.py
#
# Exercise 1.31
def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        for line in f:
            try:
                row = line.split(',')
                total_cost += int(row[1]) * float(row[2])
            except ValueError:
                print("Couldn't parse", line)
    return total_cost

cost = portfolio_cost('Data/missing.csv')
print('Total cost', cost)
