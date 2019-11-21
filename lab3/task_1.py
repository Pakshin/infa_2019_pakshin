from graph import *

def paint_circle(x, y, radius, penC, penS, brushC):
    penColor(penC)
    penSize(penS)
    brushColor(brushC)
    a = circle(x, y, radius)
    print(a)

def paint_line(x1, y1, x2, y2, penC, penS, brushC):
    penColor(penC)
    penSize(penS)
    brushColor(brushC)
    line(x1, y1, x2, y2)


paint_circle(250, 250, 150, "black", 2, "yellow")
paint_circle(190, 190, 30, "black", 1, "red")
paint_circle(190, 190, 15, "black", 1, "black")
paint_circle(310, 190, 25, "black", 1, "red")
paint_circle(310, 190, 10, "black", 1, "black")

paint_line(190, 310, 310, 310, "black", 20, "black")



run()