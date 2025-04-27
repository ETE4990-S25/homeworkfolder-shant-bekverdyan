import docker
import socket

client = docker.from_env()

def get_container_ip(container_name):
    
    try:
        container = client.containers.get(container_name)
        networks = container.attrs['NetworkSettings']['Networks']
        for _, net_data in networks.items():
            if net_data['IPAddress']:
                return net_data['IPAddress']
        return None
    
    except docker.errors.NotFound:
        print(f"Container '{container_name}' not found.")
        return None

def check_ip_availability(ip_address, port):

    if not ip_address:
        return False
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        sock.connect((ip_address, port))
        sock.close()
        return True
    
    except (socket.error, socket.timeout):
        return False

if __name__ == "__main__":
    
    containers_to_check = ["mysql", "adminer"]
    
    for container_name in containers_to_check:
        
        ip_address = get_container_ip(container_name)
        if ip_address:
            print(f"Container '{container_name}' has IP: {ip_address}")
            
            port = 3306 if container_name == "mysql" else 8080 

            if check_ip_availability(ip_address, port):
                print(f"  - {container_name} is reachable on {ip_address}:{port}")
            else:
                print(f"  - {container_name} is NOT reachable on {ip_address}:{port}")

        else:
            print(f"Could not retrieve IP for {container_name}")