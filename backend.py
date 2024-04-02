import socket
from threading import Thread
from pybelt.belt_controller import BeltController

belt_controller = BeltController()

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}

    def start(self):
        self.server.bind((self.host, self.port))
        self.server.listen()
        print(f"Server listening on {self.host}:{self.port}")

        try:
            while True:
                client, address = self.server.accept()
                
                print(f"Connected with {address}")

                message = client.recv(1024).decode()
                client.send('confirmation'.encode())
                role, name = message.split(':', 1)

                self.clients[name] = (role, client)

                print(role, name)

                if role == "l":
                    continue
                
                choice = client.recv(1024).decode()
                client.send('confirmation'.encode())
                
                destination = self.clients[choice][1]

                Thread(target=self.handle_client, args=(client,role,destination,)).start()
        except KeyboardInterrupt:
            print("Shutting down server")
            self.close_all_clients()
            self.shutdown()

    def close_all_clients(self):
        for name, (role, client) in self.clients.items():
                client.close()
                print(f"Closed {name}")

    def shutdown(self):
        self.server.close()

    def handle_client(self, client, role, destination):
        while True:
            streamData = client.recv(1024)
            if not streamData:
                break
            print(f"Received Data from: {client}, the data: {streamData}")
            
            # Assuming streamData contains pitch, roll, and yaw data
            pitch_data, roll_data, yaw_data = parse_stream_data(streamData)
            
            # Update belt vibration based on received data
            belt_controller.send_vibration_command(channel_index=0, pattern=yaw_data)

            # Forward the data to the destination client if needed
            destination.sendall(streamData)

    def parse_stream_data(self, streamData):
        # Placeholder function to parse stream data
        # Assumes data format: pitch_data|roll_data|yaw_data
        pitch_data, roll_data, yaw_data = streamData.split(b'|')
        return pitch_data, roll_data, yaw_data

if __name__ == "__main__":
    server = Server('127.0.0.1', 12345)
    server.start()
