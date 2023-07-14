import wpilib
import time
from commands2 import SubsystemBase
from wpilib.drive import DifferentialDrive
from wpilib import MotorControllerGroup, PWMSparkMax
import rev

class Drivetrain(SubsystemBase):
    def __init__(self):
        super().__init__()

        motor_type = rev.CANSparkMaxLowLevel.MotorType.kBrushless

        self.spark_neo_left_front = rev.CANSparkMax(constants.k_left_motor1_port, motor_type)
        self.spark_neo_left_back = rev.CANSparkMax(constants.k_left_motor2_port, motor_type)
        self.spark_neo_right_front = rev.CANSparkMax(constants.k_right_motor1_port, motor_type)
        self.spark_neo_right_back = rev.CANSparkMax(constants.k_right_motor2_port, motor_type)

        self.motors = [self.spark_neo_left_front,
                       self.spark_neo_left_back,
                       self.spark_neo_right_front,
                       self.spark_neo_right_back]

        self.spark_neo_left_PID = rev.CANSparkMax.getPIDController(self.spark_neo_left_front)
        self.spark_neo_right_PID = rev.CANSparkMax.getPIDController(self.spark_neo_right_front)

        self.left_motors = MotorControllerGroup(self.spark_neo_left_front, self.spark_neo_left_back)
        self.right_motors = MotorControllerGroup(self.spark_neo_right_front, self.spark_neo_right_back)

        self.diff_drive = DifferentialDrive(self.left_motors, self.right_motors)

    def steering_wheel_drive(self, fwd, rot):
        self.diff_drive.curvatureDrive(fwd, rot)

    def reset_encoders(self):
        for motor in self.motors:
            rev.CANSparkMax.getEncoder(motor).setPosition(0)
            time.sleep(0.025) # why do we do this?
            self.feed()