import numpy as np

# Crop part of the image, pad with nan if target size is bigger than input image
def crop(input_image, target_width=1024, target_height=512, x0=0, z0=0):
    # Get the dimensions of the input image
    input_height, input_width = input_image.shape[:2]

    # Calculate the cropping region
    x1 = min(input_width, x0 + target_width)
    z1 = min(input_height, z0 + target_height)

    # Crop the image
    cropped_image = input_image[z0:z1, x0:x1]

    # Add padding as needed to reach target width and height
    pad_width = ((0, max(0, target_height - (z1 - z0))), (0, max(0, target_width - (x1 - x0))), (0, 0))
    cropped_image_padded = np.pad(cropped_image, pad_width, mode='constant', constant_values=np.nan)

    return cropped_image_padded
