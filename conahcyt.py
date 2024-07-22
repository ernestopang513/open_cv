from selenium import webdriver
import cv2
import numpy as np
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


#Este programa ya resalta el elemento web definido y ubicado por selenium mediante el xpath para despues hacer el procesamiento
# digital de la imagen optener la mascara de mediante la ubicacion de contornos y despues aplicar un filtro con el tamaño objetivo 
# para finalmente recortar la imagen. 

driver = webdriver.Edge()

driver.get('https://energia.conacyt.mx/planeas/hidrocarburos/flujo-gas')

driver.maximize_window()

try:
    
    # Cambiar al iframe adecuado
    # driver.switch_to.frame("iframeResult")
    # driver.switch_to.new_window('window')
    # Ubicacion del elemento web a resaltar
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[2]/div[2]/div[2]/div')))
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    # # Obtencion del elemento web mediante el driver
    # select_element = driver.find_element(By.XPATH, '//select[contains(@name, "cars")]')
    
    # select = Select(select_element)
    # select.select_by_visible_text('Opel')

    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//body/form/input[@value="Submit"]'))).click()
    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//body/h2[text()="Your input was received as:"]/following-sibling::*[1]')))
    # element = driver.find_element(By.XPATH, '//body/h2[text()="Your input was received as:"]/following-sibling::*[1]')
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});", element)
    driver.execute_script("arguments[0].style.setProperty('border', 'thick solid black', 'important');", element)
    time.sleep(10)
    
    # Impresion de pantalla del ordenador resaltando la imagen objetivo 
    screenshot_path = 'conahcyt.png'
    driver.save_screenshot(screenshot_path)
    time.sleep(5)
    

    # time.sleep(5)


    
finally:
    # Cerrar el navegador
    driver.quit()

imagen = cv2.imread('conahcyt.png')
if imagen is None:
    print("Error: No se puede abrir o leer el archivo de imagen. Verifica la ruta y el nombre del archivo.")
else:
    # Crear una copia de la imagen original para no modificar la original
    imagen_original = imagen.copy()
        
    # Convierte la imagen a escala de grises
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Aplica un umbral para convertir la imagen a binaria
    _, th = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY_INV)
    
    # Encuentra contornos en la imagen binaria
    contornos, hierarchy = cv2.findContours(th, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    
    # print('hierarchy=', hierarchy)
    
    # print(len(contornos))
    # Crear una máscara en blanco para rellenar los contornos hijos
    mascara_hijos = np.zeros_like(gray)

    # cv2.imshow('gray',gray)
    # cv2.imshow('mascara hijos', mascara_hijos)
    
    # Dibuja todos los contornos en la imagen original
    for i in range(len(contornos)):
        area = cv2.contourArea(contornos[i])
        if area > 3000:
            cv2.drawContours(imagen, contornos, i, (0, 255, 0), 1)
           
            # Rellena los contornos hijos de blanco
            if hierarchy[0][i][3] != -1:  # Verifica si el contorno tiene un padre
                cv2.drawContours(mascara_hijos, contornos, i, 255, -1)  # Rellena el contorno hijo de blanco
    
    # cv2.imshow('mascara hijos', mascara_hijos)
    # Usar la máscara para extraer la parte del contorno hijo de la imagen original
    resultado = cv2.bitwise_and(imagen_original, imagen_original, mask = mascara_hijos)
    
    # Convertir a escala de grises y encontrar todos los píxeles no negros
    gray_resultado = cv2.cvtColor(resultado, cv2.COLOR_BGR2GRAY)
    non_zero_pixels = cv2.findNonZero(gray_resultado)
    
    # Calcular el rectángulo delimitador de la región no negra
    x, y, w, h = cv2.boundingRect(non_zero_pixels)
    
    # Recortar la imagen utilizando el rectángulo delimitador
    resultado_recortado = resultado[y:y+h, x:x+w]
    
    # Guarda el resultado recortado en un archivo .png
    cv2.imwrite('resultado_recortado.png', resultado_recortado)
    
    # # Muestra la imagen con el blanco transformado a azul
    # cv2.imshow('Imagen con blanco transformado a azul', imagen)
    
    # Muestra la imagen en escala de grises
    cv2.imshow('Imagen en escala de grises', gray)
    
    # Muestra la imagen binaria
    cv2.imshow('Imagen binaria', th)
    
    # Muestra la imagen con contornos
    cv2.imshow('Imagen con contornos', imagen)
    
    # Muestra la máscara de contornos hijos
    cv2.imshow('Máscara de contornos hijos', mascara_hijos)
    
    # Muestra el resultado final con los colores originales del contorno hijo
    cv2.imshow('Resultado', resultado)
    
    # Muestra el resultado recortado
    cv2.imshow('Resultado recortado', resultado_recortado)
    
    # Espera hasta que se presione una tecla
    cv2.waitKey(0)
    cv2.destroyAllWindows()
