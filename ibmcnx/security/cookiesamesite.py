'''
  Description:   Set CookieSameSite property

  Author:        Christoph Stoettner
  Mail:          christoph.stoettner@stoeps.de
  Documentation: http://scripting101.stoeps.de


  License:       Apache 2.0

'''
execfile("ibmcnx/wsadminlib/bin/wsadminlib.py")

servers=listServersOfType('APPLICATION_SERVER')
for server in servers:
    props = []
    serverName=getServerByNodeAndName(server[0], server[1])
    objectID=getObjectsOfType('SessionManager', serverName)

    # Check if CookieSameSite is already set
    sesMgrProps=AdminConfig.list('Property', objectID[0]).split('\n')

    # Delete old CookieSameSite entries
    for prop in sesMgrProps:
        propName = AdminConfig.showAttribute(prop, 'name')

        if propName in ['CookieSameSite', 'HttpSessionIdReuse']:
            # print('Deleting already configured CookieSameSite property')
            AdminConfig.remove(prop)

    AdminConfig.create('Property', objectID[0], '[[validationExpression ""] [name "CookieSameSite"] [description "Important for Teams Integration"] [value "None"] [required "false"]]')
    AdminConfig.create('Property', objectID[0], '[[validationExpression ""] [name "HttpSessionIdReuse"] [description "Preserve sessions across apps"] [value "true"] [required "false"]]')

saveAndSync()
