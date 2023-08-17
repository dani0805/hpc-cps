import time
import dask.array as da
from skimage import io, transform
from dask.distributed import Client

client = Client("tcp://localhost:8786")

# Create a Dask array with the size of your images
images = da.random.uniform(size=(20, 2160, 3840, 3), chunks=(1, 2160, 3840, 3))

def rescale_image(image):
    return transform.resize(image, (1, 540, 960, 3))

now = time.time()

# We use the Dask map_blocks function to apply the function to each image in our dataset
rescaled_images = images.map_blocks(rescale_image, dtype=float)

# Trigger computation
output = rescaled_images.compute()

print(output.shape)
print(f"Rescaled {len(output)} images in {time.time() - now} seconds")

client.close()

# compare this to the serial implementation
now = time.time()
rescaled_images = []
for image in images:
    print("#", end="")
    rescaled_images.append(rescale_image(image[None, ...]))
print()
print(f"Rescaled {len(rescaled_images)} images in {time.time() - now} seconds")
