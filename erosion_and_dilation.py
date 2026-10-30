# Implementation of Erosion and Dilation Using OpenCV
# Developed By: Subashini K
# Register No: 212225240160

import cv2
import matplotlib.pyplot as plt

# 1. Original Image
img = cv2.imread("city.jpg")
if img is None:
    img = cv2.imread("nature.jpeg")

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")
plt.show()

# 2. Erosion
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
erosion = cv2.erode(img, kernel, iterations=1)
plt.imshow(erosion, cmap="gray")
plt.title("Image Erosion")
plt.axis("off")
plt.show()

# 3. Dilation
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dilation = cv2.dilate(img, kernel, iterations=1)
plt.imshow(dilation, cmap="gray")
plt.title("Image Dilation")
plt.axis("off")
plt.show()
