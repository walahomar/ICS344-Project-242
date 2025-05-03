```
# ICS344 Course Project

## Phase 1: Setup and Compromise the Service

In Phase 1, we set up the attacker and victim machines by following the steps on the official repository for the ICS 344 Course. Then, we compromised the SSH service on Metasploitable, which is already vulnerable, from the attacker machine to the victim machine (Metasploitable). After that, we created a Python script to brute force SSH authentication of the Metasploitable server.

---

## Victim Environment

After downloading Metasploitable and installing it on VirtualBox:

![Metasploitable VM Boot Screen](images/metasploitable_boot_screen.jpg)

Logging in with the username and password “vagrant”:

![Login to Metasploitable](images/metasploitable_login.jpg)

After running the command `ifconfig`, it will show the IP of Metasploitable which is `192.168.56.101`:

![ifconfig Output](images/metasploitable_ifconfig.jpg)

We ran the command `ping 192.168.56.101` to test if there is a connection to Metasploitable. The result shows there is a reply, which indicates there is a connection:

![Ping to Metasploitable](images/metasploitable_ping.jpg)

---

## Attacker Environment

After following the course instructions by downloading and installing Metasploit, we executed the command `.\msfconsole.bat` to run Metasploit from the attacker machine:

![Start Metasploit](images/start_metasploit.jpg)

---

## Task 1.1: Use Kali Linux Tool Metasploit to Compromise the Service

After confirming there is a connection between the attacker and victim machines, we selected the SSH service of Metasploitable to exploit. We ran the command `nmap -p 22 192.168.56.101` to scan the SSH port and confirm it is open and vulnerable. From the screenshot below, we can confirm that the port is open:

![Nmap Scan Port 22](images/nmap_ssh_scan.jpg)

We selected the SSH (port 22) service of Metasploitable to exploit using the module `auxiliary/scanner/ssh/ssh_login` in Metasploit to establish an SSH session. We used the following commands:

```
set rhost 192.168.56.101       # Set the destination IP
set username vagrant           # Set the username
set password vagrant           # Set the password
exploit                        # Run the exploit
```

![Metasploit Exploit SSH](images/metasploit_ssh_exploit.jpg)

As shown above, the exploit was executed successfully, creating an SSH session from the attacker machine to the victim machine. The screenshot below shows the active SSH session:

![Active SSH Session](images/active_ssh_session.jpg)

After executing the attack and establishing the SSH session, we successfully connected to Metasploitable from the command line and ran the `whoami` command, which indicates the service has been compromised and any command can be executed:

![Command Execution](images/command_execution.jpg)

---

## Task 1.2: Compromise the Service Using a Custom Script

After installing Paramiko, a Python library for SSH connections, as shown below:

![Paramiko Installed](images/paramiko_installed.jpg)

We ran the custom script named `SSH-cus-script.py`, which is uploaded to our repository. The script attempts each password from a list (`password_list`), connecting over SSH port 22. It stops when it finds the correct password. If login fails, it tries the next one.

As shown in the screenshot below, the successful attempt used the password: `vagrant`.

![Custom Script Success](images/custom_script_success.jpg)
```
