#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import websockets

async def receive_audio(websocket, filename):
    total_data = b''
    async for message in websocket:
        total_data += message
        with open(filename, 'wb') as file:
            file.write(total_data)
    print("接收数据完毕！")

async def main():
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        await websocket.send("goldenfish.wav")
        await receive_audio(websocket, "received_goldenfish.wav")
        # 可以继续发送其他音频文件请求

if __name__ == "__main__":
    asyncio.run(main())