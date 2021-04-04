from Settings import MESSAGE_COLLECTION

class ItemModel():
    def __init__(self, item_id, short_description, avito_url, post_date):
        self.item_id = item_id
        self.short_description = short_description
        self.avito_url = avito_url
        self.post_date = post_date

    async def save(self, db):
        result = await db[MESSAGE_COLLECTION].insert({
            'id': self.item_id,
            'name': self.short_description,
            'url': self.avito_url,
            'date': self.post_date
        })

        return result

    @staticmethod
    async def get(db, item_id):
        q = { 'id': item_id }
        result = await db[MESSAGE_COLLECTION].find(q)

        return result