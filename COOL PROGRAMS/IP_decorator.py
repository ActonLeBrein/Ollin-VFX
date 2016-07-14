import ipaddr

WHITELIST = (
    '64.12.193.85',
    '64.207.133.18',
    '74.125.0.0/16'
)

def ip_in_whitelist(request_ip):
    user_ip = ipaddr.IPv4Address(request_ip)
    print user_ip
    for whitelist_ip in WHITELIST:
        w_ip = ipaddr.IPv4Address(whitelist_ip)
        if (user_ip == ipaddr.IPv4Network(w_ip)) or ((user_ip >= ipaddr.IPv4Network(w_ip)) and (user_ip < w_ip.broadcast)):
            return True
    return False

print ip_in_whitelist('64.12.193.85')