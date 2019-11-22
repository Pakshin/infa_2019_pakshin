from graph import *

canvasSize(600, 800)
windowSize(600, 800)

def paint_rectangle(x1, y1, x2, y2, penS, penC, brushC):
    penSize(penS)
    penColor(penC)
    brushColor(brushC)
    return rectangle(x1, y1, x2, y2)

def paint_circle(x, y, r, penS, penC, brushC):
    penSize(penS)
    penColor(penC)
    brushColor(brushC)
    return circle(x, y, r)

def elips(x,y,r1,r2):


house_color = (85, 85, 0)
ground_color = (128, 102, 0)
window_color_1 = (213, 255, 230)
window_color_2 = (135, 205, 222)
cat_color = (200, 113, 55)
ears_color = (222, 170, 135)
eyes_color = (136, 170, 135)
clew_color = (153, 153, 153)


house = paint_rectangle(0, 0, 600, 400, 1, house_color, house_color)
groud = paint_rectangle(0, 400, 600, 800, 1, ground_color, ground_color)
window_big = paint_rectangle(350, 50, 550, 350, 1, window_color_1, window_color_1)
window_small = paint_rectangle(360, 60, 540, 340, 1, window_color_2, window_color_2)
window_big_part_1 = paint_rectangle(440, 60, 460, 340, 1, window_color_1, window_color_1)
window_big_part_2 = paint_rectangle(360, 215, 540, 245, 1, window_color_1, window_color_1)
cat_tail = paint_circle(550, 600, 100, 1, "black", cat_color)

print(coords(cat_tail))
changeCoords(cat_tail, ((449, 449), (651, 529)))

run()