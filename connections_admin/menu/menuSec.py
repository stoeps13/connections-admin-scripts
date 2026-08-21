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

def menuSec():
    MenuBase.printMenuHeader("IBM WebSphere and HCL Connections Security Roles")
    
    print("\t[1] Backup J2EE Security foles (all apps)")
    print("\t[2] Restore J2EE Security foles (all apps)")
    print("\t[3] Set all apps to restricted (no unauthenticated access")
    print("\t[4] Set all apps to unrestricted (unauthenticated access")
    print("\t[5] Set Moderator roles")
    print("\t[6] Metrics Reader")
    print("\t[7] Metrics Report Run")
    print("\t[8] Mail Integration access")

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
                execfile("connections_admin/config/j2ee/RoleBackup.py", globals(), globals())
                return 1
            elif menuChoice == "2":
                execfile("connections_admin/config/j2ee/RoleRestore.py", globals(), globals())
                return 1
            elif menuChoice == "3":
                execfile("connections_admin/config/j2ee/RoleAllRestricted.py", globals(), globals())
                return 1
            elif menuChoice == "4":
                execfile("connections_admin/config/j2ee/RoleAllUnrestricted.py", globals(), globals())
                return 1
            elif menuChoice == "5":
                execfile("connections_admin/config/j2ee/RoleGlobalMod.py", globals(), globals())
                return 1
            elif menuChoice == "6":
                execfile("connections_admin/config/j2ee/RoleMetricsReader.py", globals(), globals())
                return 1
            elif menuChoice == "7":
                execfile("connections_admin/config/j2ee/RoleMetricsReportRun.py", globals(), globals())
                return 1
            elif menuChoice == "8":
                execfile("connections_admin/config/j2ee/RoleSocialMail.py", globals(), globals())
                return 1
            else:
                print "\nInvalid selection. Please try again."
                return 1
        except Exception:
            import sys
            exc_type, exc_value, exc_traceback = sys.exc_info()
            # print "Error: %s" % exc_value
            
