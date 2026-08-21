'''
Description:   Set property to disable Websphere header x-powered-by

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Update:        2025-04-10

License:       Apache 2.0
'''
import connections_admin.appServer
import connections_admin.functions

def getAnswer(question):
    answer = ''
    answer = raw_input('\t' + question)
    return answer


def getConfigIds(configList):
    """
    Return complete wsadmin config ids from AdminConfig.list output.

    Some WebSphere config ids can be wrapped across multiple lines. A plain
    splitlines() can therefore pass incomplete ids to AdminConfig.showAttribute,
    causing WASX7077E errors about missing closing parentheses.
    """
    configIds = []
    configId = ''

    for line in configList.splitlines():
        line = line.strip()
        if line == '':
            continue

        if configId == '':
            configId = line
        else:
            configId += line

        if configId.count('(') <= configId.count(')'):
            configIds.append(configId)
            configId = ''

    if configId != '':
        configIds.append(configId)

    return configIds


WS1 = connections_admin.appServer.WasServers()

serverNum = WS1.serverNum

for count in range(WS1.serverNum):
    jvm = WS1.jvm[count]
    cell = WS1.cell[count]
    node = WS1.node[count]
    servername = WS1.serverName[count]

    if servername == 'dmgr':
        print "Value not set for %s" % servername
    elif servername == 'nodeagent':
        print "Value not set for %s" % servername
    else:
        print "%s - %s - %s" % (cell, node, servername)
        print 'Setting WebContainer Custom Property'

        server = '"/Server:' + servername + '/"'
        serverId = AdminConfig.getid(server)
        serverWebContainer = AdminConfig.list("WebContainer", serverId )

        webContainerProps = getConfigIds(AdminConfig.list('Property', serverWebContainer))

        for prop in webContainerProps:
            propName = AdminConfig.showAttribute(prop, 'name')

            if propName in ['com.ibm.ws.webcontainer.disablexPoweredBy']:
                AdminConfig.remove(prop)

        newProp = [["name", "com.ibm.ws.webcontainer.disablexPoweredBy"], ["value", 'true'], ["description", "Security best practise"]]

        AdminConfig.create("Property", serverWebContainer, newProp)

connections_admin.functions.saveChanges()

