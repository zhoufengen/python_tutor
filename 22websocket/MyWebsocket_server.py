#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import websockets
import os

CHUNK_SIZE = 1024 * 1024  # 定义每个块的大小

async def send_audio(websocket, path):
    async for message in websocket:
        path = message
        break

    print(f"path={path}")
    file_size = os.path.getsize(path)
    with open(path, 'rb') as file:
        sent_bytes = 0
        while sent_bytes < file_size:
            chunk = file.read(CHUNK_SIZE)
            await websocket.send(chunk)
            sent_bytes += len(chunk)


async def main():
    async with websockets.serve(send_audio, "localhost", 6789):
        print("WebSocket server started at ws://localhost:6789")
        await asyncio.Future()  # 服务器运行直到被关闭

if __name__ == "__main__":
    asyncio.run(main())