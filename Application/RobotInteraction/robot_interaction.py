from RobotInteraction.robot_control import RobotControl
from RobotInteraction.contours import Contours


class RobotInteraction:
    def __init__(self):
        self.contours = Contours()
        self.robot_control = RobotControl()
