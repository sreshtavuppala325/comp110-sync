"""Self-driving robotic race car controller demo."""

from racing import RobotCommand, RobotSensors

RACING_NAME: str = "Crash Dummy"
RACING_COLOR: str = "#FEDD00"


def control(sensors: RobotSensors) -> RobotCommand:
    """Minimally viable self-driving controller"""
    return RobotCommand(throttle=1.0, steer=0.0)
