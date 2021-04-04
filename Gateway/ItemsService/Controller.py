from aiohttp import web
from aiohttp import WSMsgType

from Settings import log
from ItemsService.Model import ItemModel

class ItemController(web.View):
    async def post(self):

        body =  await self.request.post()
        print(body)

        _id = body["id"]
        _name = body["name"]
        _url = body["url"]
        _date = body["body"]

        item = ItemModel(_id, _name, _url, _date)
        await item.save(self.request.db)

        print('DB insertinh')

        for _ws in self.request.app['websockets']:
            print("Socket")
            await _ws.send_json(
                { "id": _id,
                  "name": _name,
                 }
            )

        return web.Response()