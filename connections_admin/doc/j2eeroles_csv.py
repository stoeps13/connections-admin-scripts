'''
** Create a documentation of j2ee roles **
pipe this script to a file (csv), then it can be used within table calculation

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


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

# Print headline to use with csv
print "App;Role;Everyone;All Authenticated;Mapped Users;Mapped Groups"

for app in appsList:
    dictionary = convertRoles2Dict(app, AdminApp.view(app, "-MapRolesToUsers"))
    for role in dictionary.keys():
        # Loop through Roles
        print app.upper() + ";" + role.upper(),
        print ";" + dictionary[role]['Everyone?'],
        print ";" + dictionary[role]['All authenticated?'],
        print ";" + dictionary[role]['Mapped users'],
        print ";" + dictionary[role]['Mapped groups']
