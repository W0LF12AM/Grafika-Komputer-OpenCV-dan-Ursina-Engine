import cv2
import numpy as np

merah = 0, 0, 255
hijau = 0, 255, 0  
biru = 255, 0, 0
putih = 255, 255, 255

jendela = np.zeros((500, 500, 3), dtype="uint8") 

koordinat1 = (250, 125)
koordinat2 = (125, 375) 
koordinat3 = (375, 375)

cv2.circle(jendela, koordinat1, 10, merah, -1)
cv2.circle(jendela, koordinat2, 10, hijau, -1)
cv2.circle(jendela, koordinat3, 10, biru, -1)

titik_segitiga = np.array( [koordinat1, koordinat2, koordinat3] )

cv2.drawContours(jendela, [titik_segitiga], 0, putih, -1)

cv2.imshow("Segitiga", jendela)
cv2.waitKey()