'''
Set Reader Roles to Restricted - no anonymous access possible

Description:
Script is tested with HCL Connections 8

Author: Christoph Stoettner
Blog: https://stoeps.de
E-Mail:
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0

History:
20131124  Christoph Stoettner     Update with loop and try/except to handle errors, added group support
20140324  Christoph Stoettner     Changed all reader roles to "All authenticated", Ajax proxy security is configured with this role!
20140716  Christoph Stoettner     Set the script to only change reader role
20241209  Christoph Stoettner     Create exception for RichTextEditors and set Reader to Everyone here (Highlights and Overview load in loop if set to authenticated)
'''

import connections_admin.functions

apps = AdminApp.list()
appsList = apps.splitlines()
for app in appsList:
    print "Setting Reader Role to Authenticated for %s" % app.upper()
    try:
        if app == 'RichTextEditors':
            print("Don't change RTE app")
            AdminApp.edit(app, '[-MapRolesToUsers [["reader" Yes No "" ""] ]]')
        else:
            AdminApp.edit(app, '[-MapRolesToUsers [["reader" No Yes "" ""] ]]')
    except:
        print "No Reader Role in %s" % app.upper()
connections_admin.functions.saveChanges()
