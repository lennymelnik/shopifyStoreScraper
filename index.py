from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import numpy as np

descXpath = "/html/body/main/div[1]/section/div[1]/div[2]/div/div[3]/div/div[2]/div/p[1]"
titleXpath = "/html/body/main/div[1]/section/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/h1"
priceXpath = "/html/body/main/div[1]/section/div[1]/div[2]/div/div[2]/div/div[2]/form/div[1]/div[1]/div/div[1]/span[1]"
imageXpath = "/html/body/main/div[1]/section/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/div/img"

allproductsUrl = "https://medixsource.com/collections/all"
allproductsXpath = "/html/body/main/div[1]/section/div[1]/div[2]/div[2]/div/div/div/div[2]"



driver = webdriver.Chrome("/home/leonard/Ivanka/codingChallenges/chromedriver")


listHi = []
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


driver.maximize_window()


driver.get(allproductsUrl)

allProductsList = driver.find_element_by_xpath(allproductsXpath).find_elements_by_xpath(".//*")
full = []

page = 1 
for d in range(17):
    newpage = "https://medixsource.com/collections/all?page=" + str(page)
    driver.get(newpage)
    for i in range(24):
        
        product = i +1
        driver.find_element_by_xpath("/html/body/main/div[1]/section/div[1]/div[2]/div[2]/div/div/div/div[2]/div[" + str(product) +"]/div/div/a[2]").click()
        driver.implicitly_wait(2)

        title = driver.find_element_by_class_name("product-meta__title").text
        tag = driver.find_element_by_xpath("/html/body/main/div[1]/section/div[1]/div[1]/nav/ol/li[2]/a").text
        description = driver.find_element_by_class_name("expandable-content").get_property('innerText')
        price = driver.find_element_by_class_name("price").text
        
        image = driver.find_element_by_class_name("lazyautosizes").get_property('srcset')

        
        print(i)
        print(tag)
        full.append([title, description,price,image])
        driver.get(newpage)
        if (d == 16) and (i == 5):
            break



        
    page = page + 1


np.savetxt('out.csv', (np.array(full)), delimiter=",", fmt = '%s',header='Title,Body (HTML),Variant Price, Image Src')