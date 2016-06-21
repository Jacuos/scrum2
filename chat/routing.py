
from channels.staticfiles import StaticFilesConsumer
from channels.routing import route
from . import consumers

channel_routing = [
    route('http.request', consumers.hold, path=r'^/hold/$'),
    route('http.request', StaticFilesConsumer()),
    route('websocket.connect', consumers.connect),
    route('websocket.receive', consumers.receive),
    route('websocket.disconnect', consumers.disconnect)
]
