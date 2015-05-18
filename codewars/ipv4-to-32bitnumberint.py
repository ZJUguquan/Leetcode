def ip_to_int32(ip):
    s = map(lambda x: bin(int(x))[2:] , ip.split('.') )
    x = ''.join(s)
    return  int(x, 2)


ip = '128.114.17.104'
print bin(128)
print bin(114)
print bin(17)
print bin(104)

print ip_to_int32(ip)