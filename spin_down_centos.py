import subprocess

subprocess.run(['VBoxManage', 'controlvm', 'CentOS_ODS', 'acpipowerbutton'])