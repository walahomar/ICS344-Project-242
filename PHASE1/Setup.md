
# ICS344 Course Project

## Phase 1: Setup and Compromise the Service

In Phase 1, we set up the attacker and victim machines by following the steps from the official repository for the ICS 344 Course. We compromised the SSH service on the Metasploitable VM, which is already vulnerable, by connecting from the attacker machine to the victim. Then, we created a Python script to brute force SSH authentication on the Metasploitable server.

---

## Victim Environment

After downloading and installing Metasploitable on VirtualBox:
![Metasploitable VM Boot Screen](images/Metasploitable.png)


![Login with vagrant](images/login_with_vagrant.png)

![Check IP address](images/ifconfig_output.png)

![Ping result](images/ping_success.png)

---

## Attacker Environment

After downloading and installing Kali tools and launching Metasploit using:
```
.\msfconsole.bat
```

---

## Task 1.1: Use Kali Linux tool Metasploit to compromise the service

After verifying the connection, we used the `nmap` tool to scan for the SSH port:

![Nmap result](images/nmap_ssh_port.png)

We used the Metasploit module: `auxiliary/scanner/ssh/ssh_login` and set the following options:

```
set rhost 192.168.56.101
set username vagrant
set password vagrant
exploit
```

![SSH session](images/ssh_exploit_result.png)
![SSH session](images/ssh_exploit_result2.png)

After opening the session, we used the `whoami` command:

![Whoami result](images/whoami_output.png)

---

## Task 1.2: Compromise the service using a custom script

We installed the Python library `paramiko` for SSH:

![Install Paramiko](images/install_paramiko.png)

Then we ran the custom script `SSH-cus-script.py`, which tries multiple passwords until it finds the correct one:

![Brute-force success](images/script_success_output.png)


