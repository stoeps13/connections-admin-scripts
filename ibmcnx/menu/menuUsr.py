'''
IBM Connections Jython script

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0

'''

import os
import sys
import ibmcnx.menu.MenuBase as MenuBase
import ibmcnx.functions 

def menuUsr():
    MenuBase.printMenuHeader("IBM WebSphere and HCL Connections User Profiles")
    
    print("\t\t[1] Check ExID (all Apps & Profiles)")
    print("\t\t[2] Deactivate and activate a user in one step")
    print("\t\t[3] Deactivate by mail address")
    print("\t\t[4] Deactivate by UserId")
    print("\t\t[5] Sync ExID for all Users and Apps")

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
                execfile("ibmcnx/member/CheckExID.py")
                return 1
            elif menuChoice == "2":
                execfile("ibmcnx/member/DeactAndActByEmail.py")
                return 1
            elif menuChoice == "3":
                execfile("ibmcnx/member/InactivateByEmail.py")
                return 1
            elif menuChoice == "4":
                execfile("ibmcnx/member/InactivateByUid.py")
                return 1
            elif menuChoice == "5":
                execfile("ibmcnx/member/SyncAllByEXID.py")
                return 1
            else:
                print "\nInvalid selection. Please try again."
                return 1
        except Exception:
            import sys
            exc_type, exc_value, exc_traceback = sys.exc_info()
            # print "Error: %s" % exc_value
            

