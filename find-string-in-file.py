#!/usr/bin/env python3

hosts = "/etc/hosts"
try:
  if "localhost" in open(hosts).read():
    print("localhost has been located")
except PermissionError:
  print("File {} is not readable".format(hosts))
except OSError as err:
  print("Unknown error occurred:")
  print(err)
