from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

# 配置selenuim
options = Options()
options.add_experimental_option(
    "excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(options=options)
file = open("addr.txt")
while True:
    # 文件读取
    line = file.readline()
    count = 0
    if line:
        print("File Line =", line, end='')
        driver.get(line)
        count += 1
        sleep(5)
        # 滚动到底部
        temp_height = 0
        while True:
            driver.execute_script("window.scrollBy(0,1000)")
            sleep(5)
            check_height = driver.execute_script(
                "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
            if check_height == temp_height:
                break
        temp_height = check_height
        driver.implicitly_wait(0.5)
        plants = driver.find_elements(
            By.CSS_SELECTOR, ".namew.fl> a:nth-child(1)")
        # 进入每个植物页面
        plantar = []
        for plant in plants:
            plantar.append(plant.get_attribute("href"))
        for plant_detail in plantar:
            driver.get(plant_detail)
            sleep(2)
            driver.implicitly_wait(0.5)
            plant_time = driver.find_element(
                By.CSS_SELECTOR, ".divback21> div:nth-child(3)").text[5:]
            plant_img = driver.find_element(
                By.CSS_SELECTOR, "#viewer2> img").get_attribute("src")
            plant_name = driver.find_element(
                By.CSS_SELECTOR, "#txt_classsys> a:nth-child(3)> b").text
            print(plant_name, "\n", plant_time, plant_img)
            # 保存图片
            if not os.path.exists("img/" + str(count) + " " + plant_name):
                os.mkdir("img/" + str(count) + " "+plant_name)
            with open("./img/" + str(count) + " "+plant_name+"/"+plant_detail.split("/")[-1]+" "+plant_time.replace("/", "-").replace(":", ";") + ".png", "wb") as f:
                f.write(driver.find_element(
                        By.CSS_SELECTOR, "#viewer2> img").screenshot_as_png)
                print("./img/"+plant_name+"/"+plant_detail.split("/")
                      [-1]+" "+plant_time.replace("/", "-").replace(": ", "") + ".png")
    else:
        file.close()
        break


driver.quit()
