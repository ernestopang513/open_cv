import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('mayacan_nitrogeno.png')

print(np.shape(image))
# Obtener las dimensiones de la imagen
height, width, _ = image.shape

# Definir el grosor de la línea
line_thickness = 5

# Dibujar la línea negra en la parte inferior de la imagen
cv2.line(image, (0, height - line_thickness), (width, height - line_thickness), (0, 0, 0), line_thickness)

# Mostrar la imagen con la línea negra


cv2.imshow('Image with Bottom Line', image)
cv2.imwrite('mayacan_tratado.png', image)
cv2.waitKey(0)
cv2.destroyAllWindows()