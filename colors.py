#!/usr/binenv python

from os import system
import curses

def init_colors():
	screen = curses.initscr()
	curses.start_color()
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
	# color pair 1 = red text on white bg