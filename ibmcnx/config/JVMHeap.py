'''
Set the JVM Heap Sizes

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0
'''

import ibmcnx.appServer

WS1 = ibmcnx.appServer.WasServers()

for count in range(WS1.serverNum):
    jvm = WS1.jvm[count]
    cell = WS1.cell[count]
    node = WS1.node[count]
    servername = WS1.serverName[count]

    print "%s - %s - %s" % (cell, node, servername)
    print 'Actual setting: '
    print '\t initialHeapSize: ' + AdminConfig.showAttribute(jvm, 'initialHeapSize')
    print '\t maximumHeapSize: ' + AdminConfig.showAttribute(jvm, 'maximumHeapSize')
    print 'RETURN to let actual value!'
    initialHeapSize = raw_input('InitialHeapSize (MB): ')
    maximumHeapSize = raw_input('MaximumHeapSize (MB): ')

    if initialHeapSize == '':
        initialHeapSize = AdminConfig.showAttribute(jvm, 'initialHeapSize')

    if maximumHeapSize == '':
        maximumHeapSize = AdminConfig.showAttribute(jvm, 'maximumHeapSize')

    initialHeap = '[[ initialHeapSize ' + str(initialHeapSize) + ' ]]'
    maxHeap = '[[ maximumHeapSize ' + str(maximumHeapSize) + ' ]]'

    AdminConfig.modify(jvm, initialHeap)
    AdminConfig.modify(jvm, maxHeap)
    print ''

ibmcnx.functions.saveChanges()
