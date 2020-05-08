from os import listdir
from os.path import isfile, join

mypath = 'E:/dathena-competition/files/Keppel'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print(onlyfiles)

def GetFilesInFolder(path):
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for file in onlyfiles:
        fileS = file.split('.')
        fileExt = fileS[len(fileS) - 1]
        print(fileExt)

def getFileExt(file):
    fileS = file.split('.')
    fileExt = fileS[len(fileS) - 1]
    return fileExt
#GetFilesInFolder(mypath)