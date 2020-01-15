from WriteDB import *
from Certificate import *
from MailService import *
from RegisterNo import *
import os
import sys
import csv

def SendScript(csv_raw):
    f = open(csv_raw,newline="")
    csvdata = csv.reader(f,delimiter=",",quotechar="|")
    check = 0
    for data in csvdata:
        if check == 0:
            check = 1
            continue
        print("name : {} {}".format(data[0],data[1]))
    f.close()
if __name__ == "__main__":
    SendScript(sys.argv[1])
