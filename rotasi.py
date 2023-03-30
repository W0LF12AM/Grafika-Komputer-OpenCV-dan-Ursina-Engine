import numpy as np
import cv2

jendela = np.zeros((500, 500, 3), dtype='uint8')

persegi = cv2.rectangle(jendela, (125, 125), (375, 375), (255,255,255), 5)

M = cv2.getRotationMatrix2D((250, 250), 30, 1.0)
rotasi = cv2.warpAffine(persegi, M, (persegi.shape[1], persegi.shape[0]))

cv2.imshow("Rotasi", rotasi)
cv2.imshow("Persegi", jendela)
cv2.waitKey(0)