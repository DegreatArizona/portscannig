import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

common_ports = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    143: 'IMAP',
    443: 'HTTPS',
    445: 'SMB',
    3306: 'MySQL',
    3389: 'RDP',
    5900: 'VNC',
    8080: 'HTTP-alt',
}

def get_service_name(port):
    return common_ports.get(port, 'Unknown')

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} ({get_service_name(port)}) is open")
        else:
            print(f"Port {port} ({get_service_name(port)}) is closed or filtered")
        sock.close()
    except socket.timeout:
        print(f"Port {port} ({get_service_name(port)}) is filtered (timeout)")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def scan_ports(host, ports):
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports:
            executor.submit(scan_port, host, port)

def main():
    parser = argparse.ArgumentParser(description="Port Scanner Plus")
    parser.add_argument("host", type=str, help="Host to scan")
    parser.add_argument("-p", "--ports", type=str, help="Comma-separated list of ports to scan (e.g., 22,80,443)")
    args = parser.parse_args()

    host = args.host
    ports = list(map(int, args.ports.split(','))) if args.ports else range(1, 1025)  
    
    print(f"Scanning host {host} on ports {ports}")
    scan_ports(host, ports)

if __name__ == "__main__":
    main()
