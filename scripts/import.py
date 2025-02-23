from selenium import webdriver
from selenium.webdriver.common.by import By
import time



# WebDriver'ı başlat
driver = webdriver.Chrome()

# Sayfayı aç
driver.get("https://tr.abrams.wiki")
time.sleep(5)
importbtn = driver.find_element(By.XPATH,"/html/body/app-root/app-root/div[1]/div[1]/wtw-page-type-next-homepage/div/section[5]/wtw-globe/div/div/div[1]/div/div[1]/form/label[2]")
importbtn.click()
time.sleep(1)

# Veriyi çek
for i in range(253):
    time.sleep(2)
    box = driver.find_element(By.TAG_NAME, "tbody")
    countries = box.find_elements(By.TAG_NAME, "tr")
    infos = countries[i].find_elements(By.TAG_NAME, "td")
    name = infos[1].text

    countries[i].click()
    time.sleep(1)
    
    box2 = driver.find_element(By.TAG_NAME, "tbody")
    countries2 = box2.find_elements(By.TAG_NAME, "tr")
    for j, country2 in enumerate(countries2):
        infos2 = country2.find_elements(By.TAG_NAME, "td")
        with open("import", "a", encoding="utf-8") as dosya:
            dosya.write(infos2[1].text)
            dosya.write(", ")
            dosya.write(name)
            dosya.write(", ")
            dosya.write(infos2[3].text)
            dosya.write("\n")

    buton = driver.find_element(By.XPATH,"/html/body/app-root/app-root/div[1]/div[1]/wtw-page-type-next-homepage/div/section[5]/wtw-globe/div/div/div[1]/div/div[2]/table/thead/tr/th[1]/span")

    buton.click()


input("enter for exit")

