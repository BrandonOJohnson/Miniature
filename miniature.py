# -*- coding: utf-8 -*-
"""
Brandon Johnson
Rollins ID: bjohnson1

Charles Mason
Rollins ID: cmason

“On my honor, I have not given, nor received, nor witnessed any unauthorized
 assistance on this work.”
 
Collaboration Statement:
    
"We have not recieved any assistance on this work"
"""
import cv2
import numpy as np
import scipy as sp

def blur_top(image):
    
    """ This function generates a gradient blur in the y direction using a 
    3X3 kernel with a 1/9 from the top of the image to the center
    
    the blur gradually gets less intense as it travels to the middle

    iterate through the image manually using kernel and gradually increasing 
    the blur by decreasing number of rows the kernel is used on

    Args:
        image (numpy.ndarray): A color image represented in a numpy array.

    Returns:
        output (numpy.ndarray): increasing intensified blur towards the top.
    """
    
    img = image.copy()
    
    new_image = image.copy()
    kernel = np.ones((3, 3))/9
    
    row, col, channel = img.shape
    
    num1 = 1.8
    
    #increase blur image transitions to upper-most region
    #reiterates to create blurier effect throughout each iteration
    #3 is arbitrary amount 
    
    for x in range(3):
        for r in range(1, int(round(row//num1))):
            for c in range(1, col-1):
                sum = 0
                for kr in range(-1, 2):
                    for kc in range(-1, 2):
                    #get the new point from combination of kernel and original image 
                        sum += (new_image[r+kr][c+kc])*(kernel[kr+1][kc+1])
                new_image[r][c] = sum
        num1 += 0.4
        
    return new_image

def blur_bottom(image):
    
    """
    This function generates a gradient blur in the y direction using a 
    3X3 kernel with a 1/9 from the bottom of the image towards the center
    
    the blur gradually gets less intense as it travels to the middle

    iterate through the image manually using kernel and gradually increasing 
    the blur by increasing the starting row throughout each iteration

    Args:
        image (numpy.ndarray): A color image represented in a numpy array.

    Returns:
        output (numpy.ndarray): increasing intensified blur towards the bottom.
    """
    
    img = image.copy()
    
    new_image = image.copy()
    kernel = np.ones((3, 3))/9
    
    row, col, channel = img.shape
    
    num2 = 1.4
    
    #increase blur image transitions to lower-most region
    #reiterates to create blurier effect throughout each iteration
    #3 is arbitrary amount
    
    
    for x in range(3):
        for r in range(int(round(row//num2)), row-1):
            for c in range(1, col-1):
                sum = 0
                for kr in range(-1, 2):
                    for kc in range(-1, 2):
                    #get the new point from combination of kernel and original image 
                        sum += (new_image[r+kr][c+kc])*(kernel[kr+1][kc+1])
                new_image[r][c] = sum
        num2 -= 0.1
    
    return new_image
    
def miniatures(image):
    
    """
    This function calls both the blur_bottom and blur_top functions in order 
    in order to generate a composit that conveys the input image with varying 
    degrees of intensity in blur as it traverses to the top and bottom portions

    Args:
        image (numpy.ndarray): A color image represented in a numpy array.

    Returns:
        output (numpy.ndarray): The image depicting a fake miniature by use of 
        gradient blur
    """

    new_image = image.copy()

    new_image = blur_top(new_image)
    new_image = blur_bottom(new_image)
       
    return new_image

