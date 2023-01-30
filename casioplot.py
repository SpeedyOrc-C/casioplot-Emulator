"""
Do not put this file into your calculator.
"""

import typing
import sys

from plotaux import *

TYPE_COLOR_RETURN = tuple[int, int, int]
TYPE_COLOR = TYPE_COLOR_RETURN | list[int, int, int]
TYPE_SIZE = typing.Literal['small', 'medium', 'large']


class CasioPlot:
    buffer: list[list[TYPE_COLOR_RETURN]]
    FONT_MEDIUM: dict[str, list[list[int]]]
    HEIGHT: int
    WIDTH: int

    @staticmethod
    def move_cursor_top_left() -> None:
        """

        """
        sys_stdout_write('\033[H')


class CasioPlotChromatic(CasioPlot):
    """

    """

    def __init__(self):
        self.buffer = ...


class CasioPlotMonochrome(CasioPlot):
    """

    """
    HEIGHT = 64
    WIDTH = 128

    def __init__(self):
        self.buffer = [[COLOR_WHITE for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)]
        self.frame_top = '╭' + '─' * self.WIDTH * 2 + '╮\r\n'
        self.frame_side = '│'
        self.frame_bottom = '╰' + '─' * self.WIDTH * 2 + '╯\r\n'
        self.FONT_MEDIUM = {
            'A': [
                [0, 0, 1, 1, 1, 0],
                [0, 1, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 1],
                [0, 1, 1, 1, 1, 1],
                [0, 1, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0]
            ],
            'B': [
                [0, 1, 1, 1, 1, 0],
                [0, 1, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 1],
                [0, 1, 1, 1, 1, 0],
                [0, 1, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 1],
                [0, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0]
            ],
        }

    def show_screen(self) -> None:
        """

        """
        self.move_cursor_top_left()
        sys_stdout_write(self.frame_top)
        for y in range(self.HEIGHT):
            sys_stdout_write(self.frame_side)
            for x in range(self.WIDTH):
                r, g, b = self.buffer[y][x]
                if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
                    continue
                sys_stdout_write('██' if r >= 248 and g >= 252 and b >= 248 else '  ')
            sys_stdout_write(self.frame_side)
            sys_stdout_write('\r\n')
        sys_stdout_write(self.frame_bottom)

    def clear_screen(self) -> None:
        """

        """
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT):
                self.buffer[y][x] = COLOR_WHITE

    def set_pixel(self, x: int, y: int, color: TYPE_COLOR = COLOR_BLACK) -> None:
        """

        :param x:
        :param y:
        :param color:
        :return:
        """
        if x < 0 or x > 127 or y < 0 or y > 63:
            return
        r, g, b = color
        if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
            return
        self.buffer[y][x] = color

    def get_pixel(self, x: int, y: int) -> TYPE_COLOR_RETURN:
        """

        :param x:
        :param y:
        :return:
        """
        return self.buffer[x][y]

    def draw_string(
            self, x: int, y: int,
            content: str, color: TYPE_COLOR = (0, 0, 0),
            size: TYPE_SIZE = 'medium') -> None:
        """

        :param x:
        :param y:
        :param content:
        :param color:
        :param size:
        """
        match size:
            case 'small':
                chosen_font = self.FONT_MEDIUM
            case 'medium':
                chosen_font = self.FONT_MEDIUM

        for char_i, char in enumerate(content):
            bitmap = chosen_font[char]
            for char_y in range(8):
                for char_x in range(6):
                    if bitmap[char_y][char_x]:
                        set_pixel(x+char_x + 6 * char_i, y+char_y, color)


# Emulated functions
# Choose CasioPlotMonochrome for 9750 and 9860 series.
# Choose CasioPlotChromatic for CG series.
CHOSEN_PLATFORM = CasioPlotMonochrome()

show_screen = CHOSEN_PLATFORM.show_screen
clear_screen = CHOSEN_PLATFORM.clear_screen
set_pixel = CHOSEN_PLATFORM.set_pixel
get_pixel = CHOSEN_PLATFORM.get_pixel
draw_string = CHOSEN_PLATFORM.draw_string

sys_stdout_write = sys.stdout.write
