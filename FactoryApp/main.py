from rq import Queue
from redis import Redis
from job import get_entry
import time
import json

redis_conn = Redis()
q = Queue(connection=redis_conn)

url = 'https://www.avito.ru/moskva?q=ps4'

if __name__ == "__main__":
    while True:
        time.sleep(1)
        job = q.enqueue(get_entry, url)