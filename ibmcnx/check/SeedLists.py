'''
Check if seedlists are available, seedlists are very important for search

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de


License:       Apache 2.0

'''

global globdict
globdict = globals()

# some variable definitions
applications = ['activities', 'blogs', 'communities',
                'dogear', 'files', 'forums', 'profiles', 'wikis']
seed_valid = []
seed_error = []


def main():
    # Load Connections Search Commands
    execfile("searchAdmin.py", globdict)

    for app in applications:
        '''
        Returncodes of validateSeedlist:
        CLFRW0262I = Successful
        CLFRW0263I = Error
        '''
        try:
            response = SearchService.validateSeedlist(app)
        except:
            print 'Problem getting seedlist of ' + app

        if response.split(':')[0] == 'CLFRW0262I':
            seed_valid.append(app)
        else:
            seed_error.append(app)

    # Print apps with errors and successful apps
    if len(seed_valid) >= 1:
        print "\n\tSeedlist validation SUCCESSFUL for: \n"
        for i in seed_valid:
            print "\t\t" + i

    if len(seed_error) >= 1:
        print "\n\tSeedlist with ERRORS: \n"
        for i in seed_error:
            print "\t\t" + i

main()
