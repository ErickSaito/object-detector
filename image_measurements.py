from image_manager import ImageManager
import cv2 as cv
import numpy as np

class ImageMeasurements():
  def __init__(self, image_path: str):
    self._manager = ImageManager(image_path)

  def color_tranformation(self):
    image = self._manager.get_image()
    black_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    self._manager.save_image("color_tranform", black_image)
  
  def border_detection(self):
    image = self._manager.get_image()
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image_border = cv.Laplacian(gray_image, cv.CV_64F)
    image_border[image_border == 0] = 255
    self._manager.save_image('border', image_border)
  
  def properties(self):
    image = self._manager.get_image()
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret,  thresh = cv.threshold(gray_image, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, 1, 2)
    print(len(contours))