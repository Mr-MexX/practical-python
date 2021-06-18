# bounce.py
#
# Exercise 1.5
height = 100 # 100m start height
num_bounce = 1
while num_bounce < 11:
    height = round(height * 3/5, 4)
    num_bounce = num_bounce + 1
    print(num_bounce, end = ' ')
    print(height)
