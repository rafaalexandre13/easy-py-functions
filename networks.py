import socket
import re


def get_my_ipv4():
    """
    Show ip address of the local machine
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('255.255.255.0', 0))
    return s.getsockname()[0]


def sum_mac_address(mac_address, value):
    """
    Sum the MAC Address with :value
    """

    int_mac_address = int(''.join(mac_address.split(':')), 16)
    new_mac_address = hex(int_mac_address + value).split('x')[-1]
    new_mac_address = re.sub(r"(..)", "\\1:", new_mac_address)[:-1]
    return new_mac_address.upper()
