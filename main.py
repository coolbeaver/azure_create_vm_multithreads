import math
import subprocess
import threading

from login import login_cli
from create import create_group
from locations_list import locs
import time
from theards_start import thread_location

unauthorized = []
authorized = []
succeeded = []
sub_list = []
ip_list = []


def start(mail, epass, user, num_br):
    subprocess.run(['sudo', '-u', user, 'az', 'logout'])
    start_time = time.time()
    login_cli(mail, epass, user, num_br)
    auth = subprocess.run(['sudo', '-u', user, 'az', 'account', 'list'], stdout=subprocess.PIPE)
    if len(auth.stdout) < 10:
        unauthorized.append(mail)
    else:
        sub_col_check = subprocess.run([f'sudo -u {user} az account list --query "[].id" -o table'],
                                       stdout=subprocess.PIPE, shell=True)
        lensub = str(sub_col_check).split('\\n')
        for i in range(2, int(len(lensub)) - 1):
            sub_list.append(lensub[i])
            # thread_location(locs, 50, create_group, user, sub)
        threads = []
        amount = 5
        b = 0

        for acc in range(math.ceil((len(sub_list)) / amount)):
            if ((len(sub_list)) - amount) - b > 0:
                amount = amount
            else:
                amount = len(sub_list) - b
            for i in range(amount):
                try:
                    sub_acc = sub_list[b]
                    t = threading.Thread(target=thread_location, args=(locs, 50, create_group, user, sub_acc,))
                    b += 1
                    t.start()
                    threads.append(t)
                except:
                    pass

            for thread in threads:
                thread.join()
        end_time = time.time()
        total = end_time - start_time
        print('Time: ', total)
        for sub in sub_list:
            status_create = subprocess.run(
                [f'sudo -u {user} az vm list-ip-addresses -o table --subscription {sub}'],
                stdout=subprocess.PIPE, shell=True)

            for i in status_create.stdout.decode().split(' '):
                if i.replace('.', '').isdigit() is True and i.isdigit != "10.0.0.4":
                    print(i)
                    ip_list.append(i)
        subprocess.run(['sudo', '-u', user, 'az', 'logout'])
        authorized.append(mail)
