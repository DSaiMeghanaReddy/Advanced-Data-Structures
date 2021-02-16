def get_key(val):
    for key, value in myDict.items():
        if val == value:
            return "success"
    return "key doesn't exist"
myDict = {'java':100,'python':20,'c':300, 20:22, 32:42}

print(get_key(100))
print(get_key(20))
print(get_key(67))
