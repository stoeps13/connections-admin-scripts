'''
Restore of J2EE Security Roles

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Author:        Martin Leyrer
Mail:          leyrer@gmail.com
Documentation: http://scripting101.stoeps.de

Version:       8.0.14
Date:          2026-08-21

License:       Apache 2.0

History:
20150307  Martin Leyrer       Added/fixed/enhanced documentation and app output.
                              Added error handling & summary output
                              Added error handling for WAS errors
                              Moved 'saveChanges' to end of script instead of "after each app"
'''

import os
import sys
import ibmcnx.functions
import com.ibm.ws.scripting.ScriptingException

# Restore Security Role from Textfile (created with RoleBackup.py)

path = raw_input(
    "Path and Folder where the files from RoleBackup.py are stored: ")
ibmcnx.functions.checkBackupPath(path)


def convertFile2Dict(appname, path):
    # function to convert backup txt files of Security Role Backup to a dictionary
    # print '\tPATH: ' + path
    filename = path + '/' + appname + ".txt"
    myfile = open(filename, 'r')

    count = 0
    dict = {}

    for line in myfile.readlines():
        # for loop through file to read it line by line
        if (':' in line) and (count > 12):
            value = line.split(':')[0]
            # cred = line.split(':')[1].strip('\n')
            cred = line.split(':')[1]
            # cred = cred.strip(' ')
            cred = cred.strip()
            if value == "Role":
                role = cred
                dict[role] = {}
            dict[role][value] = cred
        count += 1
    return dict


def setSecurityRoles(dictionary, appName):
    strRoleChange = '['
    for role in dictionary.keys():
        # Loop through Roles
        strRoleChange += '[\"' + role + '\" '
        strRoleChange += dictionary[role]['Everyone?'] + ' '
        strRoleChange += dictionary[role]['All authenticated?'] + ' '
        strRoleChange += '\"' + dictionary[role]['Mapped users'] + '\" '
        strRoleChange += '\"' + dictionary[role]['Mapped groups'] + '\" '
        strRoleChange += '\"' + dictionary[role]['All authenticated in trusted realms?'] + '\"] '
    strRoleChange += ']]'
    AdminApp.edit(appName, '[-MapRolesToUsers' + strRoleChange + ']')
    print "Setting Roles and Users for %s" % appName

apps = AdminApp.list()
appsList = apps.splitlines()
# Test with some Apps:
# appsList = ['Blogs','Activities','Wikis']
# or Single App:
# appsList = ['Blogs']
sure = raw_input('Are you sure? All roles will be overwritten! (Yes|No) ')
allowed_answer = ['yes', 'y', 'ja', 'j']

if sure.lower() in allowed_answer:
    restoreOK = []
    restoreERROR = {}
    for app in appsList:
        try:
            appDict = convertFile2Dict(app, path)
            setSecurityRoles(appDict, app)
            restoreOK.append(app)
        except IOError, e:
            restoreERROR[app] = e
        except com.ibm.ws.scripting.ScriptingException, e:
            restoreERROR[app] = e
        except:
            restoreERROR[app] = "Uncaught error: " + sys.exc_info()[0]

    ibmcnx.functions.saveChanges()

    print "\nSecurity Role restore went OK for:"
    for app in restoreOK:
        print "\t%s" % app
    if(len(restoreERROR) > 0):
        print "\nNO Security Role restore for:"
        for app in restoreERROR.keys():
            print "\t" + app + "\n\t\tReason: " + str(restoreERROR[app])

else:
    print 'Restore canceled!'
