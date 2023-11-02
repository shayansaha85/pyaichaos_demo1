import paramiko
from jproperties import Properties


def connector():
    properties = Properties()

    with open("config.properties", 'rb') as f:
        properties.load(f, "utf-8")


    vm_ip = str(properties.get('ip').data)
    ssh_username = str(properties.get('username').data)
    ssh_password = str(properties.get('password').data)

    print(vm_ip)


    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(vm_ip, username=ssh_username, password=ssh_password)
        print("Connected to the host")
        return ssh_client

    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials")
    except paramiko.SSHException as sshException:
        print(f"Unable to establish SSH connection: {sshException}")
