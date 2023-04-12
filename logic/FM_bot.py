import configparser
import csv
import os
import sys
import traceback
from io import BytesIO
from typing import Tuple

import chromedriver_binary
import requests
from HistoryCheck import check_uid, save_uid
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from db.SearchQueriesRepo import SearchQueryRepo

import model.constants.Constants as Constants
from db.FBMarketplaceRepo import FBMarketplaceRepo
from model.CarAD import CarAD
from model.FMQuery import FMQuery
from notifier.Telegram_notifier import (send_telegram_image,
                                        send_telegram_message)

global driver
global telegram_notification
global max_queries
queryRepo = SearchQueryRepo()
queriesFromCsv = True

# TODO: get search queries from DB


def get_queries() -> list[FMQuery]:
    result = []
    with open('logic/searchQueries.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            result.append(FMQuery(row[0], row[1], row[2]))

        return result


def get_page():
    global driver

    with open('out.txt', 'w') as f:
        f.write(driver.page_source)


def get_properties():
    global telegram_notification
    global max_queries
    config = configparser.RawConfigParser()

    config.read('logic/fm.properties')

    max_queries = config.get('BotProperties', 'bot.maxResults')
    telegram_notification = config.get('BotProperties', 'bot.notification')


# TODO: extract to a singleton class Webdriver
def set_up():
    global driver
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(10)
    get_properties()


def set_up_local(query: FMQuery):
    global driver

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-notifications")
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    get_properties()
    driver.get(query.get_url())
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 900)
    driver.implicitly_wait(10)


def log_in(query: FMQuery):
    global driver
    driver.get(Constants.urls.log_in)
    WebDriverWait(driver, 5)

    username_input = driver.find_element(
        By.XPATH, Constants.xpath.username_input)
    passwd_input = driver.find_element(
        By.XPATH, Constants.xpath.password_input)

    username = sys.argv[1]
    passwd = sys.argv[2]

    username_input.send_keys(username)
    passwd_input.send_keys(passwd)
    passwd_input.submit()

    driver.get(query.get_url())


def accept_cookies():
    global driver
    driver.implicitly_wait(5)
    get_page()
    accept_cookie__button = driver.find_element(
        By.XPATH, Constants.xpath.accept_cookie_path)
    accept_cookie__button.click()
    driver.implicitly_wait(5)


# TODO: keep this as main method but refactor the logic
def process_ads(query: FMQuery):
    driver.implicitly_wait(10)
    driver.get(query.get_url())
    driver.implicitly_wait(10)
    mongo_repo = FBMarketplaceRepo()
    ads_containers = driver.find_elements(
        By.XPATH, Constants.xpath.ad_container_path)
    results = 0
    for ads in ads_containers:
        cards = ads.find_elements(
            By.XPATH, Constants.xpath.cards_xpath)
        for card in cards:
            try:
                if card.text == '':
                    continue
                if any(banned in card.text for banned in Constants.banned.words):
                    continue
                link = card.find_element(By.XPATH, Constants.xpath.card_link)
                url = link.get_attribute("href")

                split_desc = card.text.splitlines()

                card_ad = CarAD(split_desc, url)

                if not mongo_repo.exists_car_ad(card_ad):

                    screenshot_file, img_url = take_screenshot(
                        query.query, card_ad.uid, card)
                    card_ad.set_images(screenshot_file, img_url)
                    mongo_repo.insert_car_ad(card_ad.to_dict())

                    # save_uid(card_ad.uid)
                    send_telegram_image(card_ad.to_string(), img_url)
                    os.remove(img_url)
                    results += 1
                    if (results >= int(max_queries)):
                        break

            except:
                traceback.print_exc()

    print('Saved {} new ads'.format(results))


def take_screenshot(query, uid, card) -> Tuple[bytes, str]:
    directory = f'img/{query}/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    screenshot_file = f"{directory}{uid}.png"

    img_src = card.find_elements(By.XPATH, ".//img")[0].get_attribute("src")
    response = requests.get(img_src)

    with open(screenshot_file, 'wb') as f:
        f.write(response.content)

    return response.content, screenshot_file


if queriesFromCsv:

    queries = get_queries()
    queryRepo.insert_multiple(queries)

else:
    queries = queryRepo.get_all_queries()

set_up()
for query in queries:
    print(
        f'\tSearch car model : {query.query} at maximum price of {query.max_price}.')
    try:
        log_in(query)
    except:
        print('Could not log in')
    WebDriverWait(driver, 5)
    try:
        accept_cookies()
    except:
        print('Could not accept cookies')
    WebDriverWait(driver, 3)
    process_ads(query)
