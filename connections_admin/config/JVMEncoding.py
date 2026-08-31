'''
Set JVM encoding custom properties to UTF-8.

The following properties are checked for every application server:
- client.encoding.override
- file.encoding
- sun.jun.encoding

Existing properties are updated when their value is not UTF-8. Missing
properties are created.

License: Apache 2.0
'''
import os

WSADMINLIB = "connections_admin/wsadminlib/bin/wsadminlib.py"
WSADMINLIB_URL = "https://raw.githubusercontent.com/wsadminlib/wsadminlib/master/bin/wsadminlib.py"

if not os.path.isfile(WSADMINLIB):
    raise IOError("Required wsadminlib is missing: %s\nDownload it from %s" % (WSADMINLIB, WSADMINLIB_URL))

execfile(WSADMINLIB)

TARGET_VALUE = 'UTF-8'
ENCODING_PROPERTIES = [
    'client.encoding.override',
    'file.encoding',
    'sun.jnu.encoding'
]

servers = listServersOfType('APPLICATION_SERVER')
print "Found %d application server(s)" % len(servers)

for nodeName, serverName in servers:
    print "Checking JVM encoding properties for %s/%s" % (nodeName, serverName)
    serverId = getServerByNodeAndName(nodeName, serverName)
    jvms = getObjectsOfType('JavaVirtualMachine', serverId)

    if not jvms:
        raise RuntimeError("No JavaVirtualMachine found for %s/%s" % (nodeName, serverName))

    jvmId = jvms[0]
    properties = {}
    propertyIds = AdminConfig.list('Property', jvmId).splitlines()

    for propertyId in propertyIds:
        if not propertyId.strip():
            continue
        propertyName = AdminConfig.showAttribute(propertyId, 'name')
        if propertyName in ENCODING_PROPERTIES:
            properties[propertyName] = propertyId

    for propertyName in ENCODING_PROPERTIES:
        propertyId = properties.get(propertyName)
        if propertyId:
            currentValue = AdminConfig.showAttribute(propertyId, 'value')
            if currentValue != TARGET_VALUE:
                print "  Updating %s: %s -> %s" % (propertyName, currentValue, TARGET_VALUE)
                AdminConfig.modify(propertyId, [['value', TARGET_VALUE]])
            else:
                print "  Keeping %s=%s" % (propertyName, TARGET_VALUE)
        else:
            print "  Creating %s=%s" % (propertyName, TARGET_VALUE)
            AdminConfig.create(
                'Property', jvmId,
                '[[validationExpression ""] [name "%s"] [description "JVM encoding"] [value "%s"] [required "false"]]' %
                (propertyName, TARGET_VALUE))

saveAndSync()
print "JVM encoding configuration completed and synchronized"
