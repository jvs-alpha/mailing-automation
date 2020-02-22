import cv2
import os
from PIL import Image
import json
import sys
import datetime

def Certificate(name,id,date=None):
    img = cv2.imread("cert.jpg")
    with open("Positions/NamePosition.json","r") as json_file:
        name_pos = json.load(json_file)
    with open("Positions/DatePosition.json","r") as json_file:
        date_pos = json.load(json_file)
    with open("Positions/IDPosition.json","r") as json_file:
        id_pos = json.load(json_file)
    cv2.putText(img,"NAME : {}".format(name),(name_pos["name"]["x"],name_pos["name"]["y"]),cv2.FONT_HERSHEY_TRIPLEX,2,(0,0,0),2,cv2.LINE_AA)
    if date:
        cv2.putText(img,str(date),(date_pos["name"]["x"],date_pos["name"]["y"]),cv2.FONT_HERSHEY_TRIPLEX,.80,(0,0,0),1,cv2.LINE_AA)
    else:
        cv2.putText(img,str(datetime.datetime.utcnow().date()),(date_pos["name"]["x"],date_pos["name"]["y"]),cv2.FONT_HERSHEY_TRIPLEX,.80,(0,0,0),1,cv2.LINE_AA)
    cv2.putText(img,id,(id_pos["name"]["x"],id_pos["name"]["y"]),cv2.FONT_HERSHEY_TRIPLEX,.80,(0,0,0),1,cv2.LINE_AA)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img.save(r"{}/images/{}.jpg".format(os.getcwd(),id))

if __name__ == "__main__":
    Certificate(sys.argv[1],sys.argv[2])
