import math, cv2, time
import numpy as np

GREEN = (0,255,0)
RED = (0,0,255)
BLUE = (255,0,0)
WHITE = (255,255,255)
TEAL = (255,255,0)

koordinat = list(range(8))

koordinat[0] = [[-1], [-1], [1]]
koordinat[1] = [[1], [-1], [1]]
koordinat[2] = [[1], [1], [1]]
koordinat[3] = [[-1], [1], [1]]
koordinat[4] = [[-1], [-1], [-1]]
koordinat[5] = [[1], [-1], [-1]]
koordinat[6] = [[1], [1], [-1]]

koordinat[7] = [[-1], [1], [-1]]

def garis (jendela, i, j, k, warna) :
    a, b = k[i], k[j]
    cv2.line(jendela, (a[0], a[1]), (b[0], b[1]), warna, 5)
    
jendela = np.zeros((500, 500, 3), dtype='uint8')
sdt_x, sdt_y, sdt_z = 0, 0, 0
kecepatan_rotasi = 120
skala = 600

perubahan_sudut = 0.01

while True :
    canvas = np.copy(jendela)
    
    proyeksi_koordinat = [j for j in range(len(koordinat))]
    sdt_x += perubahan_sudut
    sdt_y += perubahan_sudut
    sdt_z += perubahan_sudut
    
    
    rotasi_x = [
        [1, 0,  0],
        [0, math.cos(sdt_x), -math.sin(sdt_x)],
        [0, math.sin(sdt_x), math.cos(sdt_x)]
        ]
    rotasi_y = [
        [math.cos(sdt_y), 0, -math.sin(sdt_y)],
        [0, 1,  0],
        [math.sin(sdt_y), 0,  math.cos(sdt_y)]
        ]
    rotasi_z = [
        [math.cos(sdt_z), -math.sin(sdt_z), 0],
        [math.sin(sdt_z), math.cos(sdt_z), 0],
        [0, 0,  1],
        ]
    
    index = 0
    for krdnt in koordinat :
        rotasi2d = np.matmul(rotasi_y, krdnt)
        rotasi2d = np.matmul(rotasi_x, rotasi2d)
        rotasi2d = np.matmul(rotasi_z, rotasi2d)
        
        jarak = 5
        
        z = 1 / (jarak - rotasi2d[2][0])
        
        matriks_proyeksi = [[z, 0, 0], [0, z, 0]]
        proyeksi2d = np.matmul(matriks_proyeksi, rotasi2d)
        
        x = int(proyeksi2d[0][0] * skala) + 500//2
        y = int(proyeksi2d[1][0] * skala) + 500//2
        
        proyeksi_koordinat[index] = [x, y]
        
        cv2.circle(canvas, (x, y), 5, WHITE, 10)
        cv2.circle(canvas, (500//2, 500//2), 5, TEAL, -1)
        
        index += 1
        
    for koordinat_titik in range(4) : 
        garis(canvas, koordinat_titik, (koordinat_titik + 1)%4, proyeksi_koordinat, RED )
        garis(canvas, koordinat_titik + 4, (koordinat_titik + 1)%4 + 4, proyeksi_koordinat, BLUE )
        garis(canvas, koordinat_titik, (koordinat_titik + 4) , proyeksi_koordinat, GREEN )
        
    cv2.imshow("Kubus", canvas)
    time.sleep(1/kecepatan_rotasi)
    if cv2.waitKey(1) == ord('q') :
        break