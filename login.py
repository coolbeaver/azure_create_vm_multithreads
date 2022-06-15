from subprocess import PIPE, Popen
import subprocess
from threading import Thread
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from driver import browser
from config import driver_path, path
from find import find
import os

status = []


def login_cli(email, passwd, user, num_br):
    num = random.randint(0, 123123123122)

    def cmdline(command):
        process = Popen(
            args=command,
            stdout=PIPE,
            stderr=PIPE,
            shell=True
        )
        try:
            process.wait(timeout=35)
            return process.communicate()
        except subprocess.TimeoutExpired:
            status.append('cmdline error')
            return 'Ошибка авторизации'

    def check(num, email, passwd):
        for i in range(0, 10):
            time.sleep(1)
            try:
                f = open(f'{path}{num}')
                s = f.read()
                s1 = s.replace(
                    "WARNING: To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code ",
                    "")
                s1 = s1.replace(" to authenticate.", "")
                print(s1)
                os.remove(f'{path}{num}')
                driver_login(s1, email, passwd)
                return s1
            except FileNotFoundError:
                continue

    def driver_login(data, email, passwd):
        print(data, email, passwd)
        driver = browser(driver_path, num_br)
        driver.get('https://microsoft.com/devicelogin')
        find(driver, 3, By.NAME, 'otc', Keys.RETURN, data, 'Send', 'Code', 1)
        find(driver, 3, By.NAME, 'loginfmt', Keys.RETURN, email, 'Send', 'Code', 1)
        find(driver, 3, By.NAME, 'passwd', Keys.RETURN, passwd, 'Send', 'Code', 2)
        find(driver, 3, By.ID, 'idSIButton9', action='Click')
        driver.save_screenshot('test.png')
        
    thread1 = Thread(target=cmdline, args=(f'sudo -u {user} az login --use-device-code 2>{num}',))
    thread2 = Thread(target=check, args=(num, email, passwd,))

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    for i in status:
        return i
