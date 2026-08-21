'''
Functions for HCL Connections Community Scripts

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.org


License:       Apache 2.0

Collection of functions
'''

import os
import sys
import ConfigParser

# Function to get the DataSource ID


def getDSId(dbName):
    try:
        DSId = AdminConfig.getid('/DataSource:' + dbName + '/')
        return DSId
    except:
        print "Error when getting the DataSource ID!"
        pass

# Function to check for a filepath and create it, when not present


def checkBackupPath(path):
    try:
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise

# Function for Set Roles Script


def getAdmin(adminvar):
    # function to ask for adminusers
    # return a list with admins
    # function is called for each admin type and each admin group type
    admins = []
    admin = ''
    adminstring = ''
    admindict = {
        'connwasadmin': 'Local WebSphere AdminUser',
        'connadmin': 'LDAP WebSphere and Connections AdminUser (searchAdmin)',
        'connmoderators': 'Moderator User',
        'connmetrics': 'Metrics Admin',
        'connmobile': 'Mobile Administrators',
        'connadmingroup': 'LDAP Admin Group',
        'connmoderatorgroup': 'Moderators Admin Group',
        'connmetricsgroup': 'Metrics Admin Group',
        'connmobilegroup': 'Mobile Admin Group'
    }
    print 'Type 0 when finished, uid is case sensitiv!'
    while admin != "0":
        admin = raw_input('Type uid for ' + admindict[adminvar] + ': ')
        if admin != '0' and admin != '':
            admins.append(admin)
    adminstring = '|'.join(admins)
    print adminstring
    return adminstring

# Function to synchronize all Nodes


def synchAllNodes():
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
        except:
            print " error"

    print ""

# Function to save changes only when necessary


def saveChanges():
    if (AdminConfig.hasChanges()):
        answer_save = raw_input('Do you really want to save these changes? ')
        allowed_answer_save = ['yes', 'y', 'ja', 'j']
        if answer_save.lower() in allowed_answer_save:
            print "\n\nSaving changes!\n"
            AdminConfig.save()

            # Synchronize Nodes after Save
            configParser = ConfigParser.ConfigParser()
            configFilePath = r'ibmcnx/ibmcnx.properties'
            configParser.read(configFilePath)
            try:
                autoSyncStatus = configParser.get('WebSphere', 'was.autosync')
            except:
                autoSyncStatus = ''
            print "autoSyncStatus: " + autoSyncStatus
            if (autoSyncStatus == 'true'):
                print '\n\nSynchronizing all Nodes!\n\tThis may need some minutes!\n\n'
                synchAllNodes()
            elif (autoSyncStatus == 'false'):
                "Please remember to sync your Nodes after ending your session! "
            else:
                answer_sync = raw_input(
                    'Do you want to synchronize all Nodes? ')
                allowed_answer_sync = ['yes', 'y', 'ja', 'j']
                if answer_sync.lower() in allowed_answer_sync:
                    print '\n\nSynchronizing all Nodes!\n\tThis may need some minutes!\n\n'
                    synchAllNodes()
                else:
                    print "Please remember to sync your Nodes after ending your session! "
        else:
            print "\nYour changes will not be saved!\n"
    else:
        print 'Nothing to save!'


def checkPropFile():
    '''
    Check if properties file is present, used to print warning in menu

    Returns
        propPresent (int)
            0 - successful
            1 - error
    '''
    import os.path
    propPresent = os.path.exists('ibmcnx/ibmcnx.properties')
    return propPresent


def propPrintError():
    '''
    Print warning message
    '''
    print '\t####################################################'
    print '\t#                                                  #'
    print '\t#             !!!      WARNING      !!!            #'
    print '\t#                                                  #'
    print '\t#    No properties file present, did you rename    #'
    print '\t#            ibmcnx_sample.properties?             #'
    print '\t#                                                  #'
    print '\t#   Some scripts will not work without this file!  #'
    print '\t#                                                  #'
    print '\t####################################################'

# Get temporary directory from properties file


def tempPath():
    configParser = ConfigParser.ConfigParser()
    configFilePath = r'ibmcnx/ibmcnx.properties'
    configParser.read(configFilePath)
    try:
        temppath = configParser.get('WebSphere', 'was.temppath')
    except:
        temppath = ''
    return temppath

# Menu Functions


def cfgDataSource():
    execfile("ibmcnx/config/DataSources.py")


def cfgJ2EERoleBackup():
    execfile("ibmcnx/config/j2ee/RoleBackup.py")


def cfgJ2EERoleRestore():
    execfile("ibmcnx/config/j2ee/RoleRestore.py")


def cfgJ2EERoleGlobalModerator():
    execfile("ibmcnx/config/j2ee/RoleGlobalMod.py")


def cfgJ2EERoleMetricsReader():
    execfile("ibmcnx/config/j2ee/RoleMetricsReader.py")


def cfgJ2EERoleMetricsReportRun():
    execfile("ibmcnx/config/j2ee/RoleMetricsReportRun.py")


def cfgJ2EERoleSocialMail():
    execfile("ibmcnx/config/j2ee/RoleSocialMail.py")


def cfgJVMHeap():
    execfile("ibmcnx/config/JVMHeap.py")


def cfgjvmtrace():
    execfile("ibmcnx/config/jvmtrace.py")


def cfgLogFiles():
    execfile("ibmcnx/config/LogFiles.py")


def cfgMonitoringPolicy():
    execfile('ibmcnx/config/MonitoringPolicy.py')


def cfgJVMLanguage():
    execfile('ibmcnx/config/JVMLanguage.py')


def cfgJVMCustProp():
    execfile('ibmcnx/config/JVMCustProp.py')


def cfgClusterMembers():
    execfile('ibmcnx/config/addNode.py')

def cfgWebSessionTimeOut():
    execfile('ibmcnx/config/WebSessionTO.py')

def cfgWebContainerSec():
    execfile('ibmcnx/config/WebContainerSec.py')

def cfgChgDBHost():
    execfile('ibmcnx/config/ChgDBHost.py')


def checkAppStatus():
    execfile('ibmcnx/check/AppStatus.py')


def checkDataSource():
    execfile('ibmcnx/check/DataSource.py')


def checkWebServer():
    execfile('ibmcnx/check/WebSrvStatus.py')


def docJVMHeap():
    execfile('ibmcnx/doc/JVMHeap.py')


def docJVMSettings():
    execfile('ibmcnx/doc/JVMSettings.py')


def docLogFiles():
    execfile('ibmcnx/doc/LogFiles.py')


def docPorts():
    execfile('ibmcnx/doc/Ports.py')


def docdatasources():
    execfile('ibmcnx/doc/DataSources.py')


def docVariables():
    execfile('ibmcnx/doc/Variables.py')


def docj2eeroles():
    execfile('ibmcnx/doc/j2eeroles.py')


def doctracesettings():
    execfile('ibmcnx/doc/traceSettings.py')


def docroleid():
    execfile('ibmcnx/doc/ProfRoleID.py')


def docinactiveprof():
    execfile('ibmcnx/doc/ProfilesInactive.py')


def cnxBackToMainMenu():
    execfile('ibmcnx/menu/menuMain.py')


def bye():
    print "bye"
    state = 'false'
    sys.exit(0)
