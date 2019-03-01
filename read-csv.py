from os import listdir
import os
from os.path import isfile, join

if __name__ == '__main__':
    mypath = 'company-reports'
    # email = {
    #     'COGENT': 'test@test.com',
    #     'FULLTIMER': 'test1@test.com',
    #     'TOTHENEW': 'test2@test.com',
    #     'PENNYWISE': 'test3@test.com',
    #     'IGS': 'test4@test.com',
    # }
    onlyfiles = os.listdir(mypath)
    if (len(onlyfiles) > 0):
        for item in onlyfiles:
            switcher = {
            
            }
