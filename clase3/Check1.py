import re
import os
import ipaddress

#ddirectories=os.popen('uufind /var/log -name \*.log').read()
#directories=ddirectories.split()
#print("Los directorios con archivo de log son \n", directories, "\n")
#private_ips = set()
#ip_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

"""
Reminder to listcompress and parametrizar
"""

def checker(logfolder="/var/log", ip_regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" ):

    """
    Function that scans the local file system and looks for files containing internal valid IP addresses

    The function stores this information on a list

    directories is a list containing the full path to the FILES
    """
    command=('find '+str(logfolder)+' -name \*.log')
    directories=os.popen(command).read().split()
    private_ips = set()
    print(directories)
    for filename in directories:
     # Open the file
        try:
            with open(filename, 'r') as file:
         # Loop through each line in the file
                for line in file:
             #Find all IP addresses in the line using regex
                    ips = re.findall(ip_regex, line)
             #Loop through each IP address found
                    for ip in ips:
                 #Check if the IP address is private and not already in the set
                        if ipaddress.ip_address(ip).is_private and ip not in private_ips:
                     #Add the IP address to the set of private IPs
                            private_ips.add(ip)
                            print("ip encontrada en ", filename, "\n")
        except Exception as e:
            print(e)
            print("excepcion encontrada en", filename, "\n")
            pass
#Convert the set of private IPs to a list
    private_ips = list(private_ips)
    print(private_ips)
    return(private_ips)

def scanner(ip_list=["0.0.0.0", "192.168.0.75" ], rangeports=82):
    """
    Function that scans a list of ips and saves the corresponding open ports
    ip_list contains a list of valid ip addresses

    """
    import socket
    def scan_ports(ip_address):
        """
        Function that will scan ports for 1 untill default  82
        rangeports contains upper limit of scan

        """
        open_ports = []
        for port in range(1, rangeports):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        return open_ports

    open_ports_list = []

    for ip in ip_list:
        open_ports = scan_ports(ip)
        if len(open_ports) > 0:
            open_ports_str = ", ".join(str(port) for port in open_ports)
            open_ports_list.append(f"{ip}: {open_ports_str}")

    for open_ports in open_ports_list:
        print(open_ports)
    print(open_ports_list)
    return(open_ports_list)
    
def sender(hostname="192.168.0.75", username="User", password="password123", remote_path="C:\/Users\/User\/info", my_list=[1,2,3,4]):
    
    """
    Function that encrypts and sends a file to a remote sftp server
    It uses hostname, username, passowrd, and remote_path variables, my_list contains the information to be sent.
    
    """

    import paramiko
    from cryptography.fernet import Fernet

    # Write the list to a file
    with open("info.txt", "w") as f:
        for item in my_list:
            f.write(str(item) + "\n")

    # Read the file and encrypt its contents
    with open("info.txt", "rb") as f:
        plaintext = f.read()
        key = Fernet.generate_key()
        fernet = Fernet(key)
        ciphertext = fernet.encrypt(plaintext)
    with open("encryptedinfo", "wb") as f:
        f.write(key)
    with open ("encryptedtext","wb") as f:
        f.write(ciphertext)
# Create a new SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote SSH server

    ssh.connect(hostname, username=username, password=password)

# Create an SFTP session
    sftp = ssh.open_sftp()

# Upload the encrypted file to the remote server 
    sftp.put("encryptedinfo", remote_path+"key")
    sftp.put("encryptedtext", remote_path+"text")       
# Close the SFTP session and SSH connection
    sftp.close()
    ssh.close()
    return(fernet)
if __name__ == "__main__":
    sender(my_list=scanner(ip_list=(checker())))
