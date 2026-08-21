'''
Inactivate a user in all applications

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0
'''

# Only load commands if not initialized directly (call from menu)
if __name__ == "__main__":
    execfile("ibmcnx/loadCnxApps.py")

MAILADDRESS = raw_input('Mailaddress to deactivate User: ')

try:
    print "Inactivate Activities ",
    ActivitiesMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
    print 'No user with Email ' + MAILADDRESS + ' found'

try:
    print "Inactivate Blogs ",
    BlogsMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
    print 'No user with Email ' + MAILADDRESS + ' found'

try:
    print "Inactivate Communities ",
    CommunitiesMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
    print 'No user with Email ' + MAILADDRESS + ' found'

try:
    print "Inactivate Dogear ",
    DogearMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
    print 'No user with Email ' + MAILADDRESS + ' found'

try:
    print "Inactivate Files ",
    FilesMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
    print 'No user with Email ' + MAILADDRESS + ' found'

try:
    print "Inactivate Forums ",
    ForumsMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
    print 'No user with Email ' + MAILADDRESS + ' found'

try:
    print "Inactivate News, Search, Homepage ",
    NewsMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
    print 'No user with Email ' + MAILADDRESS + ' found'

try:
    print "Inactivate Wikis ",
    WikisMemberService.inactivateMemberByEmail(MAILADDRESS)
except:
    print 'No user with Email ' + MAILADDRESS + ' found'

try:
    print 'Inactivate Profiles ',
    ProfilesService.inactivateUser(MAILADDRESS)
except:
    print 'No user with Email ' + MAILADDRESS + ' found'
