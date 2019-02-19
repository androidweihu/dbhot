import redis
#
# conn=redis.Redis(host='192.168.25.132',port=6379)
# # conn.set('x1','huge',ex=5)
#
# print(conn.get('x1'))

pool=redis.ConnectionPool(host='192.168.25.132',port=6379,max_connections=1000)
r=redis.Redis(connection_pool=pool)
# r.set('foo','Bar')
print(r.get('foo'))