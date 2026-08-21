'''
Work with Libraries -
print a list with Library Space Used bigger 80%

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       8.0.14
Date:          2026-08-21

License:       Apache 2.0
'''

execfile("filesAdmin.py")

import sys

noresult = 0


def searchLibrary(libType):
    libcount = 0
    if libType == 'p':
        # get the personal library count
        libcount = FilesLibraryService.getPersonalCount()
        result = FilesLibraryService.browsePersonal(
            "title", "true", 1, libcount)
        return result

    elif libType == 'c':
        # get the personal library count
        libcount = FilesLibraryService.getCommunityCount()
        result = FilesLibraryService.browseCommunity(
            "title", "true", 1, libcount)
        return result

    else:
        print ('Not a valid library Type!')


def printLibraryDetails(librarieslist):
    result = str( librarieslist )
    libraries = librarieslist
    counter = len(librarieslist)
    print "Name;Maximum;Size;Percent Used"

    for library in librarieslist:
        lib_name = library['title']
        lib_max = str(round(library['maximumSize'] / 1073741824.0, 2)) + ' GB'
        lib_size = str(round(library['size'] / 1073741824.0, 2)) + ' GB'
        lib_used = float(library['percentUsed'])
        # print(lib_name, lib_max, lib_size, lib_used)
        # print libraryinformation, when percentUsed > 80%
        if lib_used >= 80.0:
        #if lib_used >= 1.0:
            # print or return the library details
            print lib_name + ";" + lib_max + ";" + lib_size + ";" + str(lib_used)


# better print both library types without selection
print "\n\tPersonal Libraries with Percent Used > 80%\n"
printLibraryDetails(searchLibrary('p'))
print "\n\tCommunity Libraries with Percent Used > 80%\n"
printLibraryDetails(searchLibrary('c'))
