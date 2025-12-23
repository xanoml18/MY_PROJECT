import subprocess
import sys


ip_address = input("Enter IP address or hostname (e.g. 192.168.1.1 or scanme.nmap.org): ").strip()

def run_nmap(ip):
 
    command = ["nmap", "-sL", ip]  

    print("Running Nmap command:", " ".join(command))
    print("==================\n")

    try:
       
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout  
    except subprocess.CalledProcessError as e:
        return f"Error running Nmap: {e.stderr}"
    except FileNotFoundError:
        return "Nmap is not installed or not found in PATH. Run 'sudo apt install nmap'"


output = run_nmap(ip_address)

print(f"IP/Hostname: {ip_address}")
print("Nmap Output:")
print(output)