import socket


def get_ipv4():
    # TODO: Document function

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('255.255.255.0', 0))
    return s.getsockname()[0]


# print(get_ipv4())
