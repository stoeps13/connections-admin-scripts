'''
IBM Connections Jython script

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0

'''

import ibmcnx.menu.MenuBase as MenuBase
import ibmcnx.menu.menuAdm as menuAdm
import ibmcnx.menu.menuCfg as menuCfg
import ibmcnx.menu.menuChk as menuChk
import ibmcnx.menu.menuDoc as menuDoc
import ibmcnx.menu.menuSec as menuSec
import ibmcnx.menu.menuUsr as menuUsr
import sys

def menuMain():
    while 1:
        MenuBase.printMenuHeader("IBM WebSphere and HCL Connections Main Menu")
        
        print("\t\t\t[1] Configuration")
        print("\t\t\t[2] Security Roles")
        print("\t\t\t[3] Check/Monitoring")
        print("\t\t\t[4] User Profiles")
        print("\t\t\t[5] Administration")
        print("\t\t\t[6] Documentation")
        
        # Add common footer with shortcuts (but back isn't as useful in main menu)
        # You could use a different footer for the main menu if you prefer
        MenuBase.printMainMenuFooter()
        
        menuChoice = raw_input("\nPlease select a number: ")
        
        # Check for common commands first
        if MenuBase.handleCommonCommands(menuChoice):
            if menuChoice.lower() == MenuBase.MENU_BACK:
                # In main menu, "back" just redisplays the menu
                return
        else:
            # Process regular menu items
            try:
                if menuChoice == "1":
                    menuCfg.menuCfg()
                elif menuChoice == "2":
                    menuSec.menuSec()
                elif menuChoice == "3":
                    menuChk.menuChk()
                elif menuChoice == "4":
                    menuUsr.menuUsr()
                elif menuChoice == "5":
                    menuAdm.menuAdm()
                elif menuChoice == "6":
                    menuDoc.menuDoc()
                else:
                    print "\nInvalid selection. Please try again."
            except:
                import sys
                if sys.exc_info()[0] == SystemExit:
                    raise
                import traceback
                traceback.print_exc()
            
if __name__ == "__main__":
    menuMain()
