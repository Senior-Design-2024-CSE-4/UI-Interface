import pybelt
import serial
import time
import threading
from xsens import*

from examples_utility import belt_controller_log_to_stdout, interactive_belt_connection
from pybelt.belt_controller import BeltController, BeltConnectionState, BeltControllerDelegate

def convert_reading(degrees):
  if degrees >= 0:
    return degrees
  else:
    return 360+degrees

yaw = xda.XsOutputConfiguration(xda.XDI_EulerAngles, MTi630_Settings_Orientation_Euler_SampleRate)[2]
belt_yaw = convert_reading(yaw)

def map_yaw(yaw, num_tactors):
    yaw = yaw % 360
    tactor_range = 360 / num_tactors
    for tactor_id in range(1, num_tactors + 1):
        lower = (tactor_id - 1) * tactor_range
        upper = tactor_id * tactor_range
        if lower <= yaw < upper
            return tactor_id
    return 0
num_tactors = 16

# initalize the belt

# vibrate each tactor in turning
bTestTactor_1 = 0
if bTestTactor_1 == 1:
    print('TACTOR TEST: Starting')
    for iDegrees in range(0, 360, 3):
        selected_tactor = map_yaw(iDegrees, num_tactors)
        belt_controller.send_vibration_command(selected_tactor, BeltVibrationPattern.CONTINUOUS, None,
                                              BeltOrientationType.ANGLE, iDegrees, 1, 250, 0, False, False)
        print('Tactor # = ', selected_tactor)
        time.sleep(1.0)
    print('TACTOR TEST: End')

# intensity
bTestTactor_3 = 0
if bTestTactor_3 == 1:
    print('### VARY THE INTENSITY OF TACTOR')
    # ramp up the intensity of vibration
    for iIntensity in range(0, 100, 1):
        selected_tactor = map_yaw(124, num_tactors)
        belt_controller.vibrate_at_angle(selected_tactor, intensity=iIntensity)
        print('Intensity # = ', iIntensity)
        time.sleep(0.1)
    # stop the vibration
    belt_controller.stop_vibration(None)  # None for all channels

# specific 
bTestTactor_4 = 0
if bTestTactor_4 == 1:
    print('### SENDING VIBRATION COMMAND')
    selected_tactor = map_yaw(0, num_tactors)
    belt_controller.send_vibration_command(
        channel_index=selected_tactor,
        pattern=BeltVibrationPattern.CONTINUOUS,
        intensity=None,
        orientation_type=BeltOrientationType.ANGLE,
        orientation=0,
        pattern_iterations=1,
        pattern_period=3000,
        pattern_start_time=0,
        exclusive_channel=False,
        clear_other_channels=False
    )
    time.sleep(5.75)
    belt_controller.stop_vibration()

# Additional time.sleep if needed
time.sleep(1.0)

