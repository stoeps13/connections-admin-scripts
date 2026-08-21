'''
Set all Roles to Restricted - no anonymous access possible

Description:
Script is tested with HCL Connections 5.0
You have to edit the variables and set them to your administrative Accounts

Author: Klaus Bild
Blog: http://www.kbild.ch
E-Mail:
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0

History:
2014-09-10    Christoph Stoettner    change the way for changing roles, 5.0 compatible
'''

import connections_admin.functions
import ConfigParser

configParser = ConfigParser.ConfigParser()
configFilePath = r'connections_admin/connections_admin.properties'
configParser.read(configFilePath)

answer = raw_input(
    'Do you want to set the j2ee roles with Users and Groups from connections_admin.properties? (Yes|No) ')
allowed_answer = ['yes', 'y', 'ja', 'j']

if answer.lower() in allowed_answer:
    # Get Admin Accounts and Groups for J2EE Roles
    connwasadmin = configParser.get('Generic', 'j2ee.cnxwasadmin')
    connadmin = configParser.get('Generic', 'j2ee.cnxadmin')
    connmoderators = configParser.get('Generic', 'j2ee.cnxmoderators')
    connmetrics = configParser.get('Generic', 'j2ee.cnxmetrics')
    connmobile = configParser.get('Generic', 'j2ee.connmobile')
    cnxmail = configParser.get('Generic', 'j2ee.cnxmail')
    cnxreader = configParser.get('Generic', 'j2ee.cnxreader')
    cnxcommunitycreator = configParser.get('Generic', 'j2ee.communitycreator')
    cnxwikicreator = configParser.get('Generic', 'j2ee.wikicreator')
    cnxfilesyncuser = configParser.get('Generic', 'j2ee.filesyncuser')
    # Variables for Groupmapping
    connadmingroup = configParser.get('Generic', 'j2ee.cnxadmingroup')
    connmoderatorgroup = configParser.get('Generic', 'j2ee.cnxmoderatorgroup')
    connmetricsgroup = configParser.get('Generic', 'j2ee.cnxmetricsgroup')
    connmobilegroup = configParser.get('Generic', 'j2ee.cnxmobilegroup')
    cnxmailgroup = configParser.get('Generic', 'j2ee.cnxmailgroup')
    cnxreadergroup = configParser.get('Generic', 'j2ee.cnxreadergroup')
    cnxcommunitycreatorgroup = configParser.get(
        'Generic', 'j2ee.communitycreatorgroup')
    cnxwikicreatorgroup = configParser.get('Generic', 'j2ee.wikicreatorgroup')
    cnxfilesyncusergroup = configParser.get(
        'Generic', 'j2ee.filesyncusergroup')
else:
    # Variables for Usermapping
    connwasadmin = str(connections_admin.functions.getAdmin('connwasadmin'))
    connadmin = str(connections_admin.functions.getAdmin('connadmin'))
    connmoderators = str(connections_admin.functions.getAdmin('connmoderators'))
    connmetrics = str(connections_admin.functions.getAdmin('connmetrics'))
    connmobile = str(connections_admin.functions.getAdmin('connmobile'))
    cnxmail = str(connections_admin.functions.getAdmin('cnxmail'))
    # Variables for Groupmapping
    connadmingroup = str(connections_admin.functions.getAdmin('connadmingroup'))
    connmoderatorgroup = str(connections_admin.functions.getAdmin('connmoderatorgroup'))
    connmetricsgroup = str(connections_admin.functions.getAdmin('connmetricsgroup'))
    connmobilegroup = str(connections_admin.functions.getAdmin('connmobilegroup'))
    cnxmailgroup = str(connections_admin.functions.getAdmin('cnxmailgroup'))


def setRoleCmd(appName, roleName, everyone, authenticated, users, groups):
    '''
    function to set the j2ee role of a Connections Application
    Values needed appName = Application Name, roleName = Name of the role
    everyone yes|no, authenticated yes|no, users single uid or uid1|uid2, groups like users
    '''
    print "\n\tApplication: " + appName
    print "\tRole: " + roleName
    print "\n\tEveryone: " + everyone
    print "\tAuthenticated: " + authenticated
    print "\tUsers: " + users
    print "\tGroups: " + groups + "\n"
    AdminApp.edit(appName, '[-MapRolesToUsers [[ "' + roleName + '" ' +
                  everyone + ' ' + authenticated + ' ' + users + ' ' + groups + ' ]] ]')
    # example: AdminApp.edit( "Blogs", '[-MapRolesToUsers [["person" No Yes ""
    # ""] ]]' )


