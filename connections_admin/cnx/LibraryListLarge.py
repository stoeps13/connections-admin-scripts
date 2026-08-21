'''
Work with Libraries - show persons and communities with maxUsed biggr 80%

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.org


License:       Apache 2.0
'''

execfile("filesAdmin.py")

import sys

noresult = 0

# Create two lists for personal and community libraries
persLib = FilesLibraryService.browsePersonal("title", "true", 1, 100000)
comLib = FilesLibraryService.browseCommunity("title", "true", 1, 100000)
tabs = ''


def multiply_tabs(sth, size):
    return ''.join(["%s" % sth for s in xrange(size)])


def printLibraries(librarieslist):
    result = librarieslist
    counter = len(result)
    print "\nName" + str(multiply_tabs(' ', 40 - len('Name'))) + "Percent Used" + "    " + 'maxSize (GB)' + '    ' + 'size (GB)'
    print str(multiply_tabs('-', 100))
    for i in range(counter):
        # You can change the percent value here
        if (result[i]['percentUsed'] >= 0.80):
            titleLen = len(str(result[i]['title']))
            if titleLen <= 40:
                strLen = 38 - len(str(result[i]['title']))
            elif titleLen > 40:
                strLen = 0
            print str(result[i]['title'])[:38] + str(multiply_tabs(' ', strLen)) + '  ' + str(round(result[i]['percentUsed'], 2)) + str(multiply_tabs(' ', 12)) + str(round(result[i]['maximumSize'] / 1073741824.0, 2)) + str(multiply_tabs(' ', 12)) + str(round(result[i]['size'] / 1073741824.0, 2))

print "\n\nPersonal Libraries bigger 80% used Space: "
printLibraries(persLib)
print "\n\nCommunity Libraries bigger 80% used Space: "
printLibraries(comLib)
