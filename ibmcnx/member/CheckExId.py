'''
Check ExId (GUID) by Email through JDBC

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       8.0.14
Date:          2026-08-21

License:       Apache 2.0

Check ExId of a User in all Connections Applications

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

email = raw_input("\n\tMail address of profile you want to check: ").lower()

sql = 'select PROF_UID_LOWER,PROF_MAIL_LOWER,PROF_GUID,PROF_MAIL from empinst.employee where PROF_MAIL_LOWER = \'' + \
    email + '\' order by PROF_UID_LOWER'
rs = stmt.executeQuery(sql)

employeeList = []
while (rs.next()):
    row = {}
    row['PROF_UID_LOWER'] = rs.getString(1)
    row['PROF_MAIL_LOWER'] = rs.getString(2)
    row['PROF_GUID'] = rs.getString(3)
    row['PROF_MAIL'] = rs.getString(4)
    employeeList.append(row)

rs.close()
stmt.close()
conn.close()

# print the result
for e in employeeList:
    # print e['PROF_UID_LOWER'] + "\t\t" + e['PROF_MAIL_LOWER'] + "\t\t" + e['PROF_GUID']
    # print e['PROF_MAIL']
    print "\tProfiles:\t\t\t " + e['PROF_GUID']

try:
    LOGIN = e['PROF_MAIL']
    go_on = 'true'
except:
    print '\tNo User with mail address ' + email
    go_on = 'false'

try:
    temp = ActivitiesMemberService.getMemberExtIdByLogin(LOGIN)
except:
    loadCNXCommands()

if go_on == 'true':
    try:
        print "\tActivities:\t\t\t",
        ActivitiesMemberService.getMemberExtIdByLogin(LOGIN)
    except:
        print '\tNo user with Login ' + LOGIN + ' found'

    try:
        print "\tBlogs:\t\t\t\t",
        BlogsMemberService.getMemberExtIdByLogin(LOGIN)
    except:
        print '\tNo user with Login ' + LOGIN + ' found'

    try:
        print "\tCommunities:\t\t\t",
        CommunitiesMemberService.getMemberExtIdByLogin(LOGIN)
    except:
        print '\tNo user with Login ' + LOGIN + ' found'

    try:
        print "\tDogear:\t\t\t\t",
        DogearMemberService.getMemberExtIdByLogin(LOGIN)
    except:
        print '\tNo user with Login ' + LOGIN + ' found'

    try:
        print "\tFiles:\t\t\t\t",
        FilesMemberService.getMemberExtIdByLogin(LOGIN)
    except:
        print '\tNo user with Login ' + LOGIN + ' found'

    try:
        print "\tForums:\t\t\t\t",
        ForumsMemberService.getMemberExtIdByLogin(LOGIN)
    except:
        print '\tNo user with Login ' + LOGIN + ' found'

    try:
        print "\tNews, Search, Homepage:\t\t",
        NewsMemberService.getMemberExtIdByLogin(LOGIN)
    except:
        print '\tNo user with Login ' + LOGIN + ' found'

    try:
        print "\tWikis:\t\t\t\t",
        WikisMemberService.getMemberExtIdByLogin(LOGIN)
    except:
        print '\tNo user with Login ' + LOGIN + ' found'
