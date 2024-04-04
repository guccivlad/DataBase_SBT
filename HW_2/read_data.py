import redis
import json
import time


# file = open("trade-indexes.json")

# client = redis.Redis(host='localhost', port=6379, db=0)

# data = json.load(file)
# data_json_str = json.dumps(data)
# start_time = time.time()

# client.zadd('zset', {data_json_str : 1})

# end_time = time.time()

# file.close()

# print("Time taken to upload zset: ", end_time - start_time)

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

print("Time taken: ", end_time_zset - start_time_zset)