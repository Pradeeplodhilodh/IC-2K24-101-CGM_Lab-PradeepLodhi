import math

x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))

value = float(input("Enter value of x: "))

h = x[1] - x[0]
u = (value - x[0]) / h

d1 = y[1] - y[0]
d2 = y[2] - 2*y[1] + y[0]
d3 = y[3] - 3*y[2] + 3*y[1] - y[0]

result = y[0] + u*d1 + (u*(u-1)/2)*d2 + \
         (u*(u-1)*(u-2)/6)*d3

print("Interpolated value =", result)