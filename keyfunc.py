#!/usr/bin.env python
from os import system
import curses


###############
#Operational functions
###############

def get_param(prompt_string):
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, prompt_string)
	screen.refresh()
	input = screen.getstr(10, 10, 60)
	return input

def execute_cmd_verbose(cmd_string):
	system("clear")
	a = system(cmd_string)
	print ""
	if a == 0:
		print "Command executed correctly"
	else:
		print "Command terminated with error"
	raw_input("Press enter")
	print ""

def execute_cmd(cmd_string):
	system("clear")
	a=system(cmd_string);
def str_trackpad(trackpadOff):
	if(trackpadOff):
		return "Off"
	else:
		return "On"
##############
#Actual key function
##############
def inc_vol():
	curses.endwin()
	execute_cmd("amixer -D pulse sset Master 5%+")
	
def dec_vol():
	curses.endwin()
	execute_cmd("amixer -D pulse sset Master 5%-")
	
def toggle_trackpad(trackpadOff):
	curses.endwin()
	if(trackpadOff == 0):
		execute_cmd("synclient TouchpadOff=1")
		return 1
	else:
		execute_cmd("synclient TouchpadOff=0")
		return 0


def open_firefox():
	execute_cmd("firefox")
def open_chrome():
	execute_cmd("google-chrome")


