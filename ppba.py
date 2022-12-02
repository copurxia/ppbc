from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

options = Options()
options.add_experimental_option(
    "excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://ppbc.iplant.cn/sp/10525")
driver.implicitly_wait(0.5)
plants = driver.find_elements(By.CSS_SELECTOR, ".namew.fl> a:nth-child(1)")
plantar = []
for plant in plants:
    plantar.append(plant.get_attribute("href"))

for plant_detail in plantar:
    driver.get(plant_detail)

    print(plant_detail)

    driver.implicitly_wait(0.5)
    plant_time = driver.find_element(
        By.CSS_SELECTOR, ".divback21> div:nth-child(3)").text[5:]
    plant_img = driver.find_element(
        By.CSS_SELECTOR, "#viewer2> img").get_attribute("src")
    plant_name = driver.find_element(
        By.CSS_SELECTOR, "#txt_classsys> a:nth-child(3)> b").text
    print(plant_name, "\n", plant_time, plant_img)
    if not os.path.exists("img/"+plant_name):
        os.mkdir("img/"+plant_name)
    with open("./img/"+plant_name+"/"+plant_detail.split("/")[-1]+" "+plant_time.replace("/", "-").replace(":", ";") + ".png", "wb") as f:
        f.write(driver.find_element(
            By.CSS_SELECTOR, "#viewer2> img").screenshot_as_png)


driver.quit()
