#/usr/bin.env python
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
def inc_vol():#Increments the master volume by 5%
	curses.endwin()
	execute_cmd("amixer -D pulse sset Master 5%+")
	
def dec_vol():#Decrements the master volume by 5%
	curses.endwin()
	execute_cmd("amixer -D pulse sset Master 5%-")
	
def toggle_trackpad(trackpadOff):#Toggles the trackpad between on and off. Currently does not do so intelligently, assumes it is on and keeps track of toggling rather than sensing the current state.
	curses.endwin()
	if(trackpadOff == 0):
		execute_cmd("synclient TouchpadOff=1")
		return 1
	else:
		execute_cmd("synclient TouchpadOff=0")
		return 0
def disable_VGA():#Turns off VGA connection 
	curses.endwin()
	execute_cmd("xrandr --output VGA-1-2 --off")

def open_firefox():#Open firefox 
	execute_cmd("firefox")
def open_chrome():#Doesn't really work, but it tries to open chrome. 
	execute_cmd("google-chrome")
def hibernate():#Hibernate the computer? Maybe? Sudo??
	execute_cmd("sudo pm-hibernate")
