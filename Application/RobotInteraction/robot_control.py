from pulserest.robot import Position
from pulserest import *
import time


class RobotControl:
    def MoveToInitPosition(self, ip, speed, x, y, z):  # переделать под поиск листика
        robot = RobotPulse(ip)
        init_position = Position(Point(x, y, z), Rotation(3.1415, 0, 0))
        robot.set_position(init_position, speed)
        robot.await_motion()

    def Draw(self, ip, speed, x, y, z, clean_contours, scale_percent):
        time_start = time.time()
        robot = RobotPulse(ip)

        x_list = []  # тест
        y_list = []  # тест
        point_list = []  # тест

        for i in range(1, len(clean_contours)):
            robot.run_positions([Position(Point(x + (clean_contours[i][0][0][0] * 0.0002 * scale_percent),
                                                y + (clean_contours[i][0][0][1] * 0.0002 * scale_percent),
                                                z),
                                          Rotation(3.1415, 0, 0))], speed, MT_JOINT)  # в начало контура, не опускаемся

            # # # --- ПЕРВЫЙ ВАРИАНТ РИСОВАНИЯ, ПОДАЧА РОБОТУ ПО ОДНОЙ ТОЧКЕ --- # # #
            # for j in range(len(clean_contours[i])):
            #     if j % 2 == 0:
            #         robot.run_positions([Position(Point(x + (clean_contours[i][j][0][0] * 0.0002),
            #                                             y + (clean_contours[i][j][0][1] * 0.0002),
            #                                             z - 0.105),
            #                                       Rotation(3.1415, 0, 0))], speed, MT_JOINT)

            # # # --- ТЕСТОВЫЙ ВАРИАНТ РИСОВАНИЯ №1, ПОДАЧА РОБОТУ ЦЕЛЫХ МАССИВОВ ТОЧЕК --- # # #
            # for j in range(len(clean_contours[i])):
            #     x_list.append(x + (clean_contours[i][j][0][0] * 0.0002))
            #     y_list.append(y + (clean_contours[i][j][0][1] * 0.0002))
            # robot.run_positions([Position(Point(x_list,  # [list[Position]]
            #                                     y_list,
            #                                     z - 0.105),
            #                               Rotation(3.1415, 0, 0))], speed, MT_JOINT)
            # x_list.clear()
            # y_list.clear()

            # # # --- ТЕСТОВЫЙ ВАРИАНТ РИСОВАНИЯ №2, ПОДАЧА РОБОТУ ЦЕЛЫХ МАССИВОВ ТОЧЕК --- # # #
            for j in range(len(clean_contours[i])):
                point_list.append([Position(Point(x + (clean_contours[i][j][0][0] * 0.0002 * scale_percent),
                                                  y + (clean_contours[i][j][0][1] * 0.0002 * scale_percent),
                                                  z - 0.105),
                                            Rotation(3.1415, 0, 0))])
            robot.run_positions(point_list, speed, MT_JOINT)
            # print(len(point_list))
            point_list.clear()
            # # # --------------------------------------------------------------------- # # #

            robot.run_positions([Position(Point(x + (clean_contours[i][0][0][0] * 0.0002 * scale_percent),
                                                y + (clean_contours[i][0][0][1] * 0.0002 * scale_percent),
                                                z - 0.105),
                                          Rotation(3.1415, 0, 0)),  # возвращение в начальную точку текущего контура
                                 Position(Point(x + (clean_contours[i][0][0][0] * 0.0002 * scale_percent),
                                                y + (clean_contours[i][0][0][1] * 0.0002 * scale_percent),
                                                z),
                                          Rotation(3.1415, 0, 0))], speed, MT_LINEAR)  # подъем для переход в след. контур
            robot.await_motion()
        init_position = Position(Point(x, y, z), Rotation(3.1415, 0, 0))
        robot.set_position(init_position, 10)
        robot.await_motion()
        time_finish = time.time()
        print("Time: " + time_finish - time_start)

    def Stop(self, ip):
        robot = RobotPulse(ip)
        robot.freeze()
