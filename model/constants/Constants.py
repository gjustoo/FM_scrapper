class Cities:
    london = 'london'


class Cars:
    mr2 = 'mr2'
    miata = 'mx5'


class urls:

    mp_base = 'https://www.facebook.com/marketplace/london/search/?{}'
    log_in = 'https://www.facebook.com/login'


class banned:
    words = ['mercedes', 'bmw', '350z', 'Smart', 'Smart', 'Benz', 'Mercedes']


class xpath:

    accept_cookie_path = '/html/body/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]'

    ad_container_path = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[3]/*'

    cards_xpath = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[3]/div[1]/div[2]/*'

    card_link = './/div/div/span/div/div/a'

    username_input = '/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[1]/input'

    password_input = '/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[2]/div/div/input'
