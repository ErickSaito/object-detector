import cv2 as cv

class ImageManager():
  def __init__(self, image_path: str):
    self._image_path = image_path
    self._image = cv.imread(self._image_path)

  def get_image(self):
    return self._image.copy()

  def save_image(self, process_name: str, img):
    image_name = self._image_path.split('/')[-1].split('.')[0]
    cv.imwrite(f'results/{image_name}-{process_name}.png', img)