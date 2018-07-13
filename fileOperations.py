import os

def getParameters():
    cwd = os.getcwd()
    #print(cwd)
    fileName = "spatialInfo.txt"
    #print(cwd + '\\' + fileName)

    file = open(cwd + '\\' +fileName, 'r')
    values = list()
    while True:
        msg = file.readline()
        if (msg == ''):
            break
        msg = msg.rstrip()
        splitPart = msg.split(" = ")
        #print(splitPart[0])
        #print(splitPart[1])
        values.append([splitPart[0], splitPart[1]])
    #print(values)
    
    return values

getParameters()
