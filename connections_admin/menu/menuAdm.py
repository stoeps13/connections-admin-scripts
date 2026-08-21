'''
IBM Connections Jython script

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0

'''

import os
import sys
import connections_admin.menu.MenuBase as MenuBase
import connections_admin.functions

def menuAdm():
    MenuBase.printMenuHeader("IBM WebSphere and HCL Connections Administration Tasks")

    print("\t\t[1] Update VersionStamp in LCC")
    print("\t\t[2] Edit Files Policies")
    print("\t\t[3] Work with Libraries")
    print("\t\t[4] Show Library Sizes")
    print("\t\t[5] List libraries with more than 80% used space")
    print("\t\t[6] Reparent/Move Communities")
    print("\t\t[7] Add employee.extended role to user")

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
                execfile("connections_admin/cnx/VersionStamp.py")
                return 1
            elif menuChoice == "2":
                execfile("connections_admin/cnx/FilesPolicies.py")
                return 1
            elif menuChoice == "3":
                execfile("connections_admin/cnx/LibraryPolicies.py")
                return 1
            elif menuChoice == "4":
                execfile("connections_admin/cnx/LibrarySizes.py")
                return 1
            elif menuChoice == "5":
                execfile("connections_admin/cnx/LibrarySizeOverview.py")
                return 1
            elif menuChoice == "6":
                execfile("connections_admin/cnx/CommunitiesReparenting.py")
                return 1
            elif menuChoice == "7":
                execfile("connections_admin/cnx/ProfilesAddExtRole.py")
                return 1
            else:
                print "\nInvalid selection. Please try again."
                return 1
        except Exception:
            import sys
            exc_type, exc_value, exc_traceback = sys.exc_info()
            # print "Error: %s" % exc_value

