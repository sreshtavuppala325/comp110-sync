"""Self-driving robotic race car controller demo."""

from racing import RobotCommand, RobotSensors

__author__: str = "730995916"
RACING_NAME: str = "Level 0"
RACING_COLOR: str = "#FE0072"


def control(sensors: RobotSensors) -> RobotCommand:
    """Minimally viable self-driving controller"""
    throttle: float = 0.1
    steer: float = 0.0
    if sensors.wall_lidar.front_left_m < 4.0:
        steer: float = 1.0

    else:
        if sensors.wall_lidar.front_right_m < 4.0:
            steer = -1.0
        else:
            steer = 0.0

    return RobotCommand(throttle=throttle, steer=steer)
