from jproperties import Properties

def read_properties_file(file_path):
    properties = Properties()

    with open(file_path, 'rb') as f:
        properties.load(f, "utf-8")

    value_ip = properties.get('ip')
    value_username = properties.get('username')
    value_password = properties.get('password')

    print(f"IP: {value_ip.data}")
    print(f"Username: {value_username.data}")
    print(f"Password: {value_password.data}")

file_path = 'config.properties'

read_properties_file(file_path)