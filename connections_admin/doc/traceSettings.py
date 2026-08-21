'''
Print trace settings of all JVM

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0
'''

ts = AdminControl.queryNames("type=TraceService,*")
tss = ts.split()
print '\n\t JVM Trace Settings of all servers'
print '\t =================================\n'
for trace in tss:
    print '\t ' + str(trace.split(',')[1].split("=")[1])
    spec = AdminControl.getAttribute(trace, "traceSpecification")
    print '\t\t ' + spec + '\n'
