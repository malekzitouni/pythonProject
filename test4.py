import cv2
from matplotlib import pyplot as plt
import numpy as np
path = r'C:\Users\T.M.S\OneDrive\Bureau\OPENCV tuto\MONA_LISA.JPG'
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)  # Read the image in grayscale mode
_, mask = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
kernel=np.ones((2,2),np.uint8)
dilatation=cv2.dilate(mask,kernel)

title = ['Original Image', 'Binary Mask','dilatee']
images = [img, mask,dilatation]

for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], cmap='gray')  # Moved cmap='gray' to plt.imshow()
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])  # Hide axis ticks

plt.show()
