"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Ruth Hammond.
  Spring term, 2018-2019.
"""
# TODO 1:  Put your name in the above.

import mqtt_remote_method_calls as mqtt
import rosebot
import m1_robot_code as m1
import m2_robot_code as m2


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

    # TODO: Add methods here as needed.
    def arm_up(self, speed):
        print("Robot recieved Arm Up")
        real_speed = int(speed)
        while True:
            self.robot.arm_and_claw.motor.turn_on(real_speed)
            if (self.robot.arm_and_claw.touch_sensor.is_pressed() is True):
                break
        self.robot.arm_and_claw.motor.turn_off()

    def move_arm_to_position(self,speed,position):
        print("Robot recieved Arm To")
        real_speed = speed
        if position < self.robot.arm_and_claw.motor.get_position():
            self.robot.arm_and_claw.motor.turn_on(-real_speed)
            while True:
                if self.robot.arm_and_claw.motor.get_position() == position:
                    self.robot.arm_and_claw.motor.turn_off()
                    break
        if position > self.robot.arm_and_claw.motor.get_position():
            self.robot.arm_and_claw.motor.turn_on(real_speed)
            while True:
                if self.robot.arm_and_claw.motor.get_position() == position:
                    self.robot.arm_and_claw.motor.turn_off()
                    break

    def calibrate(self):
        print("Calibrate")
        self.robot.arm_and_claw.motor.reset_position()

    def arm_down(self,speed):
        print("Robot recieved Arm Down")
        real_speed = -int(speed)
        while True:
            self.robot.arm_and_claw.motor.turn_on(real_speed)
            if self.robot.arm_and_claw.motor.get_position()==0:
                break
        self.robot.arm_and_claw.motor.turn_off()

  #  def goes_until_sees_color(self,speed,color):
        self.robot.drive_system.go(speed, speed)
        while True:
            if self.sensor_system:
                self.robot.drive_system.stop()
                break
            if self.robot.drive_system.right_motor.get_position() >= len_deg:
                self.robot.drive_system.stop()
                break


def print_message_received(method_name, arguments=None):
    print()
    print("The robot's delegate has received a message")
    print("for the  ", method_name, "  method, with arguments", arguments)


# TODO: Add functions here as needed.

