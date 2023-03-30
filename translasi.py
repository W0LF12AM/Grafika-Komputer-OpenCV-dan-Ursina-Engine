import numpy as np
import cv2

biru = 255, 0, 0
jendela = np.zeros((500, 500, 3), dtype='uint8')

persegi = cv2.rectangle(jendela, (125, 125), (375, 375), (255,255,255), 5)
M = np.float32([[1, 0, 100], [0, 1, 50]])
translasi = cv2.warpAffine(persegi, M, (persegi.shape[1], persegi.shape[0]))

cv2.imshow("Persegi", jendela)
cv2.imshow("translasi", translasi)
cv2.waitKey(0)