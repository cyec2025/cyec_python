# 14-7 Graphing Absolute Value Functions, #31, 9/2/2021
# CYeC wrote, for -10 <= x <= 10, the following:

import matplotlib.pyplot as plt

print("Absolute Radiance!")
A = float(input("Put A:"))
B = float(input("Put B:"))
C = float(input("Put C:"))
print("X   Y")
for x in range(-10,10):
    y = abs((A * x) + B) + C
    print(x, y)

X = [i-10 for i in range(21)]
Y = [abs((A*i)+B)+C for i in X]

print(X)
print(Y)

ax = plt.gca()

plt.plot(X, Y, label="Y1")
plt.xlabel("nerd")
plt.ylabel("bird")
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.show()
