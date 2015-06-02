# Write a function that takes two string parameters, an IP (v4) address and
# a subnet mask, and returns two strings: the network block,
# and the host identifier.

# For example:
# >>> print ipv4__parser('192.168.50.1', '255.255.255.0')
# ('192.168.50.0', '0.0.0.1')

def ipv4__parser(ip_addr, mask):
    l1 = map(int, ip_addr.split('.'))
    l2 = map(int, mask.split('.'))

    net_addr = '.'.join([str(l1[i] & l2[i]) for i in range(4)])
    last1, last2 = l1[-1], l2[-1]
    if last2 == 0:
        host_addr = '0.0.0.{}'.format(l1[-1])
    else:
        host_addr = '0.0.0.{}'.format( ~last2 & last1)
    return net_addr, host_addr


print ipv4__parser('192.168.50.1', '255.255.255.0')

print ( ~225 & 153)