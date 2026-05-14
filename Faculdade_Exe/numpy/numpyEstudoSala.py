from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread("banner.png")
img = np.array(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

branco = np.full(img.shape, [255,255,255])
m3 = np.hstack((img,branco))
m4 = np.hstack((branco,img))
m5 = np.vstack((m3,m4))

plt.imshow(m5)
plt.show()

lista = ['joao','maria','jose']
dict1 = {
    'ch1' : lista[0],
    'ch2' : lista[1],
    'ch3' : lista[2]
}
