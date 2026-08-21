'''
Add extended role to a user

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0
'''

import sys
import ConfigParser

global globdict
globdict = globals()


def getMailAddress():
    '''
    Ask for mail address to add role

    Returns
        mail - string
    '''
    mail = raw_input('Adding extended role to user (provide mailaddress): ')
    return mail


def main():
    mailAddress = getMailAddress()
    '''
    Idea would be to check if the user already has the role, but getRoles() do not return a value it only prints the actual value

    try:
        role = ProfilesService.getRoles(mailAddress)
    except:
        print 'User not found!'

    if role == '[employee]':
        try:
            ProfilesService.setRole(mailaddress)
        except:
            print "Error occured"
    elif role == '[employee.extended]':
        print 'User has alreay role: ' + role
    else:
        print 'User not found in peopleDB.'
    '''
    ProfilesService.setRole(mailAddress, EMPLOYEE_EXTENDED)

# Get configuration from properties file
configParser = ConfigParser.ConfigParser()
configFilePath = r'connections_admin/connections_admin.properties'
configParser.read(configFilePath)

try:
    # get admin id to check profiles commands
    connadmin = configParser.get('Generic', 'j2ee.cnxadmin').split('|')
except:
    print "Did you rename connections_admin.properties?"

try:
    # Check if Profiles Scripts are loaded
    temp = ProfilesService.getRolesByUserId(connadmin[0])
except:
    print "\tLoading Profiles Admin Commands:"
    execfile("profilesAdmin.py")

main()
