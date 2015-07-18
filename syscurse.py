#!/usr/bin/env python

from os import system
import curses

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
x = 0

while x != ord('q'):
     screen = curses.initscr()

     screen.clear()
     screen.border(0)
     screen.addstr(2, 2, "Welcome to syscurse...")
     screen.addstr(4, 4, ", to decrease Volume")
     screen.addstr(5, 4, ". to increase Volume")
     screen.addstr(6, 4, "Current volume level: ")
     screen.addstr(7, 4, "d - Show disk space")
     screen.addstr(8, 4, "q - Exit")
     screen.refresh()

     x = screen.getch()

     if x == ord('.'):
          curses.endwin()
          execute_cmd("amixer -D pulse sset Master 5%+")
     if x == ord(','):
          curses.endwin()
          execute_cmd("amixer -D pulse sset Master 5%-")
     if x == ord('d'):
          curses.endwin()
          execute_cmd_verbose("df -h")

curses.endwin()
