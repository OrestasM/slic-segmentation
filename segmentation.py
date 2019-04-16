import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage.data import astronaut
from skimage.color import rgb2gray
from skimage.filters import sobel
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from slide import open_slide
from skimage.io import imread

img = img_as_float(astronaut()[::2, ::2])


segments_slic = slic(img, n_segments=250, compactness=10, sigma=1)

print('SLIC number of segments: {}'.format(len(np.unique(segments_slic))))

plt.imshow(mark_boundaries(img, segments_slic))
plt.tight_layout()

plt.show()