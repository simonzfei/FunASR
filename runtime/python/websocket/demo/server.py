
"""

# Handler for WebSocket connections
async def handle_connection(websocket):
    async for message in websocket:
        if message == "hello":  # Check if the message is "hello"
            print('--get client')
            await websocket.send("get message")  # Respond with "hi"
        else:
            await websocket.send("I only respond to 'hello'")

# Start the WebSocket server
async def main():
    server = await websockets.serve(handle_connection, "localhost", 12345)
    print("WebSocket server started on ws://localhost:12345")
    await server.wait_closed()

asyncio.run(main())

"""


#---------------2---------

# server

import asyncio
import websockets

# File receiving and processing function
async def handle_connection(websocket, path):
    print("Client connected.")
    received_data = bytearray()
    
    try:
        while True:
            message = await websocket.recv()
            
            if message == "EOF":  # End of file transfer
                print("Received EOF. File transfer complete.")
                # Handle the received data (e.g., save to a file)
                with open("received_file.txt", "wb") as output_file:
                    output_file.write(received_data)
                await websocket.send("File successfully received and saved.")
                break
            else:
                # Append received chunk to the buffer
                received_data.extend(message)
                print(f"Received chunk of size {len(message)} bytes.")
                await websocket.send("Chunk received.")
    except websockets.ConnectionClosed:
        print("Client disconnected.")
    except Exception as e:
        print(f"Error: {e}")

# Start the WebSocket server
start_server = websockets.serve(handle_connection, "localhost", 12345)

print("WebSocket server started at ws://localhost:12345")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

