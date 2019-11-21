from graph import *

canvasSize(600, 800)
windowSize(600, 800)

def paint_rectangle(x1, y1, x2, y2, penS, penC, brushC):
    penSize(penS)
    penColor(penC)
    brushColor(brushC)
    rectangle(x1, y1, x2, y2)

paint_rectangle(0, 0, 600, 400, 1, "Brown", "Brown")
paint_rectangle(0, 400, 600, 800, 1, "Dark goldenrod", "Dark goldenrod")
paint_rectangle(350, 50, 550, 350, 1, "Aqua", "Aqua")
paint_rectangle(360, 60, 540, 340, 1, "Blue", "Blue")


run()