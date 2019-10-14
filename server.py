#!/usr/bin/env python

# WS server example

import asyncio
import websockets

messages = []

async def consumer(websocket, message):
    # messages.append(message)
    print(f'Messages: {messages}')
    await websocket.send(message)

async def consumer_handler(websocket, path):
    print(f'User connected.')
    async for message in websocket:
        await consumer(websocket, message)

start_server = websockets.serve(consumer_handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
