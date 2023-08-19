#!/usr/bin/python3
"""print names in a loop"""
names = ['Ndi', 'Nfor', 'Ngeh', 'Ngah']
for name in names:
    #if name == 'Ndi':
        print(name)
print("printing thesame numbers name with there corresponding index")

for name in range(len(names)):
    print(name, names[name])
