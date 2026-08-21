'''
Description:   Set HTTPSIndicatorHeader for all application server

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Update:        2025-04-10

License:       Apache 2.0
'''
import connections_admin.functions

def getAnswer(question):
    answer = ''
    answer = raw_input('\t' + question)
    return answer

WS1 = connections_admin.appServer.WasServers()

serverNum = WS1.serverNum

headername = getAnswer("What's the name of the HTTP header which shall be set for HttpsIndicatorHeader? ")

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

            if propName in ['httpsIndicatorHeader']:
                AdminConfig.remove(prop)

        newProp = [["name", "HttpsIndicatorHeader"], ["value", headername], ["description", "Important for SSL Offloading"]]

        AdminConfig.create("Property", serverWebContainer, newProp)

connections_admin.functions.saveChanges()

