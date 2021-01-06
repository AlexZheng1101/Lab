from datetime import datetime
import websockets,asyncio

loop=asyncio.get_event_loop()

async def time(websocket, path):
    while True:
        now = datetime.utcnow().isoformat()
        await websocket.send(now) 
        await asyncio.sleep(1)

start_server = websockets.serve(time, "127.0.0.1", 1000)
loop.run_until_complete(start_server)
loop.run_forever()
