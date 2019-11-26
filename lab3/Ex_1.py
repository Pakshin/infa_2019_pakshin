from graph import *
from math import *

penColor(200, 113, 55)
penSize(1)
brushColor(200, 113, 55)

x = 250
y = 250
a = 50
b = 25
k = 90  # коэффициент наклона
k_rad = radians(k)
x_o = - a
oval_cord_hight = []
oval_cord_low = []
for i in range(2 * a + 1):

    x_pop = (fabs(x_o) - fabs(x_o) * cos(k_rad))
    y_pop = fabs(x_o) * sin(k_rad)

    y_o = ((1 - (x_o ** 2) / (a ** 2)) * (b ** 2)) ** 0.5
    if x_o <= 0:
        oval_cord_low.append([round(x + x_o + x_pop), round(y + y_o - y_pop)])
        oval_cord_hight.append([round(x + x_o + x_pop), round(y - y_o - y_pop)])
    else:
        oval_cord_low.append([round(x + x_o - x_pop), round(y + y_o + y_pop)])
        oval_cord_hight.append([round(x + x_o - x_pop), round(y - y_o + y_pop)])
    x_o += 1


polygon(oval_cord_hight)
polygon(oval_cord_low)
run()
