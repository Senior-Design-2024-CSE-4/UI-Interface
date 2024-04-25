from vpython import*
from time import*
import json
import math



with open("imu_data.json", 'r') as f:
    data = json.load(f)
torso = box(pos=vec(0, 0, 0), length=3, width = 2, height = 6, color = color.cyan)
left_arm = box(pos=vec(-3, 3, 0), length=4, width = 1, height = 1, color=color.cyan)
right_arm = box(pos=vec(3, 3, 0), length=4, width = 1, height = 1, color=color.cyan)
head = sphere(pos=vec(0, 4, 0), radius=1, color=color.cyan)
body = compound([torso, left_arm, right_arm, head], pos = vec(0, 0, 0), axis = vec(1, 0, 0))

def rotate_pitch(pitch_val):
    body.rotate(axis=vec(1,0,0), angle = pitch_val, origin = vec(0,0,0))

def rotate_roll(roll_val):
    body.rotate(axis = vec(0, 0, 1), angle = roll_val, origin = vec(0, 0, 0))

def rotate_yaw(yaw_val):
    body.rotate(axis = vec(0, 1, 0), angle = yaw_val, origin = vec(0, 0, 0))



dt=0.1
omega=0.5
i=0
while True:
    rate(1)
    yaw = data[i]['yaw']
    pitch = data[i]['pitch']
    roll = data[i]['roll']
    rotate_yaw(yaw)
    rotate_pitch(pitch)
    rotate_roll(roll)
    i+=1
