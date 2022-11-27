from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By


mp_base = 'https://www.facebook.com/marketplace/london/search/?query=mx5'


driver = webdriver.Chrome()
driver.get(mp_base)
driver.set_window_position(0, 0)
driver.set_window_size(1920, 900)

accept_cookie_path = '/html/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]'


accept_cookie__button = driver.find_element(By.XPATH, accept_cookie_path)

accept_cookie__button.click()

ad_container_path = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[3]/*'


driver.implicitly_wait(5)
ads_containers = driver.find_elements(By.XPATH, ad_container_path)
# parent_element = element.find_element(By.XPATH, "..")
i =0
for ads in ads_containers:
    ads_infos = ads.text.split('£')
    for ad in ads_infos:
        # print(ad)
        print("=======================================================================")
        ad_info = ad.splitlines()
        if len(ad_info) > 0:
            i+=1
            print(i)
            print(ad_info)
        
a =0
