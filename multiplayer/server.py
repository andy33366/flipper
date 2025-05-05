# multiplayer/server.py
# handles all server host fundtions

import asyncio
import websockets
from models.Card import Deck

class Server():
    def __init__(self, deck, lobby, host="localhost", port=8765):
        self.deck = deck
        self.host = host
        self.port = port
        self.lobby = lobby
        self.clients = set()
        
    async def handler(self, websocket):
        card = self.deck.get_card(0)
        self.clients.add(websocket)
        self.lobby.players += 1
        self.lobby.set_player_count(self.lobby.players)
        await self.broadcast_player_count()
        try:
            async for message in websocket:
                print(f"message from client: {message}")
                await websocket.send(f"hello, you said {message}")
        finally:
            self.clients.remove(websocket)
            self.lobby.players -= 1
            self.lobby.set_player_count(self.lobby.players)
            await self.broadcast_player_count()

    async def broadcast_player_count(self):
        for client in self.clients:
            try:
                await client.send(f"player_count:{self.lobby.players}")
            except:
                pass
    def start(self):
        '''
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        server = websockets.serve(self.handler, self.host, self.port)
        print(f"server is running on {self.host}:{self.port}")
        loop.run_until_complete(server)
        loop.run_forever()
        '''
        async def run():
            async with websockets.serve(self.handler, self.host, self.port):
                print(f"Server running on {self.host}:{self.port}")
                await asyncio.Future()

        asyncio.run(run())
    
