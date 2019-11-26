from graph import *

from graph import rectangle, brushColor, penColor, canvasSize, windowSize

house_color = (85, 85, 0)
ground_color = (128, 102, 0)
window_color_1 = (213, 255, 230)
window_color_2 = (135, 205, 222)
cat_color = (200, 113, 55)
ears_color = (222, 170, 135)
eyes_color = (136, 170, 135)
clew_color = (153, 153, 153)


def paint_window(x, y, window_width, window_height, window_color_1, window_color_2):
    penColor(window_color_1)
    brushColor(window_color_1)
    rectangle(x, y, (x + window_width), (y + window_height))
    penColor(window_color_2)
    brushColor(window_color_2)
    rectangle((x + window_width / 10), (y + window_height / 10), (x + window_width - window_width / 10), \
              (y + window_height - window_height / 10))
    penColor(window_color_1)
    brushColor(window_color_1)
    rectangle(x, (y + window_height / 3), (x + window_width), (y + window_height / 3 + window_height / 10))
    rectangle((x + window_width/2 - window_width/20), y, (x + window_width/2 + window_width/20), (y + window_height))


def paint_tail(x, y, size, direction):
    pass


def paint_body(x, y, size, direction):
    pass


def paint_legs(x, y, size, direction):
    pass


def paint_head(x, y, size, direction):
    pass


def paint_cat(x, y, size, direction):
    """
    :param x: координата центра туловища
    :param y: координата центра туловища
    :param size: ширина туловища
    :param direction: left/right - направление головы
    """

    paint_tail(x, y, size, direction)
    paint_body(x, y, size, direction)
    paint_legs(x, y, size, direction)
    paint_head(x, y, size, direction)


def paint_clew(x, y, size, direction):
    pass


def paint_ground(canvas_width, canvas_height):
    penColor(ground_color)
    brushColor(ground_color)
    rectangle(0, canvas_height / 2, canvas_width, canvas_height)


def paint_house(canvas_width, canvas_height):
    penColor(house_color)
    brushColor(house_color)
    rectangle(0, 0, canvas_width, canvas_height / 2)


def paint_pictire(canvas_width, canvas_height):
    canvasSize(canvas_width, canvas_height)
    windowSize(canvas_width, canvas_height)
    paint_ground(canvas_width, canvas_height)
    paint_house(canvas_width, canvas_height)
    paint_window(320, 20, canvas_width / 3 , canvas_height / 2 * 0.75, (213, 255, 230), (135, 205, 222))

    # paint_cat(x, y, size, direction)
    # paint_clew(x, y, size, direction)

paint_pictire (600, 800)

run()
