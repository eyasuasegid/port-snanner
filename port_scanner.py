import socket
import argparse

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            try:
                banner = sock.recv(1024).decode().strip()
            except:
                banner = "No banner"
            print(f"[+] Port {port} is open - {banner}")
        sock.close()
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted.")
        exit()
    except socket.gaierror:
        print("[!] Hostname could not be resolved.")
        exit()
    except socket.error:
        print("[!] Couldn't connect to server.")
        exit()

def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("host", help="Target host (IP or domain)")
    parser.add_argument("-p", "--ports", help="Port range, e.g., 20-100", default="1-1024")
    args = parser.parse_args()

    host = args.host
    port_range = args.ports.split("-")
    start_port = int(port_range[0])
    end_port = int(port_range[1])

    print(f"[*] Scanning host: {host} from port {start_port} to {end_port}")
    for port in range(start_port, end_port + 1):
        scan_port(host, port)

if __name__ == "__main__":
    main()
