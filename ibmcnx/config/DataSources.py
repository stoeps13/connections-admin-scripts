'''
Change DataSource connectionPools

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       8.0.14
Date:          2026-08-21

License:       Apache 2.0

Check ExId of a User in all Connections Applications
'''

import ConfigParser
import ibmcnx.functions

try:
    configParser = ConfigParser.ConfigParser()
    configFilePath = r'ibmcnx/ibmcnx.properties'
    configParser.read(configFilePath)
except:
    print 'Error on reading ibmcnx.properties, maybe you forgot to create the file?'

perf = {'activities': {'minConnections': configParser.get('Tuning', 'opnact.min'), 'maxConnections': configParser.get('Tuning', 'opnact.max')},
        'blogs': {'minConnections': configParser.get('Tuning', 'blogs.min'), 'maxConnections': configParser.get('Tuning', 'blogs.max')},
        'communities': {'minConnections': configParser.get('Tuning', 'sncomm.min'), 'maxConnections': configParser.get('Tuning', 'sncomm.max')},
        'dogear': {'minConnections': configParser.get('Tuning', 'dogear.min'), 'maxConnections': configParser.get('Tuning', 'dogear.max')},
        'files': {'minConnections': configParser.get('Tuning', 'files.min'), 'maxConnections': configParser.get('Tuning', 'files.max')},
        'forum': {'minConnections': configParser.get('Tuning', 'forum.min'), 'maxConnections': configParser.get('Tuning', 'forum.max')},
        'homepage': {'minConnections': configParser.get('Tuning', 'homepage.min'), 'maxConnections': configParser.get('Tuning', 'homepage.max')},
        'metrics': {'minConnections': configParser.get('Tuning', 'metrics.min'), 'maxConnections': configParser.get('Tuning', 'metrics.max')},
        'mobile': {'minConnections': configParser.get('Tuning', 'mobile.min'), 'maxConnections': configParser.get('Tuning', 'mobile.max')},
        'news': {'minConnections': configParser.get('Tuning', 'news.min'), 'maxConnections': configParser.get('Tuning', 'news.max')},
        'oauth provider': {'minConnections': configParser.get('Tuning', 'oauth.min'), 'maxConnections': configParser.get('Tuning', 'oauth.max')},
        'profiles': {'minConnections': configParser.get('Tuning', 'profiles.min'), 'maxConnections': configParser.get('Tuning', 'profiles.max')},
        'pushnotification': {'minConnections': configParser.get('Tuning', 'pns.min'), 'maxConnections': configParser.get('Tuning', 'pns.max')},
        'search': {'minConnections': configParser.get('Tuning', 'search.min'), 'maxConnections': configParser.get('Tuning', 'search.max')},
        'urlpreview': {'minConnections': configParser.get('Tuning', 'urlprev.min'), 'maxConnections': configParser.get('Tuning', 'urlprev.max')},
        'widgetcontainer': {'minConnections': configParser.get('Tuning', 'widget.min'), 'maxConnections': configParser.get('Tuning', 'widget.max')},
        'wikis': {'minConnections': configParser.get('Tuning', 'wikis.min'), 'maxConnections': configParser.get('Tuning', 'wikis.max')},
        'icec': {'minConnections': configParser.get('Tuning', 'icec.min'), 'maxConnections': configParser.get('Tuning', 'icec.max')}}

statementCacheSize = configParser.get('Tuning', 'statementCache')

print 'DataSource Parameters will be set to: '
print 'Database \t statementCacheSize \t minConnections \t maxConnections'
print '-------------------------------------------------------------------------------'
for db in perf.keys():
    print db.upper(),
    if len(db) < 7:
        print '\t\t',
    if len(db) <= 14 and len(db) >= 7:
        print '\t',
    print '\t' + str(statementCacheSize),
    if len(str(perf[db]['minConnections'])) == 3:
        space0 = ''
    elif len(str(perf[db]['minConnections'])) == 2:
        space0 = ' '
    else:
        space0 = '  '
    if len(str(perf[db]['maxConnections'])) == 3:
        space1 = ''
    elif len(str(perf[db]['maxConnections'])) == 2:
        space1 = ' '
    else:
        space1 = '  '

    print '\t\t      ' + space0 + str(perf[db]['minConnections']),
    print '\t\t      ' + space1 + str(perf[db]['maxConnections'])

print '-------------------------------------------------------------------------------'
answer = raw_input(
    'Are you sure, that your parameters should be overwritten? (Yes|No) ')
allowed_answer = ['yes', 'y', 'ja', 'j']

if answer.lower() in allowed_answer:
    for db in perf.keys():    # Looping through databases
        print 'Change DataSource parameters for: %s' % db.upper()
        try:
            t1 = ibmcnx.functions.getDSId(db)
            print '\t\tstatementCacheSize: \t' + str(statementCacheSize)
            print '\t\tminConnections: \t' + str(perf[db]['minConnections'])
            print '\t\tmaxConnections: \t' + str(perf[db]['maxConnections'])
            AdminConfig.modify(
                t1, '[[statementCacheSize "' + str(statementCacheSize) + '"]]')
            AdminConfig.modify(t1, '[[connectionPool [[minConnections "' + str(perf[db][
                               'minConnections']) + '"][maxConnections "' + str(perf[db]['maxConnections']) + '"]]]]')
            print '\tParameter for %s successfully set!\n' % db.upper()
        except:
            print '\tError can\'t set Performance parameter for' + db.upper() + '!'
    print "Saving changes!"
    ibmcnx.functions.saveChanges()

else:
    print '\t\tNothing changed! '
