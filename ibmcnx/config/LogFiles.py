'''
Configure JVM Log Files

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0
'''

import ibmcnx.appServer

WS1 = ibmcnx.appServer.WasServers()

print "\nChanging the SystemOut & SystemErr log file rotation settings\n"

maxLogSize = 0

rolloverType = raw_input('\tRolloverType (SIZE, TIME, BOTH): ')

if rolloverType.upper() == 'BOTH' or rolloverType.upper() == 'B' or rolloverType.upper() == 'S' or rolloverType.upper() == 'SIZE':
	maxLogSize = int(raw_input('\tMax Logfile size in MB (1-50): '))

maxLogHistory = int(raw_input('\tMax Number of Backup Files (1-200): '))

servers = WS1.AllServers

for server in servers:
#    try:

    nodename = server.split('(')[1].split('/')[3]
    servername = server.split('(')[1].split('/')[5].split('|')[0]

    if len(nodename) < 10:
        tab = '\t\t\t'
    elif len(nodename) > 10 and len(nodename) < 15:
        tab = '\t\t'
    else:
        tab = '\t'

    # Print Node- and Servername
    print "\tChange log setting for: " + nodename + tab + servername

    # output and errorStream
    systemOut = AdminConfig.showAttribute(server, 'outputStreamRedirect')
    systemErr = AdminConfig.showAttribute(server, 'errorStreamRedirect')

    if rolloverType == 'BOTH' or rolloverType.upper() == 'B':
        logSetting = '[[rolloverType BOTH] [rolloverSize ' + str(
            maxLogSize) + '] [rolloverPeriod 24] [maxNumberOfBackupFiles ' + str(maxLogHistory) + ']]'
    elif rolloverType == 'TIME' or rolloverType.upper() == 'T':
        logSetting = '[[rolloverType TIME] [rolloverPeriod 24] [maxNumberOfBackupFiles ' + str(maxLogHistory) + ']]'
    elif rolloverType =='SIZE' or rolloverType.upper() == 'S':
        logSetting = '[[rolloverType SIZE][rolloverSize ' + \
            str(maxLogSize) + \
            '] [maxNumberOfBackupFiles ' + str(maxLogHistory) + ']]'
    else:
	print "\tError setting Logfile. Select BOTH, SIZE or TIME"

    # modify settings for log Size and History
    AdminConfig.modify(systemOut, logSetting)
    AdminConfig.modify(systemErr, logSetting)

#    except:
#        print "Error on setting Log File Size"

# Save Configuration
ibmcnx.functions.saveChanges()
print '\n\n'
