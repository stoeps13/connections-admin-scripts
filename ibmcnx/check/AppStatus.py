'''
  Description:   Show the status of all applications

  Author:        Christoph Stoettner
  Mail:          christoph.stoettner@stoeps.de
  Documentation: http://scripting101.stoeps.de

  Version:       8.0.14
  Date:          2026-08-21

  License:       Apache 2.0

'''

print "Getting application status of all installed applications..."

applications = AdminApp.list().splitlines()

runningApps = []
stoppedApps = []

for application in applications:
    applName = AdminControl.completeObjectName(
        'type=Application,name=' + application + ',*')
    if applName != '':
        aStatus = 'running'
        runningApps.append(application)
    else:
        aStatus = 'stopped'
        stoppedApps.append(application)

runningApps.sort()
stoppedApps.sort()

print ''
print '\tRUNNING APPLICATIONS: \n'
for app in runningApps:
    print '\t\t' + app

print ''
print '\tSTOPPED APPLICATIONS: \n'
for app in stoppedApps:
    print '\t\t' + app

print ''
