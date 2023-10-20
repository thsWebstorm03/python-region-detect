import cv2
from pdf2image import convert_from_path
import numpy as np

pdf_path = "path_to_pdf.pdf"
images = convert_from_path(pdf_path)
image = images[0]
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

pattern_template = cv2.imread('path_to_pattern_template.jpg', )
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

seed_x, seed_y = (your_input_x, your_input_y)
expansion_step = 5

top_left_y = seed_y
bottom_right_y = seed_y
top_left_x = seed_x
bottom_right_x = seed_x

while True:
   top_left_y -= expansion_step
   bottom_right_y += expansion_step
   top_left_x -= expansion_step
   bottom_right_x += expansion_step

   cropped_region = image_gray[top_left_y:bottom_right_y, top_left_x:bottom_right_x]

   if cropped_region.shape[0] > pattern_template.shape[0] or 
      break

   result = cv2.matchTemplate(cropped_region, pattern_template, )
   min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

   if max_val < 0.8:
      break

   cv2.rectangle(image, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y))

   cv2.imshow('Dected Pattern Region', image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()