  
from redis import Redis
import json


r = Redis()


class RedisAdapter:

    @staticmethod
    def create(data):
        """ creates record in Redis """
        id_ = data.get('id')
        r.set(id_, json.dumps(data))

    @staticmethod
    def get(id):
        return json.loads(r.get(id))

    @staticmethod
    def database_match_check(id):
        """ returns data or None """
        return r.get(id)