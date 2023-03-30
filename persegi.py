import numpy as np
import cv2

biru = 255, 0, 0
jendela = np.zeros((500, 500, 3), dtype='uint8')

persegi = cv2.rectangle(jendela, (125, 125), (375, 375), (255,255,255), 5)

cv2.imshow("Persegi", jendela)
cv2.waitKey(0)