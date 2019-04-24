from skimage import data
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

    image = io.imread('https://www.bmw.co.uk/model-selection/image-thumb__16852__960x540/2Series_Coupe_1920x1080.jpeg?1549294935')
    plt.imshow(image)