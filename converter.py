import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries


def segmentation(img, filename, segment, compact, sigm):
    # img = imread('C:/Users/mores/AppData/Local/Programs/Python/Python37/Lib/site-packages/skimage/data/test.png')

    segments_slic = slic(img, n_segments=int(segment), compactness=int(compact), sigma=int(sigm))
    # print('SLIC number of segments: {}'.format(len(np.unique(segments_slic))))
    # print(mark_boundaries(img, segments_slic, color=(1, 1, 1)))
    plt.imsave("images/"+filename, mark_boundaries(img, segments_slic, color=(1, 1, 1)))


