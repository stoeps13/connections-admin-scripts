'''
** Create a documentation of j2ee roles **

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       8.0.14
Date:          2026-08-21

License:       Apache 2.0
'''


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

for app in appsList:
    dictionary = convertRoles2Dict(app, AdminApp.view(app, "-MapRolesToUsers"))
    print "\n\n Application:\t" + app.upper()
    print "------------------------------------------"
    for role in dictionary.keys():
        # Loop through Roles
        print "\tRole:\t" + role.upper()
        print "\t\tEveryone:\t\t" + dictionary[role]['Everyone?']
        print "\t\tAll authenticated:\t" + dictionary[role]['All authenticated?']
        print "\t\tMapped users:\t\t" + dictionary[role]['Mapped users']
        print "\t\tMapped groups:\t\t" + dictionary[role]['Mapped groups']
