import json
import random
import math

json_file = "imu_data.json"
def generate_data(n):
    data=[]
    for i in range(n):
        yaw = random.uniform(-math.pi, math.pi)
        pitch = random.uniform(-math.pi, math.pi)
        roll = random.uniform(-math.pi, math.pi)
        signal_list = []
        for j in range(16):
            r = random.choice([0,1])
            signal_list.append(r)

        dictionary = {
            "yaw": yaw,
            "pitch": pitch,
            "roll": roll,
            "signal_list": signal_list
        }
        data.append(dictionary)
    with open("imu_data.json", 'a') as file:
        json.dump(data, file, indent = 4, separators = (',', ':'))

generate_data(100)
