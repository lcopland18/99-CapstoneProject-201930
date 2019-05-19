"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Lauren Copland.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.


import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as mqtt
import m1_laptop_code as m1
import m3_laptop_code as m3


def get_my_frame(root, window, mqtt_sender):
    # Construct your frame:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame_label = ttk.Label(frame, text="Lauren Copland")
    frame_label.grid(column = 1, row = 0)

    spin_frame = ttk.Frame(frame, padding = 10, borderwidth = 5, relief = "ridge")
    search_frame = ttk.Frame(frame,padding = 10, borderwidth = 5, relief = "ridge")

    spin_label = ttk.Label(frame,text = "Spin Buttons")
    search_label = ttk.Label(frame, text = "Search Buttons")

    # DONE 2: Put your name in the above.

    # Add the rest of your GUI to your frame:
    # TODO: Put your GUI onto your frame (using sub-frames if you wish).

    #Buttons and Entry Boxes
    spin_left_button = ttk.Button(spin_frame,text = "Spin Left" )
    spin_right_button = ttk.Button(spin_frame,text = "Spin Right")
    spin_until_facing_button = ttk.Button(search_frame,text = "Search for Object")

    spin_left_right_entry = ttk.Entry(spin_frame,width = 8)
    spin_left_right_label = ttk.Label(spin_frame, text = "Spin 0° to 360°")
    spin_left_right_entry.insert(0,'180')
    spin_speed_entry = ttk.Entry(spin_frame,width = 8)
    spin_speed_label = ttk.Label(spin_frame,text = "Spin Speed 0 to 100")
    spin_speed_entry.insert(0,'100')

    SUF_signature_entry = ttk.Entry(search_frame,width = 8)
    SUF_signature_entry.insert(0,'1')
    SUF_signature_label = ttk.Label(search_frame,text = "Enter Color Signature")

    SUF_X_entry = ttk.Entry(search_frame,width = 8)
    SUF_X_entry.insert(0,'150')
    SUF_X_label = ttk.Label(search_frame, text = "Block location on screen 0 to 299")

    SUF_delta_entry = ttk.Entry(search_frame,width = 8)
    SUF_delta_entry.insert(0,'10')
    SUF_delta_label = ttk.Label(search_frame, text = "x coordinate +/- value")

    SUF_speed_entry = ttk.Entry(search_frame,width = 8)
    SUF_speed_entry.insert(0,'50')
    SUF_speed_label = ttk.Label(search_frame,text = "Spin Speed 0 to 100")

    #Grid
    spin_left_button.grid(column =0, row = 3)
    spin_right_button.grid(column = 2, row = 3)

    spin_left_right_label.grid(column = 1, row = 2)
    spin_left_right_entry.grid(column = 1, row = 3)

    spin_speed_entry.grid(column = 1 , row =  5)
    spin_speed_label.grid(column = 1, row = 4 )

    spin_frame.grid(column = 0,row = 1)
    search_frame.grid(column = 2, row = 1)
    spin_label.grid(column = 0, row = 0)
    search_label.grid(column = 2, row = 0)


    spin_until_facing_button.grid(column = 0, row = 8)

    SUF_signature_label.grid(column = 0,row = 0)
    SUF_delta_label.grid(column = 0, row = 2)
    SUF_X_label.grid(column = 0, row = 4)
    SUF_speed_label.grid(column =0, row = 6)
    SUF_signature_entry.grid(column =0, row = 1)
    SUF_delta_entry.grid(column = 0, row =3)
    SUF_X_entry.grid(column = 0, row =5 )
    SUF_speed_entry.grid(column =0, row = 7)


    #Lambda Functions
    spin_left_button['command'] = lambda: handle_spin_left(spin_speed_entry,spin_left_right_entry,mqtt_sender)
    spin_right_button['command'] = lambda: handle_spin_right(spin_speed_entry,spin_left_right_entry,mqtt_sender)
    spin_until_facing_button['command'] = lambda: handle_spin_until_facing(SUF_signature_entry, SUF_X_entry, SUF_delta_entry, SUF_speed_entry,mqtt_sender)


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


# TODO: Add functions here as needed.

# def spin(mqtt_sender,left_speed,right_speed,degrees):
#     print("Sending message to the robot to spin at speed:",left_speed,right_speed)
#     print("Sending message to the robot to spin:",degrees,"degrees")
#     mqtt_sender.send_message("spin",[left_speed,right_speed,degrees])



def handle_spin_left(spin_speed_entry,spin_distance_deg,mqtt_sender):
    print('Spin Left Message:', spin_speed_entry.get(),spin_distance_deg.get())
    speed = int(spin_speed_entry.get())
    distance = int(spin_distance_deg.get())
    mqtt_sender.send_message('spin_left',[speed,-speed,distance])

def handle_spin_right(spin_speed_entry,spin_distance_deg,mqtt_sender):
    print('Spin Right Message:', spin_speed_entry.get(),spin_distance_deg.get())
    speed = int(spin_speed_entry.get())
    distance = int(spin_distance_deg.get())
    mqtt_sender.send_message('spin_right',[-speed,speed,distance])

def handle_spin_until_facing(signature, x, delta, speed, mqtt_sender):
    print('Spin Search Message:')
    signature = int(signature.get())
    x = int(x.get())
    delta = int(delta.get())
    speed = int(speed.get())
    mqtt_sender.send_message('spin_until_facing',[signature,x,delta,speed])