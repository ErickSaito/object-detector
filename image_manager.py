import cv2 as cv

class ImageManager():
  def __init__(self, image_path: str):
    self._image_path = image_path
    if ("pgm" in image_path):
      self.is_gray = True
      self._image = cv.cvtColor(cv.imread(self._image_path), cv.COLOR_BGR2GRAY)
    else:
      self.is_gray = False
      self._image = cv.imread(self._image_path)

  def get_image(self):
    return self._image.copy()

  def save_image(self, process_name: str, img):
    image_name = self._image_path.split('/')[-1].split('.')[0]
    tone = 'gray' if self.is_gray else 'color'
    cv.imwrite(f'results/{image_name}-{process_name}-{tone}.png', img)