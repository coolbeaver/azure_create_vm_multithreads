import time
from selenium.common.exceptions import NoSuchElementException


def find(driver, attempt, method, selector, key='None', data='None', action='None', error='None', timeout=1):
    attempt_current = 0
    while True:
        if attempt_current >= attempt:
            return error
        else:
            try:
                attempt_current += 1
                time.sleep(1)
                elem = driver.find_element(method, selector)
                if action == 'None':
                    pass
                elif action == 'Send':
                    elem.send_keys(data + key)
                elif action == 'Click':
                    elem.click()
                elif action == 'Check':
                    return True
                elif action == 'Check_r':
                    return elem.text
                attempt_current += attempt
                break
            except NoSuchElementException:
                print(selector + str(attempt_current))

    time.sleep(timeout)

def finds(driver, attempt, method, selector, key='None', data='None', action='None', error='None', timeout=1, object='None', index='None'):
    attempt_current = 0
    while True:
        if attempt_current >= attempt:
            print('Error: ' + error)
            break
        else:
            try:
                elem_list = []
                elem = driver.find_elements(method, selector)
                for i in elem:
                    list_partition = i.text.partition(' - ')[0]
                    print(list_partition)
                    elem_list.append(list_partition)
                if index == 'None':
                    index = elem_list.index(object)
                elif index != 'None':
                    index = index
                if action == 'None':
                    pass
                elif action == 'Send':
                    elem[index].send_keys(data + key)
                elif action == 'Click':
                    try:
                        elem[index].click()
                    except:
                        driver.execute_script("arguments[0].click();", elem[index])
                attempt_current += attempt
                break
            except:
                pass

    time.sleep(timeout)