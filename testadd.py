import redis

pool=redis.ConnectionPool(host='192.168.25.132',port=6379,max_connections=1000)
r=redis.Redis(connection_pool=pool)
r.sadd("set1", 33, 44, 55, 66)
r.sadd("set2", 11, 22, 33)

print(r.get('foo'))