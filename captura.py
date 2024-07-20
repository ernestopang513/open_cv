from selenium import webdriver
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Configuración del servicio para Edge


# Crear una instancia del controlador del navegador Edge
driver = webdriver.Edge()

# Navegar a la página deseada
driver.get('')

# Esperar unos segundos para asegurar que la página ha cargado completamente
time.sleep(5)

# Tomar la captura de pantalla y guardarla
screenshot_path = 'captura_de_pantalla.png'
driver.save_screenshot(screenshot_path)

# Cerrar el navegador
driver.quit()

# Mostrar la imagen guardada
img = mpimg.imread(screenshot_path)
imgplot = plt.imshow(img)
plt.axis('off')  # Ocultar los ejes
plt.show()
