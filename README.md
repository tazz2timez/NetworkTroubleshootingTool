# 🌐 Network Troubleshooting Tool (Python)

## 📌 Overview
This project is a Python-based network troubleshooting tool designed to diagnose common connectivity issues. It performs internet checks, DNS resolution, latency analysis, packet loss detection, traceroute, and optional bandwidth testing.

Built to simulate real-world IT support and networking diagnostics.

---

## 🧠 Features
- Check internet connectivity  
- Resolve domain names to IP addresses  
- Ping a target (latency analysis)  
- Detect packet loss  
- Perform traceroute (network path analysis)  
- Optional download/upload speed test  

---

## 🛠️ Technologies Used
- Python 3  
- subprocess  
- socket  
- platform  
- re  
- speedtest-cli (optional)  

---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/network-troubleshooting-tool.git
cd network-troubleshooting-tool
```

### 2. Run the script
```bash
python network_tool.py
```

### 3. (Optional) Install speed test dependency
```bash
pip install speedtest-cli
```

---

## 📌 Example Output
```
=== Network Troubleshooting Tool ===

Internet connection is active
google.com resolves to 142.250.x.x

Pinging google.com...

Latency: min/avg/max = 10/15/20 ms
Packet Loss: 0%

Traceroute:
...

Download: 120.50 Mbps | Upload: 25.30 Mbps
```

---

## 📄 Use Case
This tool helps identify:
- Connectivity issues  
- DNS failures  
- High latency  
- Packet loss  
- Network routing problems  

It can be used as a quick diagnostic utility in IT support or networking environments.

---

## 🚀 Future Improvements
- Add CLI arguments (e.g., `--target`, `--count`)  
- Export results to CSV or JSON  
- Continuous monitoring mode  
- GUI dashboard  

---

## 💡 What I Learned
- Network troubleshooting fundamentals (latency, packet loss, DNS)  
- Using Python for system-level operations  
- Parsing and analyzing command-line output  
- Building practical tools for real-world IT scenarios  

---


Python network troubleshooting tool that checks connectivity, analyzes latency and packet loss, performs traceroute, and runs optional speed tests for real-world diagnostics.
