import sys
import time
import random
from colorama import init, Fore, Style

init(autoreset=True)

log_pool = [
    "Nikto: Scanning target.com [port 80]",
    "Hydra: Brute force ssh on 192.168.1.100",
    "SQLMap: Testing connection to the target URL...",
    "SQLMap: Injection point found in parameter 'id'",
    "DDoS attack: 5000 packets sent in 10s",
    "ARP spoofing on 192.168.1.1 - success",
    "Uploading payload via /upload.php",
    "Bypassing WAF using unicode obfuscation",
    "BurpSuite: Intercepted login request with credentials",
    "Captured cookies: JSESSIONID=ab23xz9q...",
    "Shellshock vuln detected at /cgi-bin/admin.sh",
    "Executing: nmap -sV -Pn 10.10.10.10",
    "Reverse shell connected: 10.10.10.10:4444",
    "Cracking WPA2 handshake with aircrack-ng...",
    "Ping of death sent to 8.8.8.8",
    "SMB enumeration: anonymous login allowed",
    "Enumerating directories with dirb...",
    "Response code 200 OK from /admin/login",
    "SNMP community string: public",
    "Exploit CVE-2022-1388 against F5 BIG-IP",
    "Metasploit: ms17_010 success, shell opened",
    "Found JWT token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "Exfiltrating data over DNS tunnel...",
    "Crontab hijacked with malicious job",
    "Payload executed via XSS in comment field",
    # Thêm dữ liệu mới
    "Heartbleed vulnerability detected",
    "Zero-day exploit activated: CVE-2023-32456",
    "Bypassing 2FA using session hijacking",
    "DNS cache poisoning attempt",
    "RFID cloning successful",
    "ICS/SCADA system compromised",
    "PLC backdoor installed",
    "ATM jackpotting in progress",
    "WiFi pineapple attack started",
    "BlueBorne attack vector deployed",
    "BadUSB payload delivered",
    "RAM scraping malware injected",
    "Point-of-Sale system breached",
    "ICS: Stuxnet-like worm propagating",
    "AI model poisoning detected"
]

def glitchy_write(text: str):
    """In từng ký tự theo kiểu giật lag không mượt để mô phỏng máy cũ"""
    i = 0
    while i < len(text):
        chunk_size = random.choice([1, 1, 2])  # đôi khi nhảy 2 ký tự
        chunk = text[i:i+chunk_size]
        sys.stdout.write(chunk)
        sys.stdout.flush()
        i += chunk_size
        delay = random.uniform(0.02, 0.1) if random.random() < 0.8 else random.uniform(0.15, 0.25)
        time.sleep(delay)
    print()

def print_log(log: str):
    """In log với màu sắc tinh tế chỉ khi cần thiết"""
    # Chỉ highlight các dòng quan trọng hoặc nguy hiểm
    if "success" in log.lower() or "vuln" in log.lower() or "exploit" in log.lower():
        print(Fore.RED + Style.BRIGHT + log)
    elif "warning" in log.lower() or "alert" in log.lower():
        print(Fore.YELLOW + log)
    elif "connected" in log.lower() or "executing" in log.lower():
        print(Fore.CYAN + log)
    elif "detected" in log.lower() or "breached" in log.lower() or "compromised" in log.lower():
        print(Fore.MAGENTA + Style.BRIGHT + log)  # Màu hồng cho các sự kiện phát hiện
    elif "attack" in log.lower() or "injected" in log.lower() or "poisoning" in log.lower():
        print(Fore.LIGHTRED_EX + log)  # Màu đỏ nhạt cho các cuộc tấn công
    else:
        print(log)

