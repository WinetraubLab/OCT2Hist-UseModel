import utils.pix2pix as pix2pix
import cv2
import numpy as np

# Run this function to set up the Neural Network with Pre-trained segment skin network
def setup_network():
  pix2pix.setup_network("/content/drive/Shareddrives/Yolab - Current Projects/_Datasets/2023-09-05 SegmentSkin/latest_net_G.pth","segment_skin")

# This function evaluates the neural network on input image
# Inputs:
#   oct_image - input oct image in cv format (256x256x3). Input image should be scanned with 10x lens and z-stacked
# Outputs:
#   mask - specifying for each pixel is it inside tissue (true) or outside tissue (false)
def run_network (oct_image):
  # Rescale
  input_image = cv2.resize(oct_image, [256,256] , interpolation=cv2.INTER_AREA)
  
  # Run the neural net
  mask_image = pix2pix.run_network(input_image,"segment_skin", netG_flag="")

  # Convert the color image to grayscale and filter to bolean
  boolean_image = cv2.cvtColor(mask_image, cv2.COLOR_BGR2GRAY) > 127

  return boolean_image
