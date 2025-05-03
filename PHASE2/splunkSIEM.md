---
# Phase 2 - SIEM Dashboard Analysis using Splunk on Kali
In this phase, we used **Splunk on Kali Linux** to analyze logs collected from the victim machine (**Metasploitable3**).
...
After multiple attempts to install and configure the **Splunk Universal Forwarder** on the victim, we encountered persistent compatibility errors due to the outdated operating system and unsupported architecture.
As a result, we decided to adopt a **manual approach**:

* Log files were securely transferred using `scp` from the victim to the attacker machine (Kali),
* Then uploaded to Splunk for visualization and analysis.
---
## Step 1: Install Splunk on Kali Linux

We downloaded and installed **Splunk Enterprise** on Kali Linux using the `.deb` package.
After accepting the license and starting the service, we accessed the Splunk Web Interface at:
[http://localhost:8000/](http://localhost:8000/)

![Initial Splunk Configuration and Web Interface Launch on Kali Linux](images/Initial_Splunk_Configuration_and_Web_Interface_Launch_on_Kali_Linux.png)
![Installing Splunk on Kali Linux using dpkg](images/Installing_Splunk_on_Kali_Linux_using_dpkg.png)

---

## Step 2: Access Splunk Web Interface

We logged into Splunk Web Interface using the **admin credentials** set during the initial setup.

![SCP Log Transfer Process](images/SCP_Log_Transfer_Process.png)
![Splunk Enterprise Dashboard - Administrator View on Kali Linux VM](images/Splunk_Enterprise_Dashboard-Administrator_View_on_Kali_Linux_VM.png)

---

## Step 3: Manually Upload Log Files to Splunk

We used the `scp` command on Kali to copy the file from the victim (Metasploitable3):

```bash
scp vagrant@<victim-ip>:/home/vagrant/auth.log ~/Desktop/
```

Then, we used **Splunk Web**:

> `Add Data` → `Upload File`
> to ingest the log file into the system.

✅ The log file was uploaded successfully to Splunk and is ready for searching and analysis.

![Splunk Enterprise Data Upload Review Screen](images/Splunk_Enterprise_Data_Upload_Review_Screen.png)
![Splunk Enterprise Login Screen on Kali Linux Virtual Machine](images/Splunk_Enterprise_Login_Screen_on_Kali_Linux_Virtual_Machine.png)
![Splunk Event Analysis Interface - Timeline Visualization of Security Logs](images/Splunk_Event_Analysis_Interface-Timeline_Visualization_of_Security_Logs.png)


---

## Step 4: Search and Analyze Logs

We used the **Splunk Search & Reporting App** to:

* Analyze login attempts
* Track failed authentications
* Investigate SSH behavior

This helped us identify successful and failed SSH login attempts initiated during the attack.

![Splunk Pivot Configuration Interface - Time Series Analysis Dashboard](images/Splunk_Pivot_Configuration_Interface-Time_Series_Analysis_Dashboard.png)
![Splunk Security Event Timeline - Authentication Log Analysis](images/Splunk_Security_Event_Timeline-Authentication_Log_Analysis.png)

---

## Step 5: Dashboard Visualization

📈 This spike in the graph indicates a **significant increase in events** related to unauthorized access attempts.
The rise reflects the attacker's **repeated SSH login attempts**, which were captured by the system and visualized through Splunk dashboards.

![Splunk Web Interface](images/Splunk_Web_Interface.png)

---