def simulate_output():
    last_ddos_time = time.time() - 300  # đảm bảo chạy được lần đầu

    try:  
        while True:  
            current_time = time.time()  
            if current_time - last_ddos_time >= 300:  # >= 5 phút  
                ddos_attack_simulation()  
                last_ddos_time = current_time  
                continue  

            mode = random.choice(["glitchy", "fast", "burst"])  

            if mode == "glitchy":  
                glitchy_write(random.choice(log_pool))  
                time.sleep(random.uniform(0.3, 0.6))  

            elif mode == "fast":  
                for _ in range(random.randint(2, 5)):  
                    print_log(random.choice(log_pool))  
                    time.sleep(random.uniform(0.05, 0.12))  

            elif mode == "burst":  
                for _ in range(random.randint(8, 15)):  
                    print_log(random.choice(log_pool))  
                time.sleep(random.uniform(0.1, 0.4))  

            if random.random() < 0.1:  
                time.sleep(random.uniform(0.7, 1.4))  # mô phỏng delay  

    except KeyboardInterrupt:  
        print("\n[!] Simulation terminated.")

def ddos_attack_simulation():
    ddos_icon = [
        "         .e$$$$e.",
        "       e$$$$$$$$$$e",
        "      $$$$$$$$$$$$$$",
        "     d$$$$$$$$$$$$$$b",
        "     $$$$$$$$$$$$$$$$",
        "    4$$$$$$$$$$$$$$$$F",
        "    4$$$$$$$$$$$$$$$$F",
        "     $$$\" \"$$$$\" \"$$$",
        "     $$F   4$$F   4$$",
        "     '$F   4$$F   4$\"",
        "      $$   $$$$   $P",
        "      4$$$$$\"^$$$$$%",
        "       $$$$F  4$$$$",
        "        \"$$$ee$$$\"",
        "        . *$$$$F4",
        "         $     .$",
        "         \"$$$$$$\"",
        "          ^$$$$",
        " 4$$c       \"\"       .$$r",
        " ^$$$b              e$$$\"",
        " d$$$$$e          z$$$$$b",
        "4$$$*$$$$$c    .$$$$$*$$$r",
        " \"\"    ^*$$$be$$$*\"    ^\"",
        "          \"$$$$\"",
        "        .d$$P$$$b",
        "       d$$P   ^$$$b",
        "   .ed$$$\"      \"$$$be.",
        " $$$$$$P          *$$$$$$",
        "4$$$$$P            $$$$$$\"",
        " \"*$$$\"            ^$$P",
        "    \"\"              ^\""
    ]

    # In icon với hiệu ứng từng dòng nhanh
    for line in ddos_icon:
        print(Fore.RED + line)
        time.sleep(0.03)  # Thời gian delay ngắn để tạo hiệu ứng

    ddos_payloads = [
        "Sending SYN packet to 203.0.113.5:80",
        "UDP flood 192.168.0.10:53 - 4500 pps",
        "TCP ACK attack to 10.0.0.1:443",
        "HTTP GET /index.php?=A"*10,
        "ICMP packet sent to 8.8.8.8 - size=65500",
        "Spoofed packet from 45.32.1.10 to 172.16.0.5",
        "Sending oversized packet to 192.0.2.1:80",
        "Burst 1000 packets to 203.0.113.7",
        "Malformed TCP header sent to 10.10.10.10",
        "Xmas scan packet to 192.168.1.200",
        "Flooding port 22 with 10k SSH requests",
        "Overlapping fragment sent to 192.168.1.1",
        "Sending crafted packet payload: \x41\x41\x41...",
        # Thêm payload mới
        "IoT botnet activated: 15,000 devices online",
        "DNS amplification attack initiated",
        "NTP reflection attack in progress",
        "SSDP flood targeting UDP port 1900",
        "Memcached DRDoS attack launched",
        "Slowloris attack keeping connections open",
        "RUDY attack: long form field submissions"
    ]

    try:  
        for _ in range(random.randint(30, 80)):  # Burst 30-80 dòng  
            line = random.choice(ddos_payloads)  
            print(Fore.RED + Style.BRIGHT + line)  
            time.sleep(random.uniform(0.005, 0.02))  # rất nhanh  
    except KeyboardInterrupt:  
        print("\n[!] DDoS simulation stopped.")

if __name__ == "__main__":
    simulate_output()