"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Justin Guilfoyle.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m2_laptop_code as m2
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Justin Guilfoyle")
    frame_label.grid(row=0, column=1)
    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    distance_label = ttk.Label(frame, text='Distance to travel in inches')
    distance_entry = ttk.Entry(frame, width=8)
    speed_label = ttk.Label(frame, text='Speed from 0 to 100')
    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.insert(0, "100")
    distance_entry.insert(0, '1')

    forward_button.grid(row=3, column=0)
    backward_button.grid(row=3, column=2)
    speed_label.grid(row=1, column=2)
    speed_entry.grid(row=2, column=2)
    distance_label.grid(row=1, column=0)
    distance_entry.grid(row=2, column=0)

    forward_button['command'] = lambda: forward(speed_entry.get(), distance_entry.get(), mqtt_sender)

    # Return your frame:
    return frame


def forward(speed, distance, mqtt_sender):
    print()
    print("Sending a message to the robot to", forward)
    print("  using speed:", speed)
    mqtt_sender.send_message("forward", [speed, distance])


class MyLaptopDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from the ROBOT via MQTT.
    """
    def __init__(self, root):
        self.root = root  # type: tkinter.Tk
        self.mqtt_sender = None  # type: mqtt.MqttClient

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    # TODO: Add methods here as needed.


# TODO: Add functions here as needed.
