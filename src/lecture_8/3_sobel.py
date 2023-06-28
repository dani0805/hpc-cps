import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

# Load the image
pilimg = Image.open('skyscraper.png')
# convert to numpy array
img = np.asarray(pilimg)
img_orig = img.copy()

def convolve2d(I, h):
    # Manual 2D convolution with 3x3 filter
    output = np.zeros_like(I)  # Create an empty matrix of the same shape as I
    for x in range(1, I.shape[1] - 1):  # For each column
        for y in range(1, I.shape[0] - 1):  # For each row
            # Element-wise multiplication of the filter and the image
            output[y, x] = np.sum(I[y - 1:y + 2, x - 1:x + 2] * h)
    return output


# Ensure the image is grayscale
if img.ndim == 3:
    img = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140]) # grayscale conversion

# reduce the size of the image to speed up computation
img = img[::4, ::4]

# normalize the image to be between 0 and 1 and use min-max scaling
img = (img - np.min(img)) / (np.max(img) - np.min(img))

# Define the Sobel filters
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Apply the filters to the image
filtered_x = np.abs(convolve2d(img, sobel_x))
filtered_y = np.abs(convolve2d(img, sobel_y))


# Combine the filters
filtered = np.hypot(filtered_x, filtered_y)

# Normalize
filtered *= 255.0 / np.max(filtered)

# Use conditional indexing to create a binary mask of the most prominent edges
mask = filtered > 80  # adjust threshold as needed

# find the bounding box of the mask
y_idx, x_idx = np.nonzero(mask)
y1, x1 = np.min(y_idx)*4, np.min(x_idx)*4
y2, x2 = np.max(y_idx)*4, np.max(x_idx)*4

# Display the original image and the mask
plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
# plot the bounding box
plt.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], 'ro--')
plt.imshow(img_orig, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(mask, cmap='gray')
plt.title('Edge Detection')
plt.axis('off')

plt.show()
