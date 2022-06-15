from selenium import webdriver

from selenium.webdriver.chrome.service import Service

# PROXY = '91.107.119.87:45785'

def browser(driver_path, num_browser='0'):
    service = Service(f"{driver_path}{num_browser}")
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument("enable-automation");
    options.add_argument("--disable-dev-shm-usage");
    options.add_argument("--disable-notifications");
    options.add_argument("--disable-extenstions");
    options.add_argument("--disable-gpu");
    # options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(service=service,
                              options=options)
    return driver