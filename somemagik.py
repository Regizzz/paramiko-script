#!/usr/bin/env python3

import paramiko
from getpass import getpass
import time

host = "192.168.25.25"
username = (input("Enter username: ") or "miguel")
password = getpass("Enter password: ")

session = paramiko.SSHClient()

session.load_system_host_keys()

session.connect(hostname=host,
                username=username,
                password=password)

vpnclient = input("Enter vpn client name: ")

commands = [f'cd easy-rsa && yes "" | ./easyrsa gen-req {vpnclient} nopass', 
            f'cp /home/miguel/easy-rsa/pki/private/{vpnclient}.key ~/client-configs/keys', 
            'ls ~/client-configs/keys']

for command in commands:
    stdin, stdout, stderr = session.exec_command(command)
    time.sleep(1)
    print(stdout.read().decode())

session.close()