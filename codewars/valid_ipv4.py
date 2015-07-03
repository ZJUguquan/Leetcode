def is_valid_IP(strng):
    if ' ' in strng:
        return False
    ip = strng.split('.')

    for i in ip:
            if len(i) > 1 and i[0] == '0':
                return False
    print ip
    try:


        return len(ip) == 4 and all( 0<= int(i) <= 255   for i in ip)
    except:
        return False