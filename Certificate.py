import cv2
import numpy as np
import json
import sys


def Certificate(image,posfile,name):
    img = cv2.imread(image)
    json_file = open(posfile,"r+")
    pos = json.load(json_file)
    cv2.putText(img,name,(pos["name"]["x"],pos["name"]["y"]),cv2.FONT_HERSHEY_TRIPLEX,1,(0,0,0),2,cv2.LINE_AA)
    cv2.putText(img,"NRIC",(450,444),cv2.FONT_HERSHEY_TRIPLEX,1,(0,0,0),2,cv2.LINE_AA)
    cv2.imshow("Test",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if(len(sys.argv) < 4):
        print("Try:")
        print("python3 Certificate.py <image> <position file> <name>")
        sys.exit(0)
    Certificate(sys.argv[1],sys.argv[2],sys.argv[3])
