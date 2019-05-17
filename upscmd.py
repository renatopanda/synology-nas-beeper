#!/bin/python2
import sys
import telnetlib

user = "<upsd_username>"
pwd = "<upsd_pwd>"

if len(sys.argv) == 2:
    cmd = sys.argv[1]
else:
    print("the ups command to issue is missing.")
    print("example: upscmd.py beeper.enable")
    exit(1)
    

tn = telnetlib.Telnet("127.0.0.1", 3493)

tn.write("USERNAME {0}\n".format(user))
response = tn.read_until("OK", timeout=2)
print "USERNAME cmd status: {0}".format(response.strip())

tn.write("PASSWORD {0}\n".format(pwd))
response = tn.read_until("OK", timeout=2)
print "PASSWORD cmd status: {0}".format(response.strip())

tn.write("INSTCMD ups {0}\n".format(cmd))
response = tn.read_until("OK", timeout=2)
print "INSTCMD cmd status: {0}".format(response.strip())

tn.write("LOGOUT\n")
print tn.read_all()

