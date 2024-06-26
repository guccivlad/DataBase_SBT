import redis
import json
import time

client = redis.Redis(host='localhost', port=6379, db=0)

start_time_hset = time.time()
json_hset = client.hgetall('hset')
end_time_hset = time.time()

start_time_zset = time.time()
json_zset = client.zrange('zset', 0, -1)
end_time_zset = time.time()

start_time_list = time.time()
json_list = client.lrange('json_list', 0, -1)
end_time_list = time.time()

start_time_string = time.time()
json_list = client.get('string')
end_time_string = time.time()

print("Time taken to read hset data: ", end_time_hset - start_time_hset)
print("Time taken to read zset data: ", end_time_zset - start_time_zset)
print("Time taken to read list data: ", end_time_list - start_time_list)
print("Time taken to read string data: ", end_time_string - start_time_string)