from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()

driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select')

try:
    # Cambiar al iframe adecuado
    driver.switch_to.frame("iframeResult")
    
    # Ubicacion del elemento web a resaltar
    volvo = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//select[@name="cars"]/option[@value="opel"]')))
    print(volvo.text)

    # Obtencion del elemento web mediante el driver
    select_element = driver.find_element(By.XPATH, '//select[@name="cars"]')
    
    select = Select(select_element)
    select.select_by_visible_text('Opel')

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//body/form/input[@value="Submit"]'))).click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//body/h2[text()="Your input was received as:"]/following-sibling::*[1]')))
    element = driver.find_element(By.XPATH, '//body/h2[text()="Your input was received as:"]/following-sibling::*[1]')
    driver.execute_script("arguments[0].style.setProperty('border', 'thick solid black', 'important');", element)
    # Impresion de pantalla del ordenador resaltando la imagen objetivo 
    # screenshot_path = 'captura_de_pantalla.png'
    # driver.save_screenshot(screenshot_path)
    time.sleep(5)

finally:
    # Cerrar el navegador
    driver.quit()
