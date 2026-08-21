'''
Print all inactivated users

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
configFilePath = r'connections_admin/connections_admin.properties'
configParser.read(configFilePath)

# Change User and Password
props = Properties()
props.put('user', configParser.get('Database', 'dbUser'))
props.put('password', configParser.get('Database', 'dbPassword'))

jdbcPath = 'jdbc:db2://' + configParser.get('Database', 'dbHost') + ':' + configParser.get(
    'Database', 'dbPort') + '/' + configParser.get('Database', 'dbName')

conn = Driver().connect(jdbcPath, props)
stmt = conn.createStatement()

# Check column names and calls for this, should return inactive profiles
sql = "SELECT PROF_DISPLAY_NAME, PROF_UID, PROF_GUID from EMPINST.EMPLOYEE WHERE PROF_STATE = 1"

try:
    rs = stmt.executeQuery(sql)
except:
    print "\tError connecting to database!"

employeeList = []
while (rs.next()):
    row = {}
    row['PROF_DISPLAY_NAME'] = rs.getString(1)
    row['PROF_UID'] = rs.getString(2)
    row['PROF_GUID'] = rs.getString(3)
    employeeList.append(row)

rs.close()
stmt.close()
conn.close()

# print the result
print '\nInactive Userprofiles:'
print '-------------------------\n'
for e in employeeList:
    displaynamelen = len(e['PROF_DISPLAY_NAME'])
    print e['PROF_GUID'] + '\t' + e['PROF_DISPLAY_NAME'] + (30 - displaynamelen) * ' ' + e['PROF_UID']

print '\n\n'
