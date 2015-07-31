#!/usr/bin/env python

from os import system
import keyfunc
import curses
import colors

def get_param(prompt_string):
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, prompt_string)
	screen.refresh()
	input = screen.getstr(10, 10, 60)
	return input

#Here we store variables for remembering things! Yay! 
x = 0
global trackpadOff
trackpadOff =0
hibernate = 0
colors.init_colors()
screen = curses.initscr()
while x != ord('q'):
	screen = curses.initscr()
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, "Welcome to syscurse... Press q to Exit", curses.color_pair(5))
	screen.addstr(4, 4, ", - to decrease Volume", curses.color_pair(2))
	screen.addstr(5, 4, ". - to increase Volume", curses.color_pair(3))
	screen.addstr(6, 4, "    Current volume level: NaN")
	screen.addstr(7, 4, "d - Show disk space")
	if(trackpadOff):
		screen.addstr(8, 4, "t - Toggle trackpad. Current state: " + keyfunc.str_trackpad(trackpadOff), curses.color_pair(3))
	else:
		screen.addstr(8, 4, "t - Toggle trackpad. Current state: " + keyfunc.str_trackpad(trackpadOff), curses.color_pair(2))
	screen.addstr(4, 40, "f - Open Firefox", curses.color_pair(1))
	screen.addstr(5, 41, "c - Open Chrome")
	screen.addstr(9, 5, "s - Turn off screen that isn't real.", curses.color_pair(4))	
	if(hibernate == 0):
		screen.addstr(10, 8, "h - Hibernate computer.", curses.color_pair(3));
	
	if x ==ord('h' or hibernate == 1):
		hibernate = 1;
		screen.addstr(10,8, "Do you really want to hiberante? (y/n)", curses.color_pair(1));
		
		if(x == 'y'):
			keyfunc.hibernate()
		if(x == 'n'):
			hibernate = 0
	if x == ord('.'):
		keyfunc.inc_vol()
	if x == ord(','):
		keyfunc.dec_vol()
	if x == ord('d'):
		curses.endwin()
		keyfunc.execute_cmd_verbose("df -h")
	if x==ord('t'):
		trackpadOff = keyfunc.toggle_trackpad(trackpadOff)
	if x==ord('f'):
		keyfunc.open_firefox()
	if x==ord('c'):
		keyfunc.open_chrome()	
	if x==ord('s'):
		keyfunc.disable_VGA()	

	screen.refresh()
	x=screen.getch()
curses.endwin()
