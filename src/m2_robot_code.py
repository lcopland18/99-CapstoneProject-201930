"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Lauren Copland.
  Spring term, 2018-2019.
"""
# DONE 1:  Put your name in the above.
import math
import mqtt_remote_method_calls as mqtt
import rosebot
import m2_robot_code as m2
import m3_robot_code as m3



class MyRobotDelegate(object):
    """
    Defines methods that are called by the MQTT listener when that listener
    gets a message (name of the method, plus its arguments)
    from a LAPTOP via MQTT.
    """
    def __init__(self, robot):
        self.robot = robot  # type: rosebot.RoseBot
        self.mqtt_sender = None  # type: mqtt.MqttClient
        self.is_time_to_quit = False  # Set this to True to exit the robot code

    def set_mqtt_sender(self, mqtt_sender):
        self.mqtt_sender = mqtt_sender

    def stop(self):
        """ Tells the robot to stop moving. """
        print_message_received("stop")
        self.robot.drive_system.stop()

    # DONE: Add methods here as needed.

    # def spin(self,left_speed,right_speed,degrees):
    #     print("Spin message received:",left_speed,right_speed,degrees)
    #     self.robot.drive_system.go(left_speed,right_speed)

    def spin_left(self,left_speed,right_speed,degrees):
        print("Spin Left Received",left_speed,right_speed,degrees)
        distance = degrees * 5.0 #CHANGE CONSTANT
        self.robot.drive_system.right_motor.reset_position()
        self.robot.drive_system.go(left_speed,right_speed)
        while True:
            if abs(self.robot.drive_system.right_motor.get_position()) >= distance:
                self.robot.drive_system.stop()
                break

    def spin_right(self,left_speed,right_speed,degrees):
        print("Spin Right Received",left_speed,right_speed,degrees)
        distance = degrees * 5.0 #CHANGE CONSTANT
        self.robot.drive_system.left_motor.reset_position()
        self.robot.drive_system.go(left_speed,right_speed)
        while True:
            if abs(self.robot.drive_system.left_motor.get_position()) >= distance:
                self.robot.drive_system.stop()
                break

    def spin_until_facing(self,signature,x,delta,speed):
        print("Spin Until Facing Received")
        big_enough = 1500
        signature = "SIG" + str(signature)
        self.robot.sensor_system.camera.set_signature(signature)
        while True: #RETURN BLOB VALUES
            blob = self.robot.sensor_system.camera.get_biggest_blob()
            print("While",signature,x,delta,blob,big_enough,blob.get_area())
            if x - blob.center.x <= delta and blob.get_area()>big_enough:
                self.robot.drive_system.stop()
                print("Broken",blob.get_area(),big_enough)
                break
            self.spin_right(speed, -speed, 1)  # SPIN CLOCKWISE



def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.

