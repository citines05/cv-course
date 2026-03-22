import numpy as np
import matplotlib.pyplot as plt

image = plt.imread('image.png')
print(type(image))
print(image.dtype)
print(image[0,0])

# mostra a imagem
plt.imshow(image)