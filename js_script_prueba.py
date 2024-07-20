from selenium import webdriver
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


driver = webdriver.Edge()

driver.get('http://demo-store.seleniumacademy.com/')

try:
    women = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//nav/ol/li[contains(@class, "nav-1")]/a')))
    
    elements = driver.find_elements(By.XPATH, '//nav/ol/li[contains(@class, "nav-1")]/a[contains(text(), "Women")]')
    for element in elements:
        if "has-children" in element.get_attribute("class"):
            driver.execute_script("arguments[0].style.border = 'thick solid blue'", element)

    screenshot_path = 'captura_de_pantalla.png'
    driver.save_screenshot(screenshot_path)

    time.sleep(5)
    print(women.text)
finally:
    # Cerrar el navegador
    driver.quit()

img = mpimg.imread(screenshot_path)
imgplot = plt.imshow(img)
plt.axis('off')  # Ocultar los ejes
plt.show()


