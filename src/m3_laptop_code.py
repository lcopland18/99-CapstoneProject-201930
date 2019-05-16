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
    frame_label.grid(row =0,column=1)
    # TODO 2: Put your name in the above.

    armspeed_button = ttk.Label(frame, text="Arm Speed:")
    armspeed_button.grid(row = 1, column = 0 )
    armspeed_entry = ttk.Entry(frame, width=8)
    armspeed_entry.insert(0, "100")
    armspeed_entry.grid(row = 2, column = 0)

    armto_button = ttk.Button(frame, text="Go To Position")
    armto_button.grid(row = 1, column = 2)
    position_label = ttk.Label(frame, text="Position:")
    position_label.grid(row=3, column = 0)
    armto_entry = ttk.Entry(frame,width = 8)
    armto_entry.insert(0, "100")
    armto_entry.grid(row=4, column=0)
    armto_button["command"] = lambda: handle_move_arm_to_position(armspeed_entry,armto_entry,mqtt_sender)

    armcalibrate_button = ttk.Button(frame, text="Calibrate Arm")
    armcalibrate_button.grid(row = 4,column = 2)
    armcalibrate_button["command"] = lambda: handle_calibrate(mqtt_sender)

    armup_button = ttk.Button(frame, text="Arm Up")
    armup_button.grid(row = 2, column = 2)
    armup_button["command"] = lambda: handle_arm_up(armspeed_entry,mqtt_sender)

    armdown_button = ttk.Button(frame, text="Arm Down")
    armdown_button.grid(row =3,column = 2 )
    armdown_button["command"] = lambda: handle_arm_down(armspeed_entry,mqtt_sender)






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
    speed = int(armspeed_entry.get())
    print()
    print("Moving Arm Up at Speed: ")
    print('At Speed:', speed)
    mqtt_sender.send_message("arm_up", [speed])

def handle_move_arm_to_position(armspeed_entry,armto_entry,mqtt_sender):
    speed = int(armspeed_entry.get())
    position = int(armto_entry.get())
    print()
    print("Moving to Postion: ",position)
    print('At Speed: ',speed)
    mqtt_sender.send_message("move_arm_to_position", [speed, position])

def handle_calibrate(mqtt_sender):
    print()
    print("Calibrating...")
    mqtt_sender.send_message("calibrate",[])

def handle_arm_down(armspeed_entry, mqtt_sender):
    speed = int(armspeed_entry.get())
    print()
    print("Moving Arm Down")
    print('At Speed: ',speed)
    mqtt_sender.send_message("arm_down",[speed])

# TODO: Add functions here as needed.
