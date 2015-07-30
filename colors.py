#!/usr/binenv python

from os import system
import curses

def init_colors():
	screen = curses.initscr()
	curses.start_color()
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
	# color pair 1 = red text on white bg
	
	curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
