from image_manager import ImageManager
import cv2 as cv
import numpy as np

class ImageMeasurements():
  def __init__(self, image_path: str):
    self._manager = ImageManager(image_path)

  def color_tranformation(self):
    image = self._manager.get_image()
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray_image, 200, 255, 0)
    self._manager.save_image("color_tranform", thresh)
  
  def border_detection(self):
    image = self._manager.get_image()
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray_image, 200, 255, 0)
    image_border = cv.Laplacian(thresh, cv.CV_64F)
    image_border[image_border == 0] = 255
    self._manager.save_image('border', image_border)
  
  def properties(self):
    image = self._manager.get_image()
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret,  thresh = cv.threshold(gray_image, 200, 255, 0)
    contours, hierarchy = cv.findContours(thresh, 1, 2)

    print(f"número de regiões: {str(len(contours) - 1)}")
    for i, c in enumerate(contours):
      if (i < len(contours) - 1):
        M = cv.moments(c)
        
        area = cv.contourArea(c)
        perimeter = cv.arcLength(c, True)

        print(f"região {str(i)}: área: {int(area)} perímetro: {round(perimeter, 6)}")
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])  
        cv.putText(thresh, str(i), (cX, cY), cv.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)
    
    self._manager.save_image('properties', thresh)
