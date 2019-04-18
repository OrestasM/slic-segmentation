
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import base64
# from skimage.data import test
from skimage.color import rgb2gray
from skimage.filters import sobel
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from slide import open_slide
from skimage.io import imread
import converter

# img = img_as_float(astronaut()[::1, ::1])
img = imread('C:/Users/mores/AppData/Local/Programs/Python/Python37/Lib/site-packages/skimage/data/test.png')

segments_slic = slic(img, n_segments=256, compactness=10, sigma=1)

print('SLIC number of segments: {}'.format(len(np.unique(segments_slic))))

# plt.imsave("test.png", mark_boundaries(img, segments_slic))

buff = BytesIO()
plt.imsave("test.jpeg", mark_boundaries(img, segments_slic, color=(1, 1, 0)))




print(converter.im_2_b64("C:/Users/mores/Desktop/Tiff pyramids/tiff/test.jpeg"))
