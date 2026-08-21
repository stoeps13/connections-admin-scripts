'''
Set the JVM Language to get english log messages

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.org


License:       Apache 2.0
'''

import connections_admin.appServer

WS1 = connections_admin.appServer.WasServers()

property = '-Duser.language=en -Duser.region=US'


def addProperties(server):
    jvm = AdminConfig.list('JavaVirtualMachine', server)
    currentJVMProps = AdminConfig.list("Property", jvm).splitlines()
    for prop in currentJVMProps:
        if property == AdminConfig.showAttribute(prop, "name"):
            AdminConfig.remove(prop)
    AdminConfig.modify(jvm, [['genericJvmArguments', attr]])

for count in range(WS1.serverNum):
    argStr = ''
    jvm = WS1.jvm[count]
    cell = WS1.cell[count]
    node = WS1.node[count]
    servername = WS1.serverName[count]

    jvmArgs = AdminTask.showJVMProperties(
        ['-serverName', servername, '-nodeName', node, '-propertyName', 'genericJvmArguments'])
    jvmArgs = jvmArgs.replace('  ', ' ').replace(
        '  ', ' ').lstrip().rstrip().split(' ')
    tmpArgs = []
    for arg in jvmArgs:
        if (arg != ''):
            if (arg.find('-Duser.language') >= 0) or (arg.find('-Duser.region') >= 0):
                continue
            else:
                tmpArgs.append(arg)
    for i in range(len(tmpArgs)):
        argStr = argStr + tmpArgs[i] + ' '
    newJvmArgs = argStr + property
    print "Adding " + property + " to " + servername
    AdminTask.setGenericJVMArguments(
        "[-nodeName " + node + " -serverName " + servername + " -genericJvmArguments '" + newJvmArgs + "']")


connections_admin.functions.saveChanges()
