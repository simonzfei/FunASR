import asyncio
import websockets

# Client function
async def client():
    uri = "ws://localhost:12345"  # Server address
    async with websockets.connect(uri) as websocket:
        await websocket.send("hello")  # Send "hello" to the server
        response = await websocket.recv()  # Wait for the server's response
        print(f"Server response: {response}")  # Print the server's response

asyncio.run(client())