import asyncio
import websockets

# Handler for WebSocket connections
async def handle_connection(websocket):
    async for message in websocket:
        if message == "hello":  # Check if the message is "hello"
            await websocket.send("get message")  # Respond with "hi"
        else:
            await websocket.send("I only respond to 'hello'")

# Start the WebSocket server
async def main():
    server = await websockets.serve(handle_connection, "localhost", 12345)
    print("WebSocket server started on ws://localhost:12345")
    await server.wait_closed()

asyncio.run(main())


#---------------2---------
"""
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


# client

import asyncio
import websockets

# File path to send
file_path = "path/to/your/file.txt"

# Send method
async def send_to_server(uri):
    async with websockets.connect(uri) as websocket:
        print(f"Connected to {uri}")
        
        # Open the file and read it in chunks
        with open(file_path, "rb") as file:
            chunk_size = 1024  # 1KB per chunk
            while chunk := file.read(chunk_size):
                # Send each chunk to the server
                await websocket.send(chunk)
                print("Sent a chunk to the server.")

        # Indicate end of file transfer
        await websocket.send("EOF")
        print("File transfer complete.")
        return websocket

# Receive method
async def receive_from_server(uri):
    async with websockets.connect(uri) as websocket:
        while True:
            try:
                # Receive a message from the server
                response = await websocket.recv()
                print(f"Server response: {response}")
            except websockets.ConnectionClosed:
                print("Connection closed by the server.")
                break

# Run both send and receive concurrently
async def main(uri):
    async with websockets.connect(uri) as websocket:
        await asyncio.gather(
            send_to_server(websocket),
            receive_from_server(websocket)
        )
"""