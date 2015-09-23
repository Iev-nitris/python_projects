import datetime

__author__ = 'Ievgen'

# t = dict(('123_%d'%i, [1, 1, 2, 4]) for i in range(100))

def generate():
    baseString = "column %d"
    resList = list()
    for i in range(108):
        if i == 0:
            continue
        resList.append([baseString%i, i])
    return resList

def readFileGetList():
    resList = list()
    columns = {v[1]: v[0] if v[0] != "" else "" for k, v in enumerate(generate())}
    fileMy = open("heavyFile.dat", 'r')
    lineList = fileMy.readlines()
    trans = {k: v.split("|") if v != "" else "" for k, v in enumerate(lineList)}
    resssult = [{v: value[k] for k, v in columns.iteritems()} for value in trans.itervalues()]
    # {value: transValue for k, transValue in trans.itervalues() for key, value in columns.iteritems()}
    # for line in lineList:
    #     resDict = {value: line.split("|")[key] if value != "" else None for key, value in columns.iteritems()}
    #     resList.append(resDict)
    return resssult

print datetime.datetime.now()
print len(readFileGetList())
print datetime.datetime.now()
print ""


# generate()