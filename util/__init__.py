import numpy as np

def transform_image_to_coordinates(image:np.ndarray):
    """
    Transforms an image array into a 2D array with columns for X, Y coordinates and RGB values.
    Parameters:
    - image: A NumPy array of shape (height, width, 3) representing an RGB image.
    Returns:
    - A 2D NumPy array of shape (height*width, 5) where each row contains [X, Y, R, G, B].
    """
    # Get the dimensions of the image
    height, width, _ = image.shape
    # Generate the X and Y coordinate grids
    X, Y = np.meshgrid(range(width), range(height))
    # Flatten the X, Y, and image arrays to create 1D arrays
    X_flat = X.flatten()
    Y_flat = Y.flatten()
    image_flat = image.reshape(-1, 3)  # Flatten the image while keeping the RGB channels grouped
    # Concatenate the flattened X, Y, and image arrays
    transformed_data = np.column_stack((X_flat, Y_flat, image_flat))
    return transformed_data

def transform_coordinates_to_image(data):
    # Automatically determine the dimensions
    width = int(np.max(data[:, 0])) + 1
    height = int(np.max(data[:, 1])) + 1
    
    # Create an empty image
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Use indexing to place colors - much faster than looping
    x_coords = data[:, 0].astype(int)
    y_coords = data[:, 1].astype(int)
    image[y_coords, x_coords] = data[:, 2:5]
    
    return image