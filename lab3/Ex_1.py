from lab3.graph import *

penColor(200, 113, 55)
penSize(1)
brushColor(200, 113, 55)

x = 250
y = 250
a = 50
b = 25
k = 1  # коэффициент наклона
x_o = - a
oval_cord_hight = []
oval_cord_low = []
for i in range(2 * a + 1):
    y_o = ((1 - (x_o ** 2) / (a ** 2)) * (b ** 2)) ** 0.5
    oval_cord_low.append([round(x + x_o), round(y + y_o)])
    oval_cord_hight.append([round(x + x_o), round(y - y_o)])
    x_o += 1


print(oval_cord_hight)
print(oval_cord_low)
polygon(oval_cord_hight)
polygon(oval_cord_low)
run()
