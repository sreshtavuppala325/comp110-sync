"""Self-driving robotic race car controller demo."""

from racing import RobotCommand, RobotSensors

__author__: str = "730995916"
RACING_NAME: str = "Level 1"
RACING_COLOR: str = "#53F2EF"


def control(sensors: RobotSensors) -> RobotCommand:
    """Programming challanger to beat level 0"""
    throttle: float = 1.0
    steer: float = 0.0

    if sensors.wall_lidar.front_left_m < 7.0:
        steer = 1.0

    else:
        if sensors.wall_lidar.front_right_m < 9.0:
            steer = -1.0
        else:
            steer = 0.0

    if sensors.odometry.speed_mps > 20.0:
        throttle = -0.4

    return RobotCommand(throttle=throttle, steer=steer)
