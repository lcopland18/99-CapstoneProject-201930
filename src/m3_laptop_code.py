"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Ruth Hammond.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.:))

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m2_laptop_code as m2


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Ruth Hammond")
    frame_label.grid()
    # TODO 2: Put your name in the above.

    armspeed_button = ttk.Button(frame, text="Arm Speed:")
    armspeed_button.grid(row = 1, column = 0 )
    armspeed_entry = ttk.Entry(frame, width=8)
    armspeed_entry.insert(0, "100")
    armspeed_entry.grid(row = 1, column = 1)

    armto_button = ttk.Button(frame, text="Arm To:")
    armto_button.grid(row = 2, column = 0)
    armto_entry = ttk.Entry(frame,width = 8)
    armto_entry.insert(0, "100")
    armto_entry.grid(row=2, column=1)

    armcalibrate_button = ttk.Button(frame, text="Calibrate Arm")
    armcalibrate_button.grid(row = 5)


    armup_button = ttk.Button(frame, text="Arm Up")
    armup_button.grid(row = 3, column = 0 )

    armdown_button = ttk.Button(frame, text="Arm Down")
    armdown_button.grid(row =3,column = 1 )

    armto_button["command"] = lambda: handle_arm_up(
        armspeed_entry, mqtt_sender)



    #armup_button["command"] = lambda: arm_up(mqtt_sender)
    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).

    # Return your frame:
    return frame


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
    def handle_arm_up(armspeed_entry,mqtt_sender):
        print('Arm Up:', armspeed_entry)
        mqtt_sender.send_message("Arm_Up", [armspeed_entry.get()])



# TODO: Add functions here as needed.
