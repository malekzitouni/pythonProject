import cv2
from matplotlib import pyplot as plt
import numpy as np
path = r'C:\Users\T.M.S\OneDrive\Bureau\OPENCV tuto\MONA_LISA.JPG'
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale mode
_, mask = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
kernel=np.ones((3,3),np.uint8)
print(kernel)
dilatation=cv2.dilate(mask,kernel)
erosion=cv2.erode(mask,kernel)
title = ['Original Image', 'Binary Mask','dilatation','erosion']
images = [img, mask,dilatation,erosion]

for i in range(4):
    plt.subplot(1, 4, i + 1)
    plt.imshow(images[i], cmap='gray')  # Moved cmap='gray' to plt.imshow()
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])  # Hide axis ticks

plt.show()
