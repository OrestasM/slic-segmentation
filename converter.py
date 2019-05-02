import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries

def segmentation(img, filename, segment, compact, sigm):
    """
    This is where segmentation happens. segmentation function takes image, filename for saving an image,
    Salso takes three options: segments, compactness, sigma. These three options are set on working window, when
    user selects wanted options and presses "Set" button.
    """
    segments_slic = slic(img, n_segments=int(segment), compactness=int(compact), sigma=int(sigm))
    plt.imsave("images/"+filename, mark_boundaries(img, segments_slic, color=(1, 1, 1)))