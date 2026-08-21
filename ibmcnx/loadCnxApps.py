'''
Load all Connections commands in one step

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       8.0.14
Date:          2026-08-21

License:       Apache 2.0
'''

global globdict
globdict = globals()

execfile("activitiesAdmin.py", globdict)
execfile("blogsAdmin.py", globdict)
execfile("communitiesAdmin.py", globdict)
execfile("dogearAdmin.py", globdict)
execfile("filesAdmin.py", globdict)
execfile("forumsAdmin.py", globdict)
execfile("homepageAdmin.py", globdict)
execfile("newsAdmin.py", globdict)
execfile("profilesAdmin.py", globdict)
execfile("wikisAdmin.py", globdict)
