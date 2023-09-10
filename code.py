import numpy as np
import matplotlib.pyplot as plt

# Define the dog emoji as a 2D array
dog_emoji = np.array([
    [0, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 0]
])

# Set the color of the dog emoji (1 = black, 0 = white)
dog_color = np.array([
    [1, 1, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1]
])

# Combine the dog emoji and color into a 3D array
dog_image = np.dstack([dog_emoji, dog_color, np.zeros_like(dog_emoji)])

# Display the image using matplotlib
plt.imshow(dog_image)
plt.show()
