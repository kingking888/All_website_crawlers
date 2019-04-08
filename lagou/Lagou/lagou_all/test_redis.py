import redis

ips = []

def input_ips():
    ip_db = redis.StrictRedis()
    ip_pools = ip_db.lrange("LGProxies", 0, -1)
    for item in ip_pools:
        ip = str(item, encoding='utf-8')
        ips.append(ip)
    print(ips)

input_ips()
