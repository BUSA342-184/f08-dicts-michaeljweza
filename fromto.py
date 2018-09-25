#! /opt/bin/python
"""
Read through email files from mbox-short.txt
Grab only email addresses with 'From: ' and 'To: '
Second split: Separate email addresses into Username and the Hostname.
Finally, your program should use dictonaries to count the following:
    usernames in the From: field
    hosts in the From: field
    usernames in the To: field
    hosts in the To: field
"""

import sys
import csv

# http://www.py4e.com/code/mbox-short.txt
# The text filesource:
fhand = open('mbox-short.txt')
count = 0

# create dictionaries
fromUserD = {}
toUserD = {}
fromHostD = {}
toHostD = {}

for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'): 
        count += 1
        email = line.split()[1]
        userF = email.split("@")[0]
        hostF = email.split("@")[1]
        # use dictionaries
        fromUserD[userF]= fromUserD.get(userF, 0) + 1
        fromHostD[hostF]= fromHostD.get(hostF, 0) + 1

    if line.startswith('To:'):
        count += 1
        email = line.split()[1]
        userT = email.split("@")[0]
        hostT = email.split("@")[1]
        
        # use dictionaries
        toUserD[userT]= toUserD.get(userT, 0) + 1
        toHostD[hostT]= toHostD.get(hostT, 0) + 1

# connect a csv.writer filehandle to STDOUT
cw = csv.writer(sys.stdout)

# write an output header
print('--- FROM USER ---')
# fromUserD is a dict() whose key and value pairs are usernames and counts
cw.writerows(sorted(fromUserD.items()))

print('--- FROM HOST ---')
# fromUserD is a dict() whose key and value pairs are usernames and counts
cw.writerows(sorted(fromHostD.items()))

print('--- TO USER ---')
# fromUserD is a dict() whose key and value pairs are usernames and counts
cw.writerows(sorted(toUserD.items()))

print('--- TO HOST ---')
# fromUserD is a dict() whose key and value pairs are usernames and counts
cw.writerows(sorted(toHostD.items()))
