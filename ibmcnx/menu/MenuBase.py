'''
IBM Connections Jython script

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0

'''

# MenuBase.py - Common menu functions for IBM Connections CLI
import sys

# Global menu shortcuts
MENU_BACK = 'b'
MENU_QUIT = 'q'
MENU_HELP = 'h'

def handleCommonCommands(choice):
    """
    Handle common menu commands across all menus
    Returns: True if command was handled and should interrupt normal flow, False otherwise
    """
    if choice.lower() == MENU_QUIT:
        print "\nExiting the program...\n"
        sys.exit(0)
        return 1
    elif choice.lower() == MENU_HELP:
        printHelp()
        return 1
    elif choice.lower() == MENU_BACK:
        # We just return True, the caller will handle returning to main menu
        return 1
    return 0

def printHelp():
    """Display help for common menu commands"""
    print "\nCommon commands:"
    print "  %s - Go back to main menu" % MENU_BACK
    print "  %s - Quit the program" % MENU_QUIT
    print "  %s - Show this help\n" % MENU_HELP

def printMenuHeader(title):
    """Print standard menu header"""
    length=len(title)
    print("\n\n" + 70 * "-")
    print((70 - length)/2 * " " + title)
    print(70 * "-")
    print("\n")

def printMenuFooter():
    """Print common menu footer with shortcuts"""
    print "\n\t[%s]ack to main menu | [%s]uit | [%s]elp" % (MENU_BACK.upper(), MENU_QUIT.upper(), MENU_HELP.upper())

def printMainMenuFooter():
    """Print common menu footer with shortcuts"""
    print "\n\t\t\t[%s]uit | [%s]elp" % (MENU_QUIT.upper(), MENU_HELP.upper())
