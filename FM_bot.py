import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import Constants
from CarAD import CarAD
from HistoryCheck import check_uid, save_uid

global driver


def set_up():
    global driver
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(Constants.urls.mp_base.format(
        Constants.Cities.london, Constants.Cars.mr2))
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 900)


def accept_cookies():
    global driver
    accept_cookie__button = driver.find_element(
        By.XPATH, Constants.xpath.accept_cookie_path)
    accept_cookie__button.click()
    driver.implicitly_wait(5)


def process_ads():

    ads_containers = driver.find_elements(
        By.XPATH, Constants.xpath.ad_container_path)
    new_saved = 0
    for ads in ads_containers:
        cards = ads.find_elements(
            By.XPATH, Constants.xpath.cards_xpath)
        for card in cards:
            try:
                if card.text == '':
                    continue
                link = card.find_element(By.XPATH, Constants.xpath.card_link)
                url = link.get_attribute("href")
                split_desc = card.text.splitlines()
                card_ad = CarAD(split_desc, url)

                if not check_uid(card_ad.uid):
                    save_uid(card_ad.uid)
                    new_saved += 1

            except:
                print('Could not get card : \n' + str(card))
    print('Saved {} new ads'.format(new_saved))


set_up()
accept_cookies()
process_ads()
