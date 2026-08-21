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

def menuDoc():
    MenuBase.printMenuHeader("IBM WebSphere and HCL Connections Documentation")
    
    print("\t\t[1] Show JVM Heap Sizes")
    print("\t\t[2] Show JVM Settings")
    print("\t\t[3] Show JVM Trace Settings")
    print("\t\t[4] Show SystemOut/SystemErr.log config")
    print("\t\t[5] Show all used ports")
    print("\t\t[6] Show all used variables")
    print("\t\t[7] Show all j2ee roles of installed apps")
    print("\t\t[8] Show all datasources and ds parameters")
    print("\t\t[9] Show users with employee.extended role") 
    print("\t\t[10] Show inactive user profiles")
    print("\t\t[11] Create a file with info of all points above")

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
                execfile("ibmcnx/doc/JVMHeap.py")
                return 1
            elif menuChoice == "2":
                execfile("ibmcnx/doc/JVMSettings.py")
                return 1
            elif menuChoice == "3":
                execfile("ibmcnx/doc/traceSettings.py")
                return 1
            elif menuChoice == "4":
                execfile("ibmcnx/doc/LogFiles.py")
                return 1
            elif menuChoice == "5":
                execfile("ibmcnx/doc/Ports.py")
                return 1
            elif menuChoice == "6":
                execfile("ibmcnx/doc/Variables.py")
                return 1
            elif menuChoice == "7":
                execfile("ibmcnx/doc/j2eeroles.py")
                return 1
            elif menuChoice == "8":
                execfile("ibmcnx/doc/DataSources.py")
                return 1
            elif menuChoice == "9":
                execfile("ibmcnx/doc/ProfRoleID.py")
                return 1
            elif menuChoice == "10":
                execfile("ibmcnx/doc/ProfilesInactive.py")
                return 1
            elif menuChoice == "11":
                execfile("ibmcnx/doc/Documentation.py")
                return 1
            else:
                print "\nInvalid selection. Please try again."
                return 1
        except Exception:
            import sys
            exc_type, exc_value, exc_traceback = sys.exc_info()
            # print "Error: %s" % exc_value
            
