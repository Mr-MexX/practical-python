# pcost.py
#
# Exercise 1.27
total_cost = 0.0

with open('Data/portfolio.csv','rt') as f:
    headers = next(f).split(',')
    column_shares = headers.index('shares')
    # column_price = headers.index('price')
    for line in f:
        row = line.split(',')
        total_cost += int(row[column_shares]) * float(row[2])
    print('Total cost',total_cost)
