'''
Print JVM Settings of all appservers, dmgr and nodeagent

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0
'''

# Get a list of all servers in WAS cell (dmgr, nodeagents, AppServer,
# webserver)
servers = AdminTask.listServers().splitlines()
#  Get a list of all webservers
webservers = AdminTask.listServers('[-serverType WEB_SERVER]').splitlines()

#  Remove webserver from servers list
for webserver in webservers:
    servers.remove(webserver)

jvmSettingsList = ['classpath', 'bootClasspath', 'verboseModeClass', 'verboseModeGarbageCollection', 'verboseModeJNI', 'initialHeapSize', 'maximumHeapSize',
                   'runHProf', 'hprofArguments', 'debugMode', 'debugArgs', 'genericJvmArguments', 'executableJarFileName', 'disableJIT', 'internalClassAccessMode']

for server in servers:
    jvm = AdminConfig.list('JavaVirtualMachine', server)
    srv = server.split('/')
    cell = srv[1]
    node = srv[3]
    servername = srv[5].split('|')[0]
    print "%s - %s - %s" % (cell, node, servername)
    for item in jvmSettingsList:
        length = 30 - len(item)
        space = str(' ' * length)
        try:
            print "\t" + item + ':' + space + AdminConfig.showAttribute(jvm, item)
        except:
            print '\t' + item + ':' + space + 'read error or empty'
    print ' '
