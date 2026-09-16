dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

mergeddict = dict1 | dict2
print("Method 1 (Pipe):",mergeddict)

unpackeddict = {**dict1, **dict2}
print("Method 2 (Unpacking):",unpackeddict)

copydict = dict1.copy()
copydict.update(dict2)
print("Method 3 (Update):",copydict)
