import socket

def get_user_input():
    ip = input("Enter IP address to scan: ").strip()

    try:
        start_port = int(input("Enter start port (0-65535): ").strip())
        end_port = int(input("Enter end port (0-65535): ").strip())

        if not (0 <= start_port <= 65535 and 0 <= end_port <= 65535):
            raise ValueError("Ports must be in range 0-65535.")
        if start_port > end_port:
            raise ValueError("Start port cannot be greater than end port.")

    except ValueError as ve:
        print(f"Invalid input: {ve}")
        return None, None, None

    return ip, start_port, end_port

def scan_ports(ip, start_port, end_port):
    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is OPEN")
            open_ports.append(port)
        sock.close()

    return open_ports

def main():
    ip, start_port, end_port = get_user_input()
    if ip and start_port is not None:
        open_ports = scan_ports(ip, start_port, end_port)
        if open_ports:
            print("\nOpen ports:", open_ports)
        else:
            print("\nNo open ports found.")

if __name__ == "__main__":
    main()
