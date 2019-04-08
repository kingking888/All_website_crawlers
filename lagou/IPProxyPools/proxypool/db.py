import redis
from proxypool.error import PoolEmptyError
from proxypool.setting import HOST, PORT, PASSWORD


class RedisClient(object):
    def __init__(self, host=HOST, port=PORT):
        if PASSWORD:
            self._db = redis.Redis(host=host, port=port, password=PASSWORD)
        else:
            self._db = redis.Redis(host=host, port=port)

    def get(self, count=1):
        """
        get LGProxies from redis
        """
        LGProxies = self._db.lrange("LGProxies", 0, count - 1)
        self._db.ltrim("LGProxies", count, -1)
        return LGProxies

    def put(self, proxy):
        """
        add proxy to right top
        """
        self._db.rpush("LGProxies", proxy)

    def pop(self):
        """
        get proxy from right.
        """
        try:
            return self._db.rpop("LGProxies").decode('utf-8')
        except:
            raise PoolEmptyError

    @property
    def queue_len(self):
        """
        get length from queue.
        """
        return self._db.llen("LGProxies")

    def flush(self):
        """
        flush db
        """
        self._db.flushall()


if __name__ == '__main__':
    conn = RedisClient()
    print(conn.pop())
