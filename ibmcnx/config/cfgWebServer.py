'''
Add webserver to all app/modules

Author:                 Klaus Bild
E-Mail:                 klaus.bild@gmail.com
Blog:                   http://kbild.ch


Update:        Christoph Stoettner <christoph.stoettner@stoeps.de>

License:       Apache 2.0

TODO: 
Needs testing and option to add multiple webservers
'''

import ibmcnx.appServer

WS1 = ibmcnx.appServer.WasServers()


def getServerList(app, webserver):
    addServer = "NEW"
    addedServers = ""
    mapServers = AdminApp.view(app, '-MapModulesToServers').splitlines()
    for mapServer in mapServers:
        servers = mapServer.splitlines()
        for server in servers:
            if not server.find("Server:") == -1:
                if addedServers.find(addServer) == -1:
                    addedServers += "+" + server[9:]
                addServer = server[9:]
    if addedServers.find(webserver) == -1:
        addedServers += "+" + webserver
    return addedServers[1:]


def getCommand(app):
    webservers = AdminTask.listServers('[-serverType WEB_SERVER]').splitlines()
    fullservernamelist = ''
    for server in webservers:
        srv = server.split('/')
        fullservername = 'WebSphere:cell=' + srv[1] + ',node=' + srv[3] + ',server=' + (srv[5].split('|')[0])
        if fullservernamelist == '':
            fullservernamelist = fullservername
        else:
            fullservernamelist = fullservernamelist + '+' +  fullservername
    print(fullservernamelist)
    addServers = getServerList( app, fullservernamelist)
    module_ids = AdminApp.listModules(app).splitlines()
    command = "AdminApp.edit('" + app + "', '[ -MapModulesToServers ["
    for module_id in module_ids:
        start = module_id.find('#')
        module_id = module_id[start + 1:].replace("+", ",")
        endpoint = AdminApp.view(app).find(module_id)
        startpoint = AdminApp.view(app).rfind('Module:', 0, endpoint)
        module_name = AdminApp.view(app)[startpoint + 9:endpoint - 7]
        module_name = module_name.replace("\r","")
        module_name = '"' + module_name + '"'
        command += "[ " + module_name + " " + \
            module_id + " " + addServers + " ]"
    command += "]]' )"
    return command

apps = AdminApp.list().splitlines()
for app in apps:
    exec getCommand(app)
AdminConfig.save()
