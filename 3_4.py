a = (float(input('Enter first number ')))
b = (float(input('Enter second number ')))
c = (float(input('Enter third number ')))
x = 0
print('Positives quantity: ', ((a > x), (b > x), (c > x)).count(True))
print('Negative quantity: ', ((a < x), (b < x), (c < x)).count(True))
print('Zeros: ', ((a == x), (b == x), (c == x)).count(True))
