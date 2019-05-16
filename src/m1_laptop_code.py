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
    go_until_button = ttk.Button(frame, text='Go to object')
    distance_label = ttk.Label(frame, text='Distance to travel in inches')
    go_until_label = ttk.Label(frame, text='Distance wanted from closest object')
    plus_minus_label = ttk.Label(frame, text='Plus/minus on the distance to object')
    speed_label = ttk.Label(frame, text='Speed from 0 to 100')

    distance_entry = ttk.Entry(frame, width=8)
    speed_entry = ttk.Entry(frame, width=8)
    go_until_entry = ttk.Entry(frame, width=8)
    plus_minus_entry = ttk.Entry(frame, width=8)

    speed_entry.insert(0, "100")
    distance_entry.insert(0, '1')
    plus_minus_entry.insert(0, '1')
    go_until_entry.insert(0, '2')

    forward_button.grid(row=3, column=0)
    backward_button.grid(row=3, column=2)
    speed_label.grid(row=1, column=2)
    speed_entry.grid(row=2, column=2)
    distance_label.grid(row=1, column=0)
    distance_entry.grid(row=2, column=0)
    go_until_label.grid(row=4, column=0)
    go_until_entry.grid(row=5, column=0)
    go_until_button.grid(row=6, column=1)
    plus_minus_label.grid(row=4, column=2)
    plus_minus_entry.grid(row=5, column=2)

    forward_button['command'] = lambda: forward(int(speed_entry.get()), int(distance_entry.get()), mqtt_sender)
    backward_button['command'] = lambda: backward(int(speed_entry.get()), int(distance_entry.get()), mqtt_sender)
    go_until_button['command'] = lambda: go_until(int(plus_minus_entry.get()), int(go_until_entry.get()), int(speed_entry.get()), mqtt_sender)

    # Return your frame:
    return frame


def forward(speed, distance, mqtt_sender):
    print()
    print("Sending a message to the robot to", forward)
    print("  using speed:", speed)
    mqtt_sender.send_message("forward", [speed, distance])

def backward(speed, distance, mqtt_sender):
    print()
    print('Sending a message to the robot to', backward)
    print('  using speed:', speed)
    mqtt_sender.send_message('backward', [speed, distance])

def go_until(x, delta, speed, mqtt_sender):
    print()
    print('Sending a message to the robot to', go_until)
    print(' using speed:', speed)
    mqtt_sender.send_message('go_until', [x, delta, speed])


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
