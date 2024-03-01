import pybelt
import serial
import time
import threading

from examples_utility import belt_controller_log_to_stdout, interactive_belt_connection
from pybelt.belt_controller import BeltController, BeltConnectionState, BeltControllerDelegate


tactor_mapping = [
    {"tactor_id": 1, "yaw_range": (0, 45)},
    {"tactor_id": 2, "yaw_range": (45, 90)},
    {"tactor_id": 3, "yaw_range": (90, 135)},
    {"tactor_id": 4, "yaw_range": (135, 180)},
    {"tactor_id": 5, "yaw_range": (180, 225)},
    {"tactor_id": 6, "yaw_range": (225, 270)},
    {"tactor_id": 7, "yaw_range": (270, 315)},
    {"tactor_id": 8, "yaw_range": (315, 360)},
]

def map_yaw(yaw):
  yaw = yaw % 360 # to be within the range of (0, 360)
  # find tactor whose range contains the yaw value
  for map in tactor_mapping:
    if mapping["yaw_range"][0] <= yaw < mapping["yaw_range"][1]:
      return mapping["tactor_id"]
  return 0

