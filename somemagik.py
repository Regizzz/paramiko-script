#!/usr/bin/env python3

import paramiko
from getpass import getpass
import time

host = "192.168.25.25"
username = (input("Enter username: ") or "miguel")
password = getpass("Enter password: ")

session = paramiko.SSHClient()

# session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.load_system_host_keys()

session.connect(hostname=host,
                username=username,
                password=password)

# vpnclient = input("Enter vpn client name: ")
# './easyrsa gen-req {vpnclient} nopass'.format(vpnclient)
commands = ['cd easy-rsa', 'ls -l']

for command in commands:
    stdin, stdout, stderr = session.exec_command(command)
    time.sleep(.5)
    print(stdout.read().decode())

session.close()