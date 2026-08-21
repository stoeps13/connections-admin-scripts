'''
Work with Libraries - show fileSize and used space

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Author:        Martin Leyrer
Mail:          leyrer@gmail.com
Documentation: http://scripting101.stoeps.de



License:       Apache 2.0

History:
20150307  Martin Leyrer   Implemented support for paging -> more than maxpagingresults displayed
                          Added error handling for connectivity issues
'''

import sys
import java.util.ArrayList as ArrayList

try:
    execfile("filesAdmin.py")
except:
    print "\nLibrarySizes could not connect to the 'HCL Websphere Deployment Manager'. Please make sure the 'dmgr' is running."
    sys.exit()

try:
    dummy = FilesLibraryService.getPersonalCount()
except:
    print "\nLibrarySizes was not able to communicate with the 'HCL Connections Files' application. Please make sure 'Files' is running."
    sys.exit()


noresult = 0

# number of search results per page
maxpagingresults = 250


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
                execfile('ibmcnx/menu/menuMain.py')
            elif libType == 'x':
                is_valid_lib = 0
                sys.exit()
            else:
                print ("'%s' is not a valid menu option.") % libType
        except ValueError, e:
            print ("'%s' is not valid." % e.args[0].split(": ")[1])


def flsBrowse(libType, page, max):
    try:
        if libType == 'p':
            libList = FilesLibraryService.browsePersonal(
                "title", "true", page, max)
        elif libType == 'c':
            libList = FilesLibraryService.browseCommunity(
                "title", "true", page, max)
        else:
            print ('Not a valid library Type!')
            sys.exit()
    except:
        print "\nLibrarySizes was not able to communicate with the 'HCL Connections Files' application. Please make sure 'Files' is running."
        sys.exit()
    return libList


def getLibraryList(libType):
    # iterate through all the result pages to return ALL found libraries
    pagecount = 1
    allLibs = ArrayList()
    libList = flsBrowse(libType, pagecount, maxpagingresults)
    while(not libList.isEmpty()):
        allLibs.addAll(libList)
        pagecount = pagecount + 1
        libList = flsBrowse(libType, pagecount, maxpagingresults)
    return allLibs


def searchLibrary(libType):
    if libType == 'p':
        libNameAsk = 'Which User you want to search? (min 1 character): '
        libNameAnswer = raw_input(libNameAsk)
        result = FilesUtilService.filterListByString(
            getLibraryList(libType), "title", ".*" + libNameAnswer + ".*")
        return result

    elif libType == 'c':
        libNameAsk = 'Which Community Library you want to search? (min 1 character): '
        libNameAnswer = raw_input(libNameAsk)
        result = FilesUtilService.filterListByString(
            getLibraryList(libType), "title", ".*" + libNameAnswer + ".*")
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
        lib_max = result[lib_number]['maximumSize']
        lib_size = result[lib_number]['size']
        lib_used = result[lib_number]['percentUsed']
        return (lib_id, lib_name, lib_max, lib_size, lib_used, 1)

while noresult != 1:
    lib_id, lib_title, lib_max, lib_size, lib_used, noresult = getLibraryDetails(
        searchLibrary(askLibraryType()))

print "\n\tTitle: \t\t" + str(lib_title)
print "\tmaximumSize: \t" + str(round(lib_max / 1073741824.0, 2)) + ' GB'
print "\tSize used: \t" + str(round(lib_size / 1073741824.0, 2)) + ' GB'
print "\tPercent used: \t" + str(lib_used)
# getLibraryDetails(searchLibrary(askLibraryType()))
