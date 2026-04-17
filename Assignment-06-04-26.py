import cv2
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

# -------------------------------
# STEP 1: Open file picker
# -------------------------------
Tk().withdraw()  # Hide main window
file_path = filedialog.askopenfilename()

# -------------------------------
# STEP 2: Load image
# -------------------------------
image = cv2.imread(file_path)

# -------------------------------
# STEP 3: Check
# -------------------------------
if image is None:
    print("❌ Failed to load image")
else:
    print("✅ Image loaded successfully!")

    # Shape
    print("Shape:", image.shape)

    # Pixel values
    print("Pixel at (0,0):", image[0, 0])
    print("Pixel at (100,100):", image[100, 100])

    # Channels
    print("Channels:", image.shape[2])

    # Display image
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.title("Uploaded Image")
    plt.axis("off")
    plt.show()