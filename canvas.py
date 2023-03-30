import numpy as np
import cv2

jendela = np.zeros((500,500, 3), dtype='uint8')
jendela [:] = (255, 0, 0) 

cv2.imshow("Jendela", jendela)
cv2.waitKey(0)


