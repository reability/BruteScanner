from WSService.Controller import WebSocket
from ItemsService.Controller import ItemController

routes = [
    ('GET', '/ws',      WebSocket, 'service'),
    ('POST', '/item',   ItemController,     'Item'),
]