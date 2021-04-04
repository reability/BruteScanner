

from datetime import datetime
from Settings import MESSAGE_COLLECTION


class Item:

    def __init__(self, db, **kwargs):
        self.collection = db[MESSAGE_COLLECTION]

    async def save(self, user, msg, **kw):
        result = await self.collection.insert({'user': user, 'msg': msg, 'time': datetime.now()})
        return result

    async def get_messages(self):
        messages = self.collection.find().sort([('time', 1)])
        return await messages.to_list(length=None)