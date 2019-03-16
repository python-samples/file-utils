from os import listdir
from os.path import isfile, join

# find the how many times the string 'Oops' shows up in the files from folder 'path'

path = "."

files = [f for f in listdir(path) if isfile(join(path, f))]

print(files)

oopses = {}

for f in files:
    parts = f.split("_")
    if len(parts) >= 2:
        hostname = parts[0]
        print(hostname)
        counter = 0
        with open(f) as ff:
            for l in ff:
                print(l)
                if "Oops" in l:
                    counter = counter + 1
        oopses[hostname] = counter


print(oopses)
