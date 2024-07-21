from selenium import webdriver
import cv2
import numpy as np
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()

driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select')

try:

    # Ubicacion del elemento web a resaltar
    volvo = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//body/form/select[contains(@name, "cars")]/option[contains(@value, "opel")]')))
    print(volvo.text)

    # Obtencion del elemento web mediante el driver
    select_element = driver.find_element(By.XPATH, '//body/form/select[contains(@name, "cars")]')
    
    select = Select(select_element)
    select.select_by_visible_text('Opel')

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//body/'))).click()

    element = driver.find_elements(By.XPATH, '//body/h2[text()="Your input was received as:"]/following-sibling::*[1]')
    driver.execute_script("arguments[0].style.border = 'thick solid blue'", element)
    # Impresion de pantalla del ordenador resaltando la imagen objetivo 

    # screenshot_path = 'captura_de_pantalla.png'
    # driver.save_screenshot(screenshot_path)

    # time.sleep(5)


    
finally:
    # Cerrar el navegador
    driver.quit()

# imagen = cv2.imread('captura_de_pantalla.png')
# if imagen is None:
#     print("Error: No se puede abrir o leer el archivo de imagen. Verifica la ruta y el nombre del archivo.")
# else:
    # Crear una copia de la imagen original para no modificar la original
    # imagen_original = imagen.copy()
        
    # # Convierte la imagen a escala de grises
    # gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # # Aplica un umbral para convertir la imagen a binaria
    # _, th = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY_INV)
    
    # # Encuentra contornos en la imagen binaria
    # contornos, hierarchy = cv2.findContours(th, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    
    # # print('hierarchy=', hierarchy)
    
    # # print(len(contornos))
    # # Crear una máscara en blanco para rellenar los contornos hijos
    # mascara_hijos = np.zeros_like(gray)

    # # cv2.imshow('gray',gray)
    # # cv2.imshow('mascara hijos', mascara_hijos)
    
    # # Dibuja todos los contornos en la imagen original
    # for i in range(len(contornos)):
    #     area = cv2.contourArea(contornos[i])
    #     if area > 3000:
    #         cv2.drawContours(imagen, contornos, i, (0, 255, 0), 1)
           
    #         # Rellena los contornos hijos de blanco
    #         if hierarchy[0][i][3] != -1:  # Verifica si el contorno tiene un padre
    #             cv2.drawContours(mascara_hijos, contornos, i, 255, -1)  # Rellena el contorno hijo de blanco
    
    # # cv2.imshow('mascara hijos', mascara_hijos)
    # # Usar la máscara para extraer la parte del contorno hijo de la imagen original
    # resultado = cv2.bitwise_and(imagen_original, imagen_original, mask = mascara_hijos)
    
    # # Convertir a escala de grises y encontrar todos los píxeles no negros
    # gray_resultado = cv2.cvtColor(resultado, cv2.COLOR_BGR2GRAY)
    # non_zero_pixels = cv2.findNonZero(gray_resultado)
    
    # # Calcular el rectángulo delimitador de la región no negra
    # x, y, w, h = cv2.boundingRect(non_zero_pixels)
    
    # # Recortar la imagen utilizando el rectángulo delimitador
    # resultado_recortado = resultado[y:y+h, x:x+w]
    
    # # Guarda el resultado recortado en un archivo .png
    # cv2.imwrite('resultado_recortado.png', resultado_recortado)
    
    # # # Muestra la imagen con el blanco transformado a azul
    # # cv2.imshow('Imagen con blanco transformado a azul', imagen)
    
    # # Muestra la imagen en escala de grises
    # cv2.imshow('Imagen en escala de grises', gray)
    
    # # Muestra la imagen binaria
    # cv2.imshow('Imagen binaria', th)
    
    # # Muestra la imagen con contornos
    # cv2.imshow('Imagen con contornos', imagen)
    
    # # Muestra la máscara de contornos hijos
    # cv2.imshow('Máscara de contornos hijos', mascara_hijos)
    
    # # Muestra el resultado final con los colores originales del contorno hijo
    # cv2.imshow('Resultado', resultado)
    
    # # Muestra el resultado recortado
    # cv2.imshow('Resultado recortado', resultado_recortado)
    
    # # Espera hasta que se presione una tecla
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
