def dele(key):
    myDict.pop(key)
    print(myDict)
myDict = {'java':100,'python':20,'c':300, 20:22, 32:42}
dele('java')
dele('python')
