from os import listdir
from os.path import isfile, join
def dfile (path):
    mypath = path
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles
