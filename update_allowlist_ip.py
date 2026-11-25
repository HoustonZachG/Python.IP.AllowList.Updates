def update_file(import_file, remove_list):
    # Read initial contents of the allow list file
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    # Convert the continuous string into a list of individual IP addresses
    ip_addresses = ip_addresses.split()

    # Iterate through the allow list and remove any unauthorized IPs
    for element in ip_addresses:
        if element in remove_list:
            ip_addresses.remove(element)

    # Convert the revised list back into a space-separated string
    ip_addresses = " ".join(ip_addresses)

    # Overwrite the original file with only authorized IP addresses
    with open(import_file, "w") as file:
        file.write(ip_addresses)


if name_== "main":
    # Sample list of revoked IP addresses
    revoked_ips = ["192.168.25.60", "192.168.140.81", "192.168.203.198"]
    update_file("allow_list.txt", revoked_ips)

    # Verify updated file contents
    with open("allow_list.txt", "r") as file:
        print("Updated Allow List:", file.read())
