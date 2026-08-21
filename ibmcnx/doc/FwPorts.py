'''
Print ports list to have a good basis for Firewall rules

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0
'''

servers = AdminConfig.list('ServerEntry').splitlines()
portsdict = {}

for server in servers:
    nodename = str(server.split('(')[1].split('/')[3].split('|')[0])
    servername = str(server.split('(')[0])
    scope = nodename + ' ' + servername

    NamedEndPoints = AdminConfig.list("NamedEndPoint", server).splitlines()
    NamedEndPoints.sort()

    ports = []

    for namedEndPoint in NamedEndPoints:
        endPointName = AdminConfig.showAttribute(namedEndPoint, "endPointName")
        endPoint = AdminConfig.showAttribute(namedEndPoint, "endPoint")
        port = AdminConfig.showAttribute(endPoint, "port")
        ports.append(int(port))

    ports.sort()

    if portsdict.has_key( nodename ):
        portsdict[nodename].extend(ports)
    else:
        portsdict[nodename]=ports

keys = portsdict.keys()
keys.sort()

for key in keys:
    print key + ':'
    print '=' * (len(key)+1)
    portsdict[key].sort()

    ll = len(portsdict[key])
    portlist = portsdict[key]

    portstring = ''

    for i in range(ll):
        if portlist[i-1] != portlist[i] and portlist[i] != 0:
            try:
                if i == 0 and portlist[i] != 0:
                    if portlist[i] == portlist[i+1] + 1:
                        portstring = str(portlist[i])
                    else:
                        portstring = str(portlist[i]) + ', '
                elif portlist[i] == portlist[i-1]+1 and portlist[i] == portlist[i+1]-1:
                    portstring = portstring + '-'
                elif portlist[i] == portlist[i-1]+1:
                    portstring = portstring + str(portlist[i]) + ', '
                elif portlist[i] == portlist[i+1]-1 and portlist[i] == portlist[i+2]-2:
                    portstring = portstring + str(portlist[i])
                elif portlist[i] == portlist[i+1]-1:
                    portstring = portstring + str(portlist[i]) + ', '
                else:
                    portstring = portstring + str(portlist[i]) + ', '
            except:
                if portlist[i] == portlist[i-1]+1 and portlist[i] != portlist[i-2]+2:
                    portstring = portstring + ', ' + str(portlist[i])
                else:
                    portstring = portstring + str(portlist[i])
    for n in range(10):
        portstring="-".join(portstring.split('--'))
    print ''.join(portstring.split()) + '\n'
