import time
import random
import connector as c
import sys
from jproperties import Properties

properties = Properties()

with open("chaos_config.properties", 'rb') as f:
    properties.load(f, "utf-8")


perc = str(properties.get('percentage').data)
cores = str(properties.get('cores').data)
duration = str(properties.get('duration').data)

def execute_CPUStress(conn, percentage, cores, duration):
    server = "Linux"
    if server == "Linux":
        print("Executing stress")
        stdin, stdout, stderr = conn.exec_command("stress-ng -c {cores} -l {percentage} -t {duration}".format(cores=cores, percentage=percentage, duration=duration))
        print(stdout.read().decode().strip())
        time.sleep(120)

def get_data():
    return [perc, cores, duration]

execute_CPUStress(c.connector(), perc, cores, duration)
