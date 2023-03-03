import os
import re

ip_addresses = set()  # Create an empty set to store unique IP addresses

# Walk through the var partition and search for files with IP addresses
for root, dirs, files in os.walk('/var/log'):
    for file in files:
        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r') as f:
                # Read the file and search for IP addresses using regular expressions
                for line in f:
                    ip_matches = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', line)
                    # Add unique IP addresses to the set
                    for ip in ip_matches:
                        ip_addresses.add(ip)
        except Exception as e:
            # Ignore files that we can't open
            pass

# Convert the set to a list and print the unique IP addresses
ip_list = list(ip_addresses)
print(ip_list)
