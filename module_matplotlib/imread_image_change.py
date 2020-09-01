"""
# Filling holes in outline text - by Steve Eddins, October 10, 2016
"""
# https://blogs.mathworks.com/steve/2016/10/10/filling-holes-in-outline-text/

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import imread_image_change as myself         # self for object get

func_names = [func_name
                for func_name in dir(myself)
                if func_name.startswith("run")]

dirs = os.path.dirname(__file__).partition('module_matplotlib')
dir_home = "".join(dirs[:2]) + '\\'
dir_img = dir_home + 'statics\\'

def main():
    # execute_with_doc(obj=myself, method_name_str='run_02_2')
    [execute_with_doc(myself, func_name) for func_name in func_names]
    pass


def get_cut_dir(name_cut:str) -> str:
    dir_hereent = os.path.dirname(__file__)
    dir_cut = "".join(dir_hereent.partition(name_cut)[:2])
    return dir_cut


def run_01():
    """01.show imread original image from 'url_target'
    # https://blogs.mathworks.com/steve/files/MathWorks-address-binary.png
    """
    url_target = 'http://bit.ly/2Bp2elu'   # img URL
    bw = plt.imread(dir_img + 'MathWorks-address-binary.png')
    bw = plt.imread(url_target)
    plt.imshow(bw)
    plt.show()

def run_02_1():
    """02-1.ERROR = imfill() is MATLAB function --> refer run_03
    # How can we fill in the text characters from their outlines without
    # filling in the internal holes? If we just use imfill with the 'holes'
    # option, you can see that it doesn't give us the desired result.
    """
    # bw = plt.imread(dir_img + 'MathWorks-address-binary.png')
    # bw_filled = plt.imfill(bw,'holes')
    bw_filled = plt.imread(dir_img + 'MathWorks-address-binary.png')
    plt.imshow(bw_filled)
    plt.title('Original with holes filled')
    plt.show()

def run_02_2():
    """02-2.Error: 'matplotlib.pyplot' has no attribute 'imclearborder'
    # When I saw this problem, I thought that some combination of imfill,
    # imclearborder, and logical operators could possibly solve it.
    # You've already seen imfill. Here's how imclearborder works.
    # You can see that any connected component touching any image border
    # has been removed.
    """
    url_sample = 'https://blogs.mathworks.com/images/steve/168/aug31.png';
    bw_sample = plt.imread(url_sample);
    plt.imshow(bw_sample)
    plt.title('imclearborder demonstration - input image')
    plt.show()

    # bw_sample_clearborder = plt.imclearborder(bw_sample);
    bw_sample_clearborder = bw_sample
    plt.imshow(bw_sample_clearborder)
    plt.title('imclearborder demonstration - output image')
    plt.show()

def run_03():
    """03. Filling holes in an image using OpenCV ( Python / C++ )
    # by. Satya Mallick - Nov. 23, 2015
    # https://www.learnopencv.com
    # /filling-holes-in-an-image-using-opencv-python-c/
    """

    im_in = cv2.imread(
                    dir_img + "/statics/nickel_338x338.png",
                    # dir_img + 'MathWorks-address-binary.png',
                    cv2.IMREAD_GRAYSCALE,
                    )
    # Threshold.
    # Set values equal to or above 220 to 0.
    # Set values below 220 to 255.

    _, im_th = cv2.threshold(im_in, 220, 255, cv2.THRESH_BINARY_INV)

    # Copy the thresholded image.
    im_floodfill = im_th.copy()

    # Mask used to flood filling./
    # Notice the size needs to be 2 pixels than the image.
    h, w = im_th.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)

    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (0,0), 255)

    # Invert floodfilled image
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)

    # Combine the two images to get the foreground.
    im_out = im_th | im_floodfill_inv

    # Display images.
    cv2.imshow("The Origibal Image", im_in)
    cv2.imshow("Thresholded Image", im_th)
    cv2.imshow("Floodfilled Image", im_floodfill)
    cv2.imshow("Inverted Floodfilled Image", im_floodfill_inv)
    cv2.imshow("Foreground", im_out)
    cv2.waitKey(0)

def execute_with_doc(obj, method_name_str):
    """HELPER() for main()"""
    func = getattr(obj, method_name_str)
    print(func.__doc__)
    func()



if __name__ == '__main__':
    print(__doc__)
    main()
