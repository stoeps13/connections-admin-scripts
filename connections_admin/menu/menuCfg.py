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

def menuCfg():
    MenuBase.printMenuHeader("IBM WebSphere and HCL Connections Configuration Tasks")
    
    print("\t\t[1] Configure DataSources (Tuning)")
    print("\t\t[2] Set JVM Heap Sizes (Tuning)")
    print("\t\t[3] Set SystemOut and SystemErr Log Size")
    print("\t\t[4] Set Log language to english")
    print("\t\t[5] AppServer Monitoring Policy")
    print("\t\t[6] Set Custom Cache Parameter")
    print("\t\t[7] Set JVM Trace Settings")
    print("\t\t[8] Set WebSession Timeout")
    print("\t\t[9] Disable x-powered-by header") 
    print("\t\t[10] Set CookiesSameSite")
    print("\t\t[11] Change DB server and port")
    print("\t\t[12] Create new Cluster members")
    print("\t\t[13] Synchronize all nodes")

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
                execfile("connections_admin/config/DataSources.py", globals(), globals())
                return 1
            elif menuChoice == "2":
                execfile("connections_admin/config/JVMHeap.py", globals(), globals())
                return 1
            elif menuChoice == "3":
                execfile("connections_admin/config/LogFiles.py", globals(), globals())
                return 1
            elif menuChoice == "4":
                execfile("connections_admin/config/JVMLanguage.py", globals(), globals())
                return 1
            elif menuChoice == "5":
                execfile("connections_admin/config/MonitoringPolicy.py", globals(), globals())
                return 1
            elif menuChoice == "6":
                execfile("connections_admin/config/JVMCustProp.py", globals(), globals())
                return 1
            elif menuChoice == "7":
                execfile("connections_admin/config/jvmtrace.py", globals(), globals())
                return 1
            elif menuChoice == "8":
                execfile("connections_admin/config/WebSessionTO.py", globals(), globals())
                return 1
            elif menuChoice == "9":
                execfile("connections_admin/config/WebContainerSec.py", globals(), globals())
                return 1
            elif menuChoice == "10":
                execfile("connections_admin/security/cookiesamesite.py", globals(), globals())
                return 1
            elif menuChoice == "11":
                execfile("connections_admin/config/ChgDBHost.py", globals(), globals())
                return 1
            elif menuChoice == "12":
                execfile("connections_admin/config/addNode.py", globals(), globals())
                return 1
            elif menuChoice == "13":
                nodelist = AdminTask.listManagedNodes().splitlines()
                cell = AdminControl.getCell()
                for nodename in nodelist:
                    print "Syncronizing node " + nodename + " -",
                    try:
                        repo = AdminControl.completeObjectName(
                            'type=ConfigRepository,process=nodeagent,node=' + nodename + ',*')
                        AdminControl.invoke(repo, 'refreshRepositoryEpoch')
                        sync = AdminControl.completeObjectName(
                            'cell=' + cell + ',node=' + nodename + ',type=NodeSync,*')
                        AdminControl.invoke(sync, 'sync')
                        print " completed "
                    except Exception:
                        print " error"
            else:
                print "\nInvalid selection. Please try again."
                return 1
        except Exception:
            import sys
            exc_type, exc_value, exc_traceback = sys.exc_info()
            # print "Error: %s" % exc_value
            

