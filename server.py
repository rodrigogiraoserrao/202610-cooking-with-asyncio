import asyncio


class Server:
    def __init__(self, host, port):
        print("Initialising server.")
        self.host = host
        self.port = port

    async def connection_callback(self, reader, writer):
        """Implements an echo server.

        Contains an infinite loop that reads data from the reader
        and sends it back to the writer.
        """
        print("Connection received!")
        while True:
            data = await reader.readline()
            print(f"\tServer got {data = }.")
            writer.write(data)

    async def run(self):
        """Creates and runs the `asyncio` server.

        Initialises an `asyncio` server with the attributes passed earlier
        and then uses the method `server_forever` to listen for connections.
        """
        print("Starting server...")
        server = await asyncio.start_server(
            self.connection_callback,  # server logic
            self.host,                 # host
            self.port,                 # port
        )
        await server.serve_forever()


async def main():
    server = Server("localhost", 7342)
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())