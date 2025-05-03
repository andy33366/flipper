# multiplayer/client.py
# handles websocket stuff for the client

import asyncio
import websockets

class Client():
    def __init__(self, host="localhost", port=8765):
        #idk
        self.uri = f"ws://{host}:{port}"

    async def run(self):
        try:
            async with websockets.connect(self.uri) as websocket:
                msg = "I am the client. hear me roar"
                await websocket.send(msg)
                print("sending msg to server")
                response = await websocket.recv()
                print(f"server says: {response}")
        except Exception as e:
            print(f"failed to connect: {e}")

    def start(self):
        asyncio.run(self.run())
