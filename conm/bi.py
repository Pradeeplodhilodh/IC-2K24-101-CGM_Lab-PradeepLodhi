#11111backward interpolation

import math

x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))

value = float(input("Enter value of x: "))

h = x[1] - x[0]
u = (value - x[-1]) / h

d1 = y[3] - y[2]
d2 = y[3] - 2*y[2] + y[1]
d3 = y[3] - 3*y[2] + 3*y[1] - y[0]

result = y[-1] + u*d1 + (u*(u+1)/2)*d2 + (u*(u+1)*(u+2)/6)*d3

print("Interpolated value =", result)



# 22222forward interpolation, we use the formula:

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

#3333newton divided difference method

x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))

value = float(input("Enter value of x: "))

# First divided differences
d1 = (y[1] - y[0]) / (x[1] - x[0])
d2 = (y[2] - y[1]) / (x[2] - x[1])
d3 = (y[3] - y[2]) / (x[3] - x[2])

# Second divided differences
d12 = (d2 - d1) / (x[2] - x[0])
d23 = (d3 - d2) / (x[3] - x[1])

# Third divided difference
d123 = (d23 - d12) / (x[3] - x[0])
#Newton Divided Difference formula
result = y[0] + \
         (value - x[0]) * d1 + \
         (value - x[0]) * (value - x[1]) * d12 + \
         (value - x[0]) * (value - x[1]) * (value - x[2]) * d123

print("Interpolated value =", result)

# 
# 
# 44444lagrange interpolation method
x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))

value = float(input("Enter value of x: "))

# Lagrange terms
L0 = ((value - x[1]) * (value - x[2]) * (value - x[3])) / \
     ((x[0] - x[1]) * (x[0] - x[2]) * (x[0] - x[3]))

L1 = ((value - x[0]) * (value - x[2]) * (value - x[3])) / \
     ((x[1] - x[0]) * (x[1] - x[2]) * (x[1] - x[3]))

L2 = ((value - x[0]) * (value - x[1]) * (value - x[3])) / \
     ((x[2] - x[0]) * (x[2] - x[1]) * (x[2] - x[3]))

L3 = ((value - x[0]) * (value - x[1]) * (value - x[2])) / \
     ((x[3] - x[0]) * (x[3] - x[1]) * (x[3] - x[2]))

# Lagrange interpolation
result = y[0]*L0 + y[1]*L1 + y[2]*L2 + y[3]*L3

print("Interpolated value =", result)