import subprocess
import paramiko
import time


vboxmanage_path = 'E:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe'

vm_name = "CentOS_ODS"

start_command = f'"{vboxmanage_path}" startvm {vm_name} --type headless'

vm_ip = "192.168.56.103" 
ssh_username = "root"
ssh_password = "root"

try:
    subprocess.run(start_command, shell=True, check=True)
    print(f"Starting virtual machine '{vm_name}'...")
    time.sleep(120)

except subprocess.CalledProcessError:
    print(f"Failed to start virtual machine '{vm_name}'.")
    
except Exception as e:
    print(f"An error occurred: {str(e)}")