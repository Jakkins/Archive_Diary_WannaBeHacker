#!/usr/bin/env python3

# python3 -m pip install simple-term-menu

# sudo password
# nome interfaccia

# select interface name
# try to guess
# add manually

from simple_term_menu import TerminalMenu
from scan import scan as scanExternal

# 0, 1, 2
menu = [
"Scan the area",
"entry 2",
"entry 3"
]

tm = TerminalMenu(menu,
                title="AutomAirCrack",
                cycle_cursor=True,
                clear_screen=True)
tm_chosen = tm.show()

def scan(): scanExternal()
def bho1(): print("You typed bho1.")
def bho2(): print("You typed bho2.")

options = {
    0 : scan,
    1 : bho1,
    2 : bho2,
}

options[tm_chosen]()