def setRole(appName, roleName, connwasadmin, connadmin, connmoderators, connmetrics, connmobile, cnxmail, cnxreader, cnxcommunitycreator, cnxwikicreator, cnxfilesyncuser, connadmingroup, connmoderatorgroup, connmetricsgroup, connmobilegroup, cnxmailgroup, cnxreadergroup, cnxcommunitycreatorgroup, cnxwikicreatorgroup, cnxfilesyncusergroup):
    if roleName == "admin" or roleName == "search-admin" or roleName == "widget-admin" or roleName == "dsx-admin" or roleName == "trustedExternalApplication" or roleName == 'org-admin' or roleName == 'orgadmin':
        # Administration Roles
        setRoleCmd(appName, roleName, "No", "No", connwasadmin +
                   '|' + connadmin, connadmingroup)
    elif roleName == "administrator":
        # Mobile Administration
        setRoleCmd(appName, roleName, "No", "No", connmobile, connmobilegroup)
    elif roleName == "global-moderator":
        # Moderators
        setRoleCmd(appName, roleName, "No", "No",
                   connmoderators, connmoderatorgroup)
    elif roleName == "metrics-reader" or roleName == "metrics-report-run" or roleName == "community-metrics-run":
        # Metrics
        setRoleCmd(appName, roleName, "No", "No",
                   connmetrics, connmetricsgroup)
    elif roleName == "reader" or roleName == "person" or roleName == "allAuthenticated" or roleName == "everyone-authenticated" or roleName == "files-owner":
        # Default Access reader, person, authenticated
        if cnxreader == "allauthenticated":
            setRoleCmd(appName, roleName, "No", "Yes", "' '", "' '")
        else:
            setRoleCmd(appName, roleName, "No", "No",
                       cnxreader, cnxreadergroup)
    elif roleName == "mail-user":
        # Mail User
        if cnxmail == "allauthenticated":
            setRoleCmd(appName, roleName, "No", "Yes", "' '", "' '")
        else:
            setRoleCmd(appName, roleName, "No", "No",
                       cnxmail, cnxmailgroup)
    elif roleName == "everyone" or roleName == "Everyone":
        # Public to yes
        setRoleCmd(appName, roleName, "Yes", "No", "' '", "' '")
    elif roleName == "discussthis-user" or roleName == "Anonymous":
        # Public to yes
        setRoleCmd(appName, roleName, "Yes", "No", "' '", "' '")
    elif roleName == "bss-provisioning-admin" or roleName == "client manager":
        # Public to yes
        setRoleCmd(appName, roleName, "No", "No", "' '", "' '")
    elif roleName == "authenticated" or roleName == "Authenticated" or roleName == "OAuthClient":
        # Public to yes
        setRoleCmd(appName, roleName, "No", "Yes", "' '", "' '")
    elif roleName == "community-creator":
        # Community Creator
        if cnxmail == "allauthenticated":
            setRoleCmd(appName, roleName, "No", "Yes", "' '", "' '")
        else:
            setRoleCmd(appName, roleName, "No", "No",
                       cnxcommunitycreator, cnxcommunitycreatorgroup)
    elif roleName == 'wiki-creator':
        # Wiki Creator
        if cnxmail == "allauthenticated":
            setRoleCmd(appName, roleName, "No", "Yes", "' '", "' '")
        else:
            setRoleCmd(appName, roleName, "No", "No",
                       cnxwikicreator, cnxwikicreatorgroup)
    elif roleName == 'filesync-user':
        # Wiki Creator
        if cnxfilesyncuser == "allauthenticated":
            setRoleCmd(appName, roleName, "No", "Yes", "' '", "' '")
        else:
            setRoleCmd(appName, roleName, "No", "No",
                       cnxfilesyncuser, cnxfilesyncusergroup)
    else:
        print "\n\nApplication " + appName + "- Role " + roleName + " not set!\n\n"


def convertRoles2Dict(appname, list):
    # function to convert backup txt files of Security Role Backup to a dictionary
    # print '\tPATH: ' + path
    count = 0
    dict = {}

    for line in list.splitlines():
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

apps = AdminApp.list()
appsList = apps.splitlines()
# only for testing single apps, uncomment following line:
# appsList = ['fncs']

for app in appsList:
    dictionary = convertRoles2Dict(app, AdminApp.view(app, "-MapRolesToUsers"))
    print "\n\tApplication: " + app + "\n\n"
    # app, role
    for role in dictionary.keys():
        # Loop through Roles
        try:
            setRole(app, role, connwasadmin, connadmin, connmoderators, connmetrics, connmobile, cnxmail, cnxreader, cnxcommunitycreator, cnxwikicreator, cnxfilesyncuser,
                    connadmingroup, connmoderatorgroup, connmetricsgroup, connmobilegroup, cnxmailgroup, cnxreadergroup, cnxcommunitycreatorgroup, cnxwikicreatorgroup, cnxfilesyncusergroup)
        except:
            print "Error setting role: " + role + " in App: " + app

connections_admin.functions.saveChanges()
