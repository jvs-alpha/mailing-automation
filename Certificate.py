import cv2
import os
from PIL import Image
import json
import sys


def Certificate(image,posfile,name,id):
    img = cv2.imread(image)
    json_file = open(posfile,"r+")
    pos = json.load(json_file)
    cv2.putText(img,"NAME : {}".format(name),(pos["name"]["x"],pos["name"]["y"]),cv2.FONT_HERSHEY_TRIPLEX,2,(0,0,0),2,cv2.LINE_AA)
    img = Image.fromarray(img)
    img = img.convert("RGB")
    img.save(r"{}/images/{}.pdf".format(os.getcwd(),id))

if __name__ == "__main__":
    if(len(sys.argv) < 5):
        print("Try:")
        print("python3 Certificate.py <image> <position file> <name> <Register_ID>")
        sys.exit(0)
    Certificate(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
