import threading
import math


def thread_login(input_list, amount, func):

    threads = []

    b = 0

    for acc in range(math.ceil((len(input_list)) / amount)):
        if ((len(input_list)) - amount) - b > 0:
            amount = amount
        else:
            amount = len(input_list) - b
        for i in range(amount):
            try:

                data_acc = input_list[b].split(':')
                print(data_acc)
                t = threading.Thread(target=func, args=(data_acc[0], data_acc[1], f'bob{i}', str(i),))
                b += 1
                t.start()
                threads.append(t)
            except:
                pass

        for thread in threads:
            thread.join()


def thread_location(input_list, amount, func, user, sub):

    threads = []

    b = 0

    for acc in range(math.ceil((len(input_list)) / amount)):
        if ((len(input_list)) - amount) - b > 0:
            amount = amount
        else:
            amount = len(input_list) - b
        for i in range(amount):
            try:
                t = threading.Thread(target=func, args=(f'NameGroup{input_list[b]}', input_list[b], user, sub,))
                b += 1
                t.start()
                threads.append(t)
            except:
                pass

        for thread in threads:
            thread.join()

