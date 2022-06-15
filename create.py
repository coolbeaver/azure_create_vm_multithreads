import subprocess
from config import login, password


def create_group(name, location, user, sub):
    subprocess.run(['sudo', '-u', user, 'az', 'group', 'create', '--name', name, '-l', location, '--subscription', sub])
    create = subprocess.run(['sudo', '-u', user, 'az', 'vm', 'create', '--resource-group', name, '--subscription', sub, '--name', 'myVM',
                             '--image', 'UbuntuLTS', '--public-ip-sku', 'Standard', '--size', 'Standard_D8as_v4',
                             '--admin-username', login, '--admin-password', password], stdout=subprocess.PIPE)
    print(len(create.stdout))



# Standard_D8s_v4
# Standard_D8s_v3