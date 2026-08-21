'''
Work with Libraries - add policies

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0

TODO: Check Errorhandling and print assigned policy of the libraries
'''

execfile("filesAdmin.py")

import sys

noresult = 0


def printPolicies(policies):
    state = ''
    print '# \tmax Size \t\t uuid \t\t\t\t\t title'
    print '----------------------------------------------------------------------------------------------------'
    for i in range(len(policies)):
        print str(i) + '\t' + str(round(policies[i]['maximumSize'] / 1073741824.0, 2)) + ' GB\t\t' + str(policies[i]['id']) + '\t\t' + str(policies[i]['title'])
    print
    return policies


def getAssignedPolicy(policyId):
    policy = FilesPolicyService.getById(policyId)
    policy_name = policy['title']
    return policy_name


def askLibraryType():
    #  Check if Community or Personal Libraries should be searched
    is_valid_lib = 0
    while not is_valid_lib:
        try:
            libask = 'Personal, Community Library, Menu or Exit? (P|C|M|X)'
            libType = raw_input(libask).lower()

            if libType == 'p':
                is_valid_lib = 1  # set it to 1 to validate input and to terminate the while..not loop
                return libType
            elif libType == 'c':
                is_valid_lib = 1  # set it to 1 to validate input and to terminate the while..not loop
                return libType
            elif libType == 'm':
                is_valid_lib = 0
                execfile('connections_admin/menu/menuMain.py')
            elif libType == 'x':
                is_valid_lib = 0
                sys.exit()
            else:
                print ("'%s' is not a valid menu option.") % libType
        except ValueError, e:
            print ("'%s' is not valid." % e.args[0].split(": ")[1])


def searchLibrary(libType):
    if libType == 'p':
        libcount = FilesLibraryService.getPersonalCount()
        libNameAsk = 'Which User you want to search? (min 1 character): '
        libNameAnswer = raw_input(libNameAsk)
        result = FilesUtilService.filterListByString(FilesLibraryService.browsePersonal(
            "title", "true", 1, libcount), "title", ".*" + libNameAnswer + ".*")
        return result

    elif libType == 'c':
        libcount = FilesLibraryService.getCommunityCount()
        libNameAsk = 'Which Community Library you want to search? (min 1 character): '
        libNameAnswer = raw_input(libNameAsk)
        result = FilesUtilService.filterListByString(FilesLibraryService.browseCommunity(
            "title", "true", 1, libcount), "title", ".*" + libNameAnswer + ".*")
        return result

    else:
        print ('Not a valid library Type!')


def getLibraryDetails(librarieslist):
    # result = str( librarieslist )
    result = librarieslist
    counter = len(result)
    index = 0
    count = 0

    if (counter < 1):
        print '\n------------------------------------------------------------------'
        print 'There is NO Library with this name\nPlease try again ----------->'
        print '------------------------------------------------------------------\n'
        return (0, 0, 0, 0)
    elif (counter < 2):
        lib_number = 0
        lib_id = result[lib_number]['id']
        lib_name = result[lib_number]['title']
        lib_policy = result[lib_number]['policyId']
        return (lib_id, lib_name, lib_policy, 1)
    else:
        lib_id = []
        lib_name = []
        numberlist = []
        lib_number = -1
        i = 0
        print '\nThere are multiple libraries with this name:'
        print '----------------------------------------------'
        for i in range(len(result)):
            print str(i) + '\t' + result[i]['title']
            i += 1
            count += 1
        print '----------------------------------------------'
        go_on = ''
        while go_on != 'TRUE':
            lib_number = raw_input('Please type the number of the library? ')
            try:
                lib_number = int(lib_number)
            except (TypeError, ValueError):
                continue
            if count - 1 >= lib_number >= 0:
                break
            else:
                continue
        lib_id = result[lib_number]['id']
        lib_name = result[lib_number]['title']
        lib_policy = result[lib_number]['policyId']
        return (lib_id, lib_name, lib_policy, 1)

while noresult != 1:
    lib_id, lib_title, lib_policy, noresult = getLibraryDetails(
        searchLibrary(askLibraryType()))

libraryUUID = lib_id

print 'Available Policies: '
policies = printPolicies(FilesPolicyService.browse("title", "true", 1, 250))
print '\n'
print 'Policy will be assigned to: ' + lib_title
print 'Actual assigned policy is: ' + getAssignedPolicy(lib_policy)
print '\n'

policyID = int(raw_input('Which policy do you want to assign? '))
policyUUID = policies[policyID]['id']

FilesLibraryService.assignPolicy(libraryUUID, policyUUID)
