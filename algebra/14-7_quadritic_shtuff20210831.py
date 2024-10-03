# 14-7 Quadratic Functions, #27 and #30, 8/31/2021
# To graph two parabolas on the same scale in order to see 
#  the effects of changing coefficients a, b and c in 
#  quadratic functions, CYeC wrote:

import matplotlib.pyplot as plt

print("Y e-value-ator")
A = float(input("Put A:"))
B = float(input("Put B:"))
C = float(input("Put C:"))
print("X   Y")
for x in range(-10,100):
    y = (A * x * x) + (B * x) + C
    print(x, y)

X = [i-10 for i in range(21)]
#X = [i-10 for i in range(101)]
Y = [A*(i**2)+B*i+C for i in X]

A2 = float(input("Put A2:"))
B2 = float(input("Put B2:"))
C2 = float(input("Put C2:"))
print("X2  Y2")
for xx in range(-10,100):
    y = (A2 * xx * xx) + (B2 * xx) + C2
    print(xx, y)

#X2 = [i-10 for i in range(21)]
X2 = [i-10 for i in range(101)]
Y2 = [A2*(i**2)+B2*i+C2 for i in X2]

print(X)
print(Y)
print(X2)
print(Y2)

ax = plt.gca()

plt.plot(X, Y, label="Y1")
plt.xlabel("nerd")
plt.plot(X2, Y2, label="Y2")
plt.ylabel("bird")
ax.grid(True)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.legend()
plt.show()
