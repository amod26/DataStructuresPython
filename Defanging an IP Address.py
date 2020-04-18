# given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

address = "255.100.50.0"


def defangIPaddr(address):
    address = address.split(".")
    return "[.]".join(address)


defangIPaddr(address)
