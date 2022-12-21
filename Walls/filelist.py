from os import listdir
from os.path import isfile, join
import json
files = [f for f in listdir('C:\code') if isfile(join('C:\code', f))] 
files = sorted(files, key=lambda s: s.lower())
res = []
for i in files:
    res.append({
        "name": i,
        "filename": i
    })
with open("result.json", "w") as outfile:
    json.dump(res, outfile)
print(res)