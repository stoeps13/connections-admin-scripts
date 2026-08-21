'''
IBM Connections Jython script

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       8.0.14
Date:          2026-08-21

License:       Apache 2.0

'''

import os
import sys
import ibmcnx.menu.MenuBase as MenuBase
import ibmcnx.functions 

def menuChk():
    MenuBase.printMenuHeader("IBM WebSphere and HCL Connections Check Tasks")
    
    print("\t\t[1] Check if all applications are running")
    print("\t\t[2] Check database connections")
    print("\t\t[3] Check webserver")
    print("\t\t[4] Check SeedLists")

    # Add common footer with shortcuts (but back isn't as useful in main menu)
    # You could use a different footer for the main menu if you prefer
    MenuBase.printMenuFooter()
    
    menuChoice = raw_input("\nPlease select a number: ")
    
    # Check for common commands first
    if MenuBase.handleCommonCommands(menuChoice):
        if menuChoice.lower() == MenuBase.MENU_BACK:
            # In main menu, "back" just redisplays the menu
            return
        elif menuChoice.lower() == MenuBase.MENU_QUIT:
            sys.exit(0)
            
    else:
        # Process regular menu items
        try:
            if menuChoice == "1":
                execfile("ibmcnx/check/AppStatus.py")
                return 1
            elif menuChoice == "2":
                execfile("ibmcnx/check/DataSource.py")
                return 1
            elif menuChoice == "3":
                execfile("ibmcnx/check/WebSrvStatus.py")
                return 1
            elif menuChoice == "4":
                execfile("ibmcnx/SeedLists.py")
                return 1
            else:
                print "\nInvalid selection. Please try again."
                return 1
        except Exception:
            import sys
            exc_type, exc_value, exc_traceback = sys.exc_info()
            # print "Error: %s" % exc_value
            
