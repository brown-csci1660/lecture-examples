import cv2
import numpy as np
import sys
import os

img_path = sys.argv[1]
img_path = os.path.abspath(img_path)

IMAGE = cv2.imread(img_path)


SHAPE=IMAGE.shape




def gen_img_pair(bias):
    
    x_shape, y_shape, z_shape = SHAPE
    key = np.packbits(np.random.choice([0, 1], size=(8, x_shape, y_shape, z_shape), p=[1-(bias/100), 1-(1-(bias/100))])).reshape(SHAPE)
    cipher = cv2.bitwise_xor(key, IMAGE)
    # annotate
    key = cv2.putText(key, 'Key', (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3, cv2.LINE_AA)
    
    cipher = cv2.putText(cipher, 'Cipher', (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3, cv2.LINE_AA)
    cipher = cv2.line(cipher,(0,0),(0,y_shape),(0,255,0),5)
    

    return np.hstack((key, cipher))


print("computing...")
precompute_table = {bias : gen_img_pair(bias) for bias in range(101)}
print("done")


def on_change(value):
    cv2.imshow(windowName, precompute_table[value])


windowName = 'main' 


cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)

cv2.imshow(windowName, precompute_table[50])
cv2.createTrackbar('Bias Slider:', windowName, 50, 100, on_change)

cv2.waitKey(0)
cv2.destroyAllWindows()
