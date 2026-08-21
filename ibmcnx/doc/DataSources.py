'''
Documentation of DataSources

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.org

Update:        2025-03-18

License:       Apache 2.0
'''

import ibmcnx.functions

# Get a list of all DataSources
datasources = AdminConfig.list('DataSource', AdminConfig.getid(
    '/Cell:' + AdminControl.getCell() + '/')).splitlines()
# new list for database names
dbList = []


def multiply_tabs(sth, size):
    return ''.join(["%s" % sth for s in xrange(size)])

for datasource in datasources:
    # split DataSource and DataSource ID
    datasource = datasource.split('(')
    ds = datasource[0]
    # Remove Default Datasources
    if (ds != 'DefaultEJBTimerDataSource') and (ds != 'OTiSDataSource'):
        # check for " (e.g. "oauth provider)
        if (len(ds.split('"')) > 1):
            ds = ds.split('"')[1]
        # write datasouce to database list
        dbList.append(ds)
dbList.sort()

parameterList = ['currentSchema', 'databaseName', 'driverType',
                 'portNumber', 'resultSetHoldability', 'serverName']

for count in range(len(dbList)):
    db = dbList[count]
    # Loop through all databases in our dictionary
    print '\n\tDataSource parameters of: ' + db.upper()
    try:
        # get the id of the datasource
        dsid = ibmcnx.functions.getDSId(db)

        # Get connection pool settings
        connectionPool = AdminConfig.list('ConnectionPool', dsid)
        if connectionPool:
            try:
                minConn = AdminConfig.showAttribute(connectionPool, 'minConnections')
                print '\t\tminConnections',
                print str(multiply_tabs(' ', 25 - len('minConnections'))),
                print minConn
            except Exception, e:
                print '\t\tminConnections             ERROR: ' + str(e)

            try:
                maxConn = AdminConfig.showAttribute(connectionPool, 'maxConnections')
                print '\t\tmaxConnections',
                print str(multiply_tabs(' ', 25 - len('maxConnections'))),
                print maxConn
            except Exception, e:
                print '\t\tmaxConnections             ERROR: ' + str(e)

        # Try to get statement cache size from the datasource itself
        try:
            stmtCacheSize = AdminConfig.showAttribute(dsid, 'statementCacheSize')
            print '\t\tstatementCacheSize',
            print str(multiply_tabs(' ', 25 - len('statementCacheSize'))),
            print stmtCacheSize
        except Exception, e:
            # If not found directly, try to look for it in the properties
            stmtCacheSizeFound = False
            properties = AdminConfig.list('J2EEResourceProperty', dsid).splitlines()
            for prop in properties:
                propName = AdminConfig.showAttribute(prop, 'name')
                if propName == 'statementCacheSize':
                    stmtCacheSizeFound = True
                    print '\t\tstatementCacheSize',
                    print str(multiply_tabs(' ', 25 - len('statementCacheSize'))),
                    print AdminConfig.showAttribute(prop, 'value')

            if not stmtCacheSizeFound:
                # Try to check if it's under datasource properties
                print '\t\tstatementCacheSize         NOT FOUND'

        # Get the original properties
        properties = AdminConfig.list(
            'J2EEResourceProperty', dsid).splitlines()

        for prop in properties:
            propName = AdminConfig.showAttribute(prop, 'name')
            for para in parameterList:
                if (propName == para):
                    print '\t\t' + propName,
                    print str(multiply_tabs(' ', 25 - len(propName))),
                    print AdminConfig.showAttribute(prop, 'value')

    except Exception, e:
        error_type = e.__class__.__name__
        error_message = str(e)
        print ' - ERROR: ' + error_type + ': ' + error_message
        print '\t\tError details:'

        # Get the traceback info
        tb_info = traceback.format_exc()
        # Print the traceback with proper indentation
        for line in tb_info.splitlines():
            print '\t\t' + line
