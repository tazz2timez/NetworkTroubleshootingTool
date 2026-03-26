Python 3.14.3 (v3.14.3:323c59a5e34, Feb  3 2026, 11:41:37) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
import subprocess
import platform
import socket
import re

TARGET = "google.com"


def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False


def resolve_dns(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        return None


def ping(target):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "4", target]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout


def extract_latency(output):
    for line in output.split("\n"):
        if "avg" in line or "Average" in line or "min/avg/max" in line:
            return line.strip()
    return "Latency info not found"


def extract_packet_loss(output):
    match = re.search(r"(\d+)% packet loss", output)
    if match:
        return match.group(1) + "%"
    return "Packet loss info not found"


def traceroute(target):
    cmd = "tracert" if platform.system().lower() == "windows" else "traceroute"
    try:
        result = subprocess.run([cmd, target], capture_output=True, text=True)
        return result.stdout
    except Exception:
        return "Traceroute failed"


def speed_test():
    try:
        import speedtest
        st = speedtest.Speedtest()
        st.get_best_server()
        download = st.download() / 1_000_000
        upload = st.upload() / 1_000_000
        return f"Download: {download:.2f} Mbps | Upload: {upload:.2f} Mbps"
    except Exception:
        return "Speed test not available (install speedtest-cli)"

... 
... def main():
...     print("=== Network Troubleshooting Tool ===\n")
... 
...     # Internet Check
...     if not check_internet():
...         print("❌ No internet connection")
...         return
...     print("✅ Internet connection is active\n")
... 
...     # DNS
...     ip = resolve_dns(TARGET)
...     if not ip:
...         print("❌ DNS resolution failed")
...         return
...     print(f"🌍 {TARGET} resolves to {ip}\n")
... 
...     # Ping
...     print(f"📡 Pinging {TARGET}...\n")
...     ping_output = ping(TARGET)
...     print(ping_output)
... 
...     latency = extract_latency(ping_output)
...     packet_loss = extract_packet_loss(ping_output)
... 
...     print("\n📊 Ping Summary:")
...     print(f"Latency: {latency}")
...     print(f"Packet Loss: {packet_loss}\n")
... 
...     # Traceroute
...     print(f"🛣️ Traceroute to {TARGET}:\n")
...     print(traceroute(TARGET))
... 
...     # Speed Test
...     print("⚡ Running speed test...\n")
...     print(speed_test())
... 
... 
... if __name__ == "__main__":
