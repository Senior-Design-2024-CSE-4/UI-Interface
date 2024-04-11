#! /usr/bin/env python
# encoding: utf-8
import time
from datetime import datetime
from datetime import timedelta
from threading import Event, Lock

from pybelt.examples_utility import belt_controller_log_to_stdout, interactive_belt_connection
from pybelt.belt_controller import *

from test_client import Client
# Event to stop the script
button_pressed_event = Event()

# Belt orientation
orientation_lock = Lock()  # Lock to read and write the heading and period (only necessary for BLE interface)
belt_heading: int = -1  # Last known belt heading value
belt_orientation_update_period = timedelta()  # Period between the last two orientation updates


class Delegate(BeltControllerDelegate):

    def __init__(self):
        # __init__ is only used for the orientation notification period
        self._last_orientation_update_time = datetime.now()  # Time of the last heading update

    def on_belt_orientation_notified(self, heading, is_orientation_accurate, extra):
        global belt_heading
        global belt_orientation_update_period
        with orientation_lock:
            belt_heading = heading
            # Below code is only for measuring notification period
            now = datetime.now()
            belt_orientation_update_period = now - self._last_orientation_update_time
            self._last_orientation_update_time = now

    def on_belt_button_pressed(self, button_id, previous_mode, new_mode):
        button_pressed_event.set()


def main():
    belt_controller_log_to_stdout()

    # Interactive script to connect the belt
    belt_controller_delegate = Delegate()
    belt_controller = BeltController(belt_controller_delegate)
    interactive_belt_connection(belt_controller)
    if belt_controller.get_connection_state() != BeltConnectionState.CONNECTED:
        print("Connection failed.")
        return 0

    # Change orientation notification period
    belt_controller.set_orientation_notifications(True)

    client = Client('127.0.0.1', 12345)
    # client.connect('xsens', 'l')
    client.connect('ubelt', 'l')
    time.sleep(5)

    print("Press a button on the belt to quit.")
    while belt_controller.get_connection_state() == BeltConnectionState.CONNECTED and not button_pressed_event.is_set():
        # Delay for terminal display (not necessary if other processing)
        # heading = float(client.listen_to_server())
        
        temp = client.listen_to_server()   
        print(temp)

        if temp == '':
            heading = -1
        else:
            rcv = temp.split(',')
            a = int(rcv[0])
            b = int(rcv[1])
            heading = float(rcv[2])
            intensity = int(rcv[3])
        # print(a, b, heading, intensity)
        time.sleep(0.005)
        # # Retrieve orientation with lock
        with orientation_lock:
            heading = heading
            notification_period = belt_orientation_update_period.total_seconds()
        # Process orientation
        belt_controller.send_pulse_command(
                    channel_index=0,
                    orientation_type=BeltOrientationType.ANGLE,
                    orientation=int(heading)-360,
                    intensity=intensity,
                    on_duration_ms=150,
                    pulse_period=500,
                    pulse_iterations=3,
                    series_period=1500,
                    series_iterations=1,
                    timer_option=BeltVibrationTimerOption.RESET_TIMER,
                    exclusive_channel=False,
                    clear_other_channels=False
                )
        # print("\rBelt heading: {}°\t (period: {:.3f}s)            ".format(heading, notification_period), end="")

    belt_controller.set_orientation_notifications(False)
    belt_controller.disconnect_belt()
    return 0


if __name__ == "__main__":
    main()