import numpy as np
import cv2
import os
import sys

if (len(sys.argv) != 3):
    print(f"Usage: {sys.argv[0]}, <image1-path> <image2-path>")
    exit(1)


img1_path = sys.argv[1]
img2_path = sys.argv[2]
img1_path = os.path.abspath(img1_path)
img2_path = os.path.abspath(img2_path)


img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

assert img1.shape == img2.shape


cv2.imshow('image 1', img1)
cv2.imshow('image 2', img2)

key = np.random.randint(255, size=img1.shape,dtype=np.uint8)

cv2.imshow('KEY', key)
cv2.waitKey(0)
cv2.destroyAllWindows()


# FIRST IMAGE


encryptImg1 = cv2.bitwise_xor(img1, key)
cv2.imshow('image 1', img1)
cv2.imshow('Encrypt Image 1',encryptImg1)
cv2.waitKey(0)


# SECOND IMAGE


encryptImg2 = cv2.bitwise_xor(img2, key)
cv2.imshow('image 2', img2)
cv2.imshow('Encrypt Image 2',encryptImg2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# OVERLAY FLAW

encryptBoth = cv2.bitwise_xor(encryptImg1, encryptImg2)
cv2.imshow('Encrypt Both',encryptBoth)

key_xor = cv2.bitwise_xor(key, key)
cv2.imshow('key encrypt', key_xor)
cv2.waitKey(0)
cv2.destroyAllWindows()
