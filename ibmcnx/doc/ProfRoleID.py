'''
Print all user with ROLE_ID=employee.extended

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0

'''
import os
import sys
from java.util import Properties
import ConfigParser

global globdict
globdict = globals()

try:
    import com.ibm.db2.jcc.DB2Driver as Driver
except:
    print "\n\tNo jdbc driver available, start wsadmin with\n"
    print "\t\"-javaoption -Dcom.ibm.ws.scripting.classpath=path/db2jcc4.jar\"\n"
    print "\tSee http://scripting101.org/resources/installing-the-scripts/ for details\n"

# Get configuration from properties file
configParser = ConfigParser.ConfigParser()
configFilePath = r'ibmcnx/ibmcnx.properties'
configParser.read(configFilePath)

# Change User and Password
props = Properties()
props.put('user', configParser.get('Database', 'dbUser'))
props.put('password', configParser.get('Database', 'dbPassword'))

jdbcPath = 'jdbc:db2://' + configParser.get('Database', 'dbHost') + ':' + configParser.get(
    'Database', 'dbPort') + '/' + configParser.get('Database', 'dbName')

conn = Driver().connect(jdbcPath, props)
stmt = conn.createStatement()

sql = "SELECT r.PROF_DISPLAY_NAME, r.PROF_MAIL, r.PROF_UID, e.ROLE_ID from EMPINST.EMP_ROLE_MAP e left join EMPINST.EMPLOYEE r ON e.PROF_KEY = r.PROF_KEY WHERE e.ROLE_ID = 'employee.extended'"

try:
    rs = stmt.executeQuery(sql)
except:
    print "Error connecting to database!"

employeeList = []
while (rs.next()):
    row = {}
    row['PROF_DISPLAY_NAME'] = rs.getString(1)
    row['PROF_MAIL'] = rs.getString(2)
    row['PROF_UID'] = rs.getString(3)
    row['ROLE_ID'] = rs.getString(4)
    employeeList.append(row)

rs.close()
stmt.close()
conn.close()

# print the result
print '\n\nUser with employee.extended role:'
print '---------------------------------\n'
for e in employeeList:
    maillen = len(e['PROF_DISPLAY_NAME'])
    displaynamelen = len(e['PROF_DISPLAY_NAME'])
    uidlen = len(e['PROF_UID'])

    print e['PROF_DISPLAY_NAME'] + (30 - displaynamelen) * ' ' + e['PROF_MAIL'] + (50 - maillen) * ' ' + e['PROF_UID']

print "\n"
