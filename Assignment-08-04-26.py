import cv2
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

Tk().withdraw()
file_path = filedialog.askopenfilename()

image = cv2.imread(file_path)

if image is None:
    print("❌ Failed to load image")
    exit()


image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


blur = cv2.GaussianBlur(gray, (9,9), 0)


edges = cv2.Canny(blur, 100, 200)


plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")


plt.subplot(2, 2, 2)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale")
plt.axis("off")

# Blurred
plt.subplot(2, 2, 3)
plt.imshow(blur, cmap='gray')
plt.title("Blurred Image")
plt.axis("off")


plt.subplot(2, 2, 4)
plt.imshow(edges, cmap='gray')
plt.title("Edge Detection (Canny)")
plt.axis("off")

plt.tight_layout()
plt.show()