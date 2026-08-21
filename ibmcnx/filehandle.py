'''
Classes to create files

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       8.0.14
Date:          2026-08-21

License:       Apache 2.0

Create Files for Backups, Log-Messages and so on
'''

import os.path


class Ibmcnxfile:

    def __init__(self):
        print "Initialize Ibmcnxfile"
        self.createFile()

    def askFileParams(self):
        # function to create file
        folderquestion = "Directory to store the file: "
        folder = raw_input(folderquestion)
        filequestion = "Filename: "
        filename = raw_input(filequestion)
        fileopen = folder + "/" + filename
        return fileopen

    def createFile(self):
        fileopen = self.askFileParams()
        if (os.path.isfile(fileopen)):
            answer = raw_input(
                "File exists, Overwrite, Append or Abort? (O|A|X)").lower()
            if answer == "o":
                self.file = open(fileopen, 'w')
            elif answer == "a":
                self.file = open(fileopen, 'a')
            else:
                print "Exit"
                exit()
        else:
            self.file = open(fileopen, 'w')

    def writeToFile(self, string):
        self.file.write(string + "\n")

    def closeFile(self):
        self.file.flush
        self.file.close()
