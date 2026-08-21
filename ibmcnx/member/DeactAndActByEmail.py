'''
Deactivate and activate a user

Description:
on login problems you often need to deactivate and reactivate a user
with this script you can do this with one step

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       8.0.14
Date:          2026-08-21

License:       Apache 2.0

'''

import os
import sys
from java.util import Properties
import ConfigParser

global globdict
globdict = globals()


def loadCNXCommands():
    execfile("ibmcnx/loadCnxApps.py", globdict)

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

email = raw_input(
    "\n\tMail address of profile you want to deactivate: ").lower()

sql = 'select PROF_UID,PROF_MAIL,PROF_MAIL_LOWER,PROF_GUID from empinst.employee where PROF_MAIL_LOWER = \'' + \
    email + '\' order by PROF_UID_LOWER'
rs = stmt.executeQuery(sql)

employeeList = []
while (rs.next()):
    row = {}
    row['PROF_UID'] = rs.getString(1)
    row['PROF_MAIL'] = rs.getString(2)
    row['PROF_MAIL_LOWER'] = rs.getString(3)
    row['PROF_GUID'] = rs.getString(4)
    employeeList.append(row)

rs.close()
stmt.close()
conn.close()

# print the result
for e in employeeList:
    # print e['PROF_UID_LOWER'] + "\t\t" + e['PROF_MAIL_LOWER'] + "\t\t" + e['PROF_GUID']
    # print e['PROF_MAIL']
    print '\tDeactivate User with ExID: \t',

try:
    MAILADDRESS = e['PROF_MAIL']
except:
    print '\tNo User with mail address ' + email + ' found!'

try:
    temp = ActivitiesMemberService.getMemberExtIdByLogin(MAILADDRESS)
except:
    loadCNXCommands()

try:
    print "\tInactivate Activities\t\t",
    ActivitiesMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
    print '\t No user with Email ' + MAILADDRESS + ' found'

try:
    print "\tInactivate Blogs\t\t",
    BlogsMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
    print '\t No user with Email ' + MAILADDRESS + ' found'

try:
    print "\tInactivate Communities\t\t",
    CommunitiesMemberService.inactivateMemberByEmail(MAILADDRESS.lower())
except:
    print '\t No user with Email ' + MAILADDRESS + ' found'

try:
    print "\tInactivate Dogear\t\t",
    DogearMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
    print '\t No user with Email ' + MAILADDRESS + ' found'

try:
    print "\tInactivate Files\t\t",
    FilesMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
    print '\t No user with Email ' + MAILADDRESS + ' found'

try:
    print "\tInactivate Forums\t\t",
    ForumsMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
    print '\t No user with Email ' + MAILADDRESS + ' found'

try:
    print "\tInactivate News, Search, Homepage ",
    NewsMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
    print '\t No user with Email ' + MAILADDRESS + ' found'

try:
    print "\tInactivate Wikis\t\t",
    WikisMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
    print '\t No user with Email ' + MAILADDRESS + ' found'

try:
    print '\tInactivate Profiles\t\t',
    ProfilesService.inactivateUser(MAILADDRESS)
except:
    print '\t No user with Email ' + MAILADDRESS + ' found'

print '\n\tActivate User: '

print '\t',
ProfilesService.activateUserByUserId(
    e['PROF_GUID'], email=e['PROF_MAIL'], uid=e['PROF_UID'])
print '\t',
ProfilesService.publishUserData(MAILADDRESS)
