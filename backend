import socket
from threading import Thread
import numpy as np
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
            
            # Assume streamData contains pitch, roll, and yaw data
            pitch_data, roll_data, yaw_data = parse_stream_data(streamData)
            process_and_update_belt(pitch_data, roll_data, yaw_data)

            # Forward the data to the destination client if needed
            destination.sendall(streamData)

    def parse_stream_data(self, streamData):
        # Placeholder function to parse stream data
        # Assumes data format: pitch_data|roll_data|yaw_data
        pitch_data, roll_data, yaw_data = streamData.split(b'|')
        pitch_data = np.frombuffer(pitch_data, dtype=np.float64)
        roll_data = np.frombuffer(roll_data, dtype=np.float64)
        yaw_data = np.frombuffer(yaw_data, dtype=np.float64)
        return pitch_data, roll_data, yaw_data

    def process_and_update_belt(self, pitch_data, roll_data, yaw_data):
        # Placeholder function to process sensor data and update belt vibration
        # Perform data processing/manipulation here
        # Example: calculate vibration intensity and pattern based on sensor data
        intensity = calculate_intensity(pitch_data, roll_data)
        pattern = calculate_pattern(yaw_data)
        
        # Update belt vibration
        belt_controller.send_vibration_command(channel_index=0, pattern=pattern, intensity=intensity)

    def calculate_intensity(self, pitch_data, roll_data):
        # Placeholder function to calculate vibration intensity based on pitch and roll data
        # Modify this according to your specific requirements
        intensity = np.linalg.norm(pitch_data) + np.linalg.norm(roll_data)
        return intensity

    def calculate_pattern(self, yaw_data):
        # Placeholder function to calculate vibration pattern based on yaw data
        # Modify this according to your specific requirements
        # Here we assume a simple mapping of yaw to pattern
        if np.mean(yaw_data) < 90:
            return "CONTINUOUS"
        elif np.mean(yaw_data) < 180:
            return "PULSING"
        elif np.mean(yaw_data) < 270:
            return "DOUBLE_PULSING"
        else:
            return "CONTINUOUS"

if __name__ == "__main__":
    server = Server('127.0.0.1', 12345)
    server.start()
