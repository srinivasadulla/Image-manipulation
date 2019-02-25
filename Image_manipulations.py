# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 14:56:53 2019

@author: sinu2
"""
# Code is divided into 3 sections
# 1.Rotation
# 2.Scaling
# 3.Cropping



#Image Manipulations in OpenCV
import numpy as np
import cv2

#Load Image

Original_image = cv2.imread("Image.jpg")

#Display image
cv2.imshow("Original_image",Original_image)

################# ROTATION ###########################

#Rotate image by 180 degrees
angle = 60  #in degrees
scale = 1  #Scale factor
(u,v) = Original_image.shape[:2]

center = (v//2,u//2)

#Get Affine Rotation Matrix

rotation_matrix = cv2.getRotationMatrix2D(center,angle,scale)

# We need to translate the image inorder to display the image completely without any cuts after rotating.

cos = np.abs(rotation_matrix[0,0])
sin = np.abs(rotation_matrix[0,1])


frame_w = int((u*sin)+(v*cos))
frame_h = int((u*cos)+(v*sin))

rotation_matrix[0,2] += ((frame_w/2)-center[0])
rotation_matrix[1,2] += ((frame_h/2)-center[1])

#Apply Affine Transformation to original image

rotated = cv2.warpAffine(Original_image,rotation_matrix,(frame_w,frame_h))

# Display rotated image
cv2.imshow("Rotated Image",rotated)
cv2.imwrite("Rotated_image.jpg",rotated)

######################################################


################### SCALING ##########################

#The above rotation section can be used to scale the image, by inputing 0 degrees as angle and desired scale factor.

#To scale the image to desired number of pixels, use the following code

#lets say the image is to be scaled to 500 pixels wide.

new_width = 1000  # New image width

w_ratio = float(new_width)/Original_image.shape[1]

N_pixel = (int(Original_image.shape[1]*w_ratio),int(Original_image.shape[0]*w_ratio))

resize = cv2.resize(Original_image,N_pixel,interpolation = cv2.INTER_LINEAR)

cv2.imshow("resized",resize)

cv2.imwrite("Resized_image.jpg",resize)

######################################################


################### CROPPING ##########################

#Cropping is easy, just select the pixels to be cropped from original image

crop = Original_image[:,1980/2:1980]

cv2.imshow("Cropped",crop)
cv2.imwrite("Cropped_image.jpg",crop)

cv2.waitKey(0)