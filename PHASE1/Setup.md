# ICS344 Course Project

## Phase 1: Setup and Compromise the Service

In Phase 1, we set up the attacker and victim machines by following the steps from the official repository for the ICS 344 Course. We compromised the SSH service on the Metasploitable VM, which is already vulnerable, by connecting from the attacker machine to the victim. Then, we created a Python script to brute force SSH authentication on the Metasploitable server.

---

## Victim Environment

After downloading and installing Metasploitable on VirtualBox:
### 🖼 Image 1: installing Metasploitable
![Metasploitable VM Boot Screen](images/Metasploitable.png)
### 🖼 Image 2: Login using username and password `vagrant`
![Login with vagrant](images/login_with_vagrant.png)

After running the command “ifconfig”, it will show  the IP of metasploitable which is 192.168.56.101
### 🖼 Image 3: Check the IP address using `ifconfig`
![Check IP address](images/ifconfig_output.png)

### 🖼 Image 4: Verify connection using `ping`
![Ping result](images/ping_success.png)


we have run the command “ping 192.168.56.101” to test if there is connection to the metasploitable, the result shows there is reply which indicates there is connection. 


---
## Attacker Environment

After downloading and installing Kali tools and launching Metasploit using:
```
.\msfconsole.bat
```

---

## Task 1.1: Use Kali Linux tool Metasploit to compromise the service

After confirming there is conneciton between the attacher and victim mchine, We have selected the SSH service of metasploitable to exploit. Furthermore, we have run the command “namp -p 22 192.168.56.101”  in order to scan SSH port is and confirm it is open and vulnerable, from the Screenshoot below we can confirm that the port is open.

### 🖼 Image 5: Result of `nmap -p 22 192.168.56.101`
![Nmap result](images/nmap_ssh_port.png)

We used the Metasploit module: `auxiliary/scanner/ssh/ssh_login` and set the following options:

```
set rhost 192.168.56.101
set username vagrant
set password vagrant
exploit
```

### 🖼 Image 6: Executing the exploit and opening SSH session
![SSH session](images/ssh_exploit_result.png)

As shown in above screen shot, the exploit has been executed successfully by creating the SSH session from the attacker machine to victim machine. the screenshot below shows the active SSH session.

![SSH session](images/ssh_exploit_result2.png)

After opening the session, we used the `whoami` command:

### 🖼 Image 7: Output of `whoami` inside the session
![Whoami result](images/whoami_output.png)

---

## Task 1.2: Compromise the service using a custom script

We installed the Python library `paramiko` for SSH:

### 🖼 Image 8: Installing paramiko library
![Install Paramiko](images/install_paramiko.png)

Then we ran the custom script `SSH-cus-script.py`, which tries multiple passwords until it finds the correct one:

After running the customized script named “SSH-cus-script.py” which is uploaded on our repository.  The script will It tries each password from a listpassword_list).
Connects over SSH port 22. Stops when it finds the correct password. If login fails, it tries the next password. H. as shown in below table the success attempt on password : vagrant.

### 🖼 Image 9: Script success with correct password
![Brute-force success](images/script_success_output.png)

