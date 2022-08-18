a = (float(input('Enter a ')))
b = (float(input('Enter b ')))
c = (float(input('Enter c ')))
x = 0
print('Positives quantity: ', ((a > x), (b > x), (c > x)).count(True))
print('Negative quantity: ', ((a < x), (b < x), (c < x)).count(True))
print('Zeros: ', ((a == x), (b == x), (c == x)).count(True))
