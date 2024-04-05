import socket
target_host = input("Input Target Host: ")
target_port = [int(port) for port in input("Input two or more port 'Separated by comma': ").split(",")]
def scan_port(target_host, target_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, target_port))
        if result == 0:
            print(f"Port {target_port} is open")
        elif result >= 1:
            print(f"Port {target_port} is closed")
        sock.close()
    except Exception as e:
        print(f"Error scanning {target_port}: {e}")
for port in target_port:
    scan_port(target_host, port)
