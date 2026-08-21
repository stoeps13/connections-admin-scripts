'''
Set WebSession Timeout in all application servers

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0
'''
import ibmcnx.functions


def getAnswer(question):
    answer = ''
    while not answer.isnumeric():
        answer = raw_input('\t' + question)

    return answer

wasServers = []
wasServers = AdminTask.listServers(
    '[-serverType APPLICATION_SERVER]').splitlines()

print '\n'
timeoutValue = getAnswer(
    "Which value should be set as websession timeout (integer)? ")
print '\n'
for wasServer in wasServers:
    tuningVM = AdminConfig.list('TuningParams', wasServer)
    AdminConfig.modify(
        tuningVM, '[[invalidationTimeout "' + timeoutValue + '"]]')
    print "\tSession Timeout set for " + wasServer.split('|')[0].split('(')[0] + ":\t\t" + timeoutValue

print '\n'
ibmcnx.functions.saveChanges()
print '\n'
