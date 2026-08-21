'''
Description:   Set property to disable Websphere header x-powered-by

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       8.0.14
Date:          2026-08-21
Update:        2025-04-10

License:       Apache 2.0
'''
import ibmcnx.functions

def getAnswer(question):
    answer = ''
    answer = raw_input('\t' + question)
    return answer

WS1 = ibmcnx.appServer.WasServers()

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

        webContainerProps = AdminConfig.list('Property', serverWebContainer).split('\n')

        for prop in webContainerProps:
            if prop == '': continue
            propName = AdminConfig.showAttribute(prop, 'name')

            if propName in ['com.ibm.ws.webcontainer.disablexPoweredBy']:
                AdminConfig.remove(prop)

        newProp = [["name", "com.ibm.ws.webcontainer.disablexPoweredBy"], ["value", 'true'], ["description", "Security best practise"]]

        AdminConfig.create("Property", serverWebContainer, newProp)

ibmcnx.functions.saveChanges()

