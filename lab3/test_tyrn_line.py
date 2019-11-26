from graph import *
from math import *

x = 250
y = 250
a = 100
b = 25
k = 0  # угол поворота
k_rad = radians(k)
p = []
x_0 = -a
y_0 = 0

for i in range(2 * a + 1):
    y_0 = 0
    x_pop = (fabs(x_0) - fabs(x_0) * cos(k_rad))
    y_pop = fabs(x_0) * sin(k_rad)
    if x_0 <= 0:
        p.append([x + x_0 + x_pop, y + y_0 - y_pop])
    else:
        p.append([x + x_0 - x_pop, y + y_0 + y_pop])

    x_0 += 1

polyline(p)

run()