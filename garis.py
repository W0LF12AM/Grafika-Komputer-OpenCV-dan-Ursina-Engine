import numpy as np
import cv2

jendela = np.zeros((500,500, 3), dtype='uint8')
jendela [:] = (255, 0, 0) 

cv2.line(jendela, (250, 0), (250, 250), (255,255,255), 5)

cv2.imshow("Garis", jendela)
cv2.waitKey(0)


