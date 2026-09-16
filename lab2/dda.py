import matplotlib.pyplot as plt

# Input points
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# Calculate dx and dy
dx = x2 - x1
dy = y2 - y1

# Calculate steps
steps = max(abs(dx), abs(dy))

# Calculate increments
x_inc = dx / steps
y_inc = dy / steps

# Starting point
x = x1
y = y1

# Store points
x_points = []
y_points = []

# DDA Algorithm
for i in range(steps + 1):
    x_points.append(round(x))
    y_points.append(round(y))

    x = x + x_inc
    y = y + y_inc

# Draw line
plt.plot(x_points, y_points, 'o')
plt.plot(x_points, y_points)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("DDA Line Drawing Algorithm")
plt.grid()
plt.show()

