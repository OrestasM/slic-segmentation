from PIL import Image
from io import BytesIO
import base64
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import sobel
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from slide import open_slide
from skimage.io import imread
import time
import os

def segmentation(img, filename, segment, compact, sigm):
    # img = imread('C:/Users/mores/AppData/Local/Programs/Python/Python37/Lib/site-packages/skimage/data/test.png')

    segments_slic = slic(img, n_segments=int(segment), compactness=int(compact), sigma=int(sigm))
    # print('SLIC number of segments: {}'.format(len(np.unique(segments_slic))))
    # print(mark_boundaries(img, segments_slic, color=(1, 1, 1)))
    plt.imsave("images/"+filename, mark_boundaries(img, segments_slic, color=(1, 1, 1)))


