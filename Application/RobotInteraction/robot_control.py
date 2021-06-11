from pulseapi import *


class RobotControl:
    def MoveToInitPosition(self, ip, speed, x, y, z):
        robot = RobotPulse(ip)
        init_position = position([x, y, z], [3.1415, 0, 0])
        robot.set_position(init_position, speed)
        robot.await_motion()

    def Draw(self, ip, speed, x, y, z, clean_contours, scale_percent):
        robot = RobotPulse(ip)
        contour_points_list = []

        for i in range(1, len(clean_contours)):
            # Up first point
            x_temp = x + (clean_contours[i][0][0][0] * 0.0002 * scale_percent)
            y_temp = y + (clean_contours[i][0][0][1] * 0.0002 * scale_percent)
            z_temp = z
            up_first_point = position([x_temp, y_temp, z_temp], [3.1415, 0, 0])
            robot.set_position(up_first_point, speed, motion_type=MT_LINEAR)

            # Draw contour
            for j in range(len(clean_contours[i])):
                x_temp = x + (clean_contours[i][j][0][0] * 0.0002 * scale_percent)
                y_temp = y + (clean_contours[i][j][0][1] * 0.0002 * scale_percent)
                z_temp = z-0.022
                contour_points_list.append(position([x_temp, y_temp, z_temp], [3.1415, 0, 0]))
            robot.run_positions(contour_points_list, speed, motion_type=MT_LINEAR)
            contour_points_list.clear()

            # Up last point
            x_temp = x + (clean_contours[i][0][0][0] * 0.0002 * scale_percent)
            y_temp = y + (clean_contours[i][0][0][1] * 0.0002 * scale_percent)
            z_temp = z
            up_last_point = position([x_temp, y_temp, z_temp], [3.1415, 0, 0])
            robot.set_position(up_last_point, speed, motion_type=MT_LINEAR)
            robot.await_motion()

        init_position = position([x, y, z], [3.1415, 0, 0])
        robot.set_position(init_position, speed)
        robot.await_motion()

    def Stop(self, ip):
        robot = RobotPulse(ip)
        robot.freeze()
