'''
Set the Version Stamp to actual time and date

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0
'''

import connections_admin.functions

print "\nSet Version Stamp in LotusConnections-config.xml to actual Date and Time\n"

# Check properties if temppath is defined
if (connections_admin.functions.tempPath() == ''):
    path = raw_input("Path and Folder where config is temporarily stored: ")
else:
    path = connections_admin.functions.tempPath()

execfile("connectionsConfig.py")
LCConfigService.checkOutConfig(path, AdminControl.getCell())
LCConfigService.updateConfig("versionStamp", "")
LCConfigService.checkInConfig(path, AdminControl.getCell())
synchAllNodes()
