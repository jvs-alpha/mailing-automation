from Certificate import *
import csv

if __name__ == "__main__":
    with open("ANNEXURE_1.csv","r") as csv_raw:
        datas = list(csv.reader(csv_raw,delimiter=",",quotechar="|"))
    datas.pop(0)
    check = 0
    for data in datas:
        check += 1
        if check < 10:
            cid = "WS02202000"+str(check)
        else:
            cid = "WS0220200"+str(check)
        Certificate(data[1],cid,"05.02.2020-06.02.2020")
        print("Certificate Generated for {} : {}".format(data[1],cid))
