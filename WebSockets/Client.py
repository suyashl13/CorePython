import asyncio
import websockets


async def hello(websocket, path):
    name = await websocket.recv()

    greeting = f"Hello {name}"
    print(greeting)

try:
    start_server = websockets.serve(hello, 'localhost', 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    print("Session Over..")