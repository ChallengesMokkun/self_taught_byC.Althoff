import re

sen = "The ghost that says boo haunts the bamboo faffoo ranranroo ohshibaroo huloo"
mat = re.findall(".oo",sen)
for word in mat:
    print(word)
