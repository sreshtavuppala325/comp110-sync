"""Self-driving robotic race car controller demo."""

from racing import RobotCommand, RobotSensors

__author__: str = "730995916"

RACING_NAME: str = "Level 3"
RACING_COLOR: str = "#53F2EF"


def control(sensors: RobotSensors) -> RobotCommand:
    """"Steer using immediate offset/heading plus a lookahead point to anticipate curves."""
    throttle: float = 1.0
    offset_center: float = sensors.camera.center_offset_m
    heading_error: float = sensors.camera.heading_error_degrees
    lookahead: float = sensors.camera.lookahead_offsets_m [-1]

    position: float = -offset_center/2.0
    heading: float = -heading_error/30.0
    lookahead: float = -lookahead/6.0
    steer: float = position + heading +lookahead

    
    if steer>1.0:
        steer = -1.0
    elif steer < -1.0:
        steer = 1.0
    

    speed_mps: float = sensors.odometry.speed_mps
    target_speed: float = 40.0 
    if abs(lookahead)>3.0:
        target_speed = 17.0  

    throttle: float = (target_speed - speed_mps) / target_speed
    if throttle > 1.0:
        throttle = 1.0
    elif throttle < -1.0:
        throttle = -1.0
    
    return RobotCommand(throttle=throttle, steer=steer)
