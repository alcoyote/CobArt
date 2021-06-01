from pulseapi import *


class RobotControl:
    def MoveToInitPosition(self, ip, speed, x, y, z):
        robot = RobotPulse(ip)
        init_position = position([x, y, z], [3.1415, 0, 0])
        robot.set_position(init_position, speed)
        robot.await_motion()

    def Draw(self, ip, speed, x, y, z, clean_contours, scale_percent):
        robot = RobotPulse(ip)
        positions_list = []

        for i in range(1, len(clean_contours)):
            # Up beginning of the contour
            x_temp = x + (clean_contours[i][0][0][0] * 0.0002 * scale_percent)
            y_temp = y + (clean_contours[i][0][0][1] * 0.0002 * scale_percent)
            z_temp = z
            zero_point = position([x_temp, y_temp, z_temp], [3.1415, 0, 0])
            robot.set_position(zero_point, speed, motion_type=MT_JOINT)

            # Creating a list of contours points and drawing
            for j in range(len(clean_contours[i])):
                x_temp = x + (clean_contours[i][j][0][0] * 0.0002 * scale_percent)
                y_temp = y + (clean_contours[i][j][0][1] * 0.0002 * scale_percent)
                z_temp = z-0.175
                positions_list.append(position([x_temp, y_temp, z_temp], [3.1415, 0, 0]))
            robot.run_positions(positions_list, speed, motion_type=MT_JOINT)
            positions_list.clear()

            # Returning to the first point of the current contour
            x_temp = x + (clean_contours[i][0][0][0] * 0.0002 * scale_percent)
            y_temp = y + (clean_contours[i][0][0][1] * 0.0002 * scale_percent)
            z_temp = z-0.175
            contour_last_point = position([x_temp, y_temp, z_temp], [3.1415, 0, 0])
            robot.set_position(contour_last_point, speed, motion_type=MT_JOINT)

            # Up for moving to the next contour
            x_temp = x + (clean_contours[i][0][0][0] * 0.0002 * scale_percent)
            y_temp = y + (clean_contours[i][0][0][1] * 0.0002 * scale_percent)
            z_temp = z
            up_point = position([x_temp, y_temp, z_temp], [3.1415, 0, 0])
            robot.set_position(up_point, speed, motion_type=MT_LINEAR)

            robot.await_motion()
        init_position = position([x, y, z], [3.1415, 0, 0])
        robot.set_position(init_position, speed)
        robot.await_motion()

    def Stop(self, ip):
        robot = RobotPulse(ip)
        robot.freeze()
