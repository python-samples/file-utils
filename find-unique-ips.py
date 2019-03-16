with open("hosts.txt", "r") as ins:
    array = []
    for line in ins:
#        print(line)
        ip = line.split()[0]
        print(ip)
        if ip.startswith("#"):
            print("skipping {0} as it is commented out".format(ip))
        else:
            if (":" in ip):
                print("skipping {0} as it seems to be ipv6".format(ip))
            else:
                array.append(ip)
uniqueIps = set(array)
print(uniqueIps)
