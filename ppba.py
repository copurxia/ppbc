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
count = 0
count_start = 22
pcount_max = 30
while True:
    # 文件读取
    line = file.readline()
    if line:
        print("File Line =", line, end='')
        count = count+1
        print("count = ", count)
        while count < count_start:
            line = file.readline()
            count = count+1
            print("count = ", count)
            print("File Line =", line, end='')
        driver.get(line)
        sleep(5)
        plant_name = driver.find_element(
            By.CSS_SELECTOR, ".divpa2> .fl> div:nth-child(2)").text
        print("Plant Name =", plant_name)
        # 滚动到底部
        temp_height = 0
        while True:
            driver.execute_script("window.scrollBy(0,1000)")
            sleep(1)
            check_height = driver.execute_script(
                "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
            if check_height == temp_height:
                break
            temp_height = check_height
        driver.implicitly_wait(0.5)
        plants = driver.find_elements(
            By.CSS_SELECTOR, ".namew.fl> a:nth-child(1)")
        # 进入每个植物页面
        pcount = 0
        plantar = []
        for plant in plants:
            plantar.append(plant.get_attribute("href"))
        for plant_detail in plantar:
            pcount = pcount + 1
            if pcount > pcount_max:
                break
            driver.get(plant_detail)
            print("Plant Detail =", plant_detail)
            sleep(2)
            driver.implicitly_wait(0.5)
            plant_time = driver.find_element(
                By.CSS_SELECTOR, ".divback21> div:nth-child(3)").text[5:]
            plant_img = driver.find_element(
                By.CSS_SELECTOR, "#viewer2> img").get_attribute("src")
            print(plant_name, "\n", plant_time, plant_img)
            # 保存图片
            if not os.path.exists("img/" + str(count) + " " + plant_name):
                os.mkdir("img/" + str(count) + " "+plant_name)
            with open("./img/" + str(count) + " "+plant_name+"/"+plant_detail.split("/")[-1]+" "+plant_time.replace("/", "-").replace(":", ";") + ".png", "wb") as f:
                f.write(driver.find_element(
                        By.CSS_SELECTOR, "#viewer2> img").screenshot_as_png)
                print("./img/" + str(count) + " "+plant_name+"/"+plant_detail.split("/")
                      [-1]+" "+plant_time.replace("/", "-").replace(": ", "") + ".png")
    else:
        file.close()
        break


driver.quit()
