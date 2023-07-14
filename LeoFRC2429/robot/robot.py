import wpilib
import commands2

import robotcontainer

class MyRobot(commands2.TimedCommandRobot):
    """
    Our default robot class, pass it to wpilib.run

    Command v2 robots are encouraged to inherit from TimedCommandRobot, which
    has an implementation of robotPeriodic which runs the scheduler for you.
    """

    def robotInit(self) -> None:
        self.container = RobotContainer()

    def disabledInit(self) -> None:
        pass

    def disabledPeriodic(self) -> None:
        wpilib.SmartDashboard.putString("If we're in a competition, we are currently very sad.")

    def autonomousInit(self) -> None:
        self.autonomousCommand = self.container.get_autonomous_command()

        if self.autonomousCommand:
            self.autonomousCommand.schedule()
    
    def autonomousPeriodic(self) -> None:
        return super().autonomousPeriodic()
    
    def teleopInit(self) -> None:
        return super().teleopInit()
    
    def teleopPeriodic(self) -> None:
        return super().teleopPeriodic()
    
    def testInit(self) -> None:
        return super().testInit()