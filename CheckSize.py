import cv2
import sys

img = cv2.imread(sys.argv[1])
print("Size of the Image is {}".format(img.shape[:2]))
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
