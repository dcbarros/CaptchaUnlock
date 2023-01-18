from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
import os


driver = webdriver.Firefox()
driver.get('https://www.fundamentus.com.br/visual.php')

for i in range(2000):

    diretorio = os.path.join(Path(__file__).parent,"data","captchaDataSet")
    with open(os.path.join(diretorio,f"img{i+1}.png"),'wb') as file:
        element = driver.find_element(By.XPATH,"/html/body/img")
        file.write(element.screenshot_as_png)
        driver.refresh()

driver.close()