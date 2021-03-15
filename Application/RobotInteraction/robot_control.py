from pulserest.robot import Position
from pulserest import *
import cv2
import time


def FindInitPosition(ip, speed, x, y, z):  # переделать под поиск листика
    # robot = RobotPulse(ip)
    # search_position = Position(Point(x, y, z), Rotation(3.1415, 0, 0))  # фиксированная позиция сверху
    # camera = cv2.VideoCapture(0)
    # ret, frame = camera.read()

    frame = cv2.imread('D:\\test.jpg')  # check
    # cv2.imshow("test", frame)  # check

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh_frame = cv2.threshold(gray_frame, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = max(contours, key=cv2.contourArea)
    contours_frame = cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

    # contours = sorted(contours, reverse=True)  # check
    print(contours[0][0][0])  # check
    print(contours[0][0][1])  # check
    seed = (contours[0][0][0], contours[0][0][1])  # check
    cv2.circle(contours_frame, seed, 7, (0, 0, 255), cv2.FILLED, cv2.LINE_AA)  # check
    cv2.imshow("test2", contours_frame)  # check

    # ---OLD VARIANT---
    # robot = RobotPulse(ip)
    # init_position = Position(Point(x, y, z), Rotation(3.1415, 0, 0))
    # robot.set_position(init_position, speed)
    # robot.await_motion()


def Draw(ip, speed, x, y, z, clean_contours):
    time_start = time.time()
    robot = RobotPulse(ip)

    x_list = []  # тест
    y_list = []  # тест

    for i in range(1, len(clean_contours)):
        robot.run_positions([Position(Point(x + (clean_contours[i][0][0][0] * 0.0002),
                                            y + (clean_contours[i][0][0][1] * 0.0002),
                                            z),
                                      Rotation(3.1415, 0, 0))], speed, MT_JOINT)  # в начало контура, не опускаемся
        # --- ТЕСТ НИЖЕ ВМЕСТО ЭТОГО ЦИКЛА --- ТЕСТ НИЖЕ ВМЕСТО ЭТОГО ЦИКЛА --- ТЕСТ НИЖЕ ВМЕСТО ЭТОГО ЦИКЛА --- #
        # for j in range(len(clean_contours[i])):
        #     if j % 2 == 0:
        #         robot.run_positions([Position(Point(x + (clean_contours[i][j][0][0] * 0.0002),
        #                                             y + (clean_contours[i][j][0][1] * 0.0002),
        #                                             z - 0.105),
        #                                       Rotation(3.1415, 0, 0))], speed, MT_JOINT)

        # --- ТЕСТ --- ТЕСТ --- ТЕСТ --- ТЕСТ --- ТЕСТ --- ТЕСТ --- ТЕСТ --- ТЕСТ --- ТЕСТ --- ТЕСТ --- ТЕСТ --- #
        for j in range(len(clean_contours[i])):
            x_list.append(x + (clean_contours[i][j][0][0] * 0.0002))
            y_list.append(y + (clean_contours[i][j][0][1] * 0.0002))
        robot.run_positions([Position(Point(x_list,
                                            y_list,
                                            z - 0.105),
                                      Rotation(3.1415, 0, 0))], speed, MT_JOINT)
        x_list.clear()
        y_list.clear()
        # --- КОНЕЦ ТЕСТА --- КОНЕЦ ТЕСТА --- КОНЕЦ ТЕСТА --- КОНЕЦ ТЕСТА --- КОНЕЦ ТЕСТА --- КОНЕЦ ТЕСТА --- #

        robot.run_positions([Position(Point(x + (clean_contours[i][0][0][0] * 0.0002),
                                            y + (clean_contours[i][0][0][1] * 0.0002),
                                            z - 0.105),
                                      Rotation(3.1415, 0, 0)),  # возвращение в начальную точку текущего контура
                             Position(Point(x + (clean_contours[i][0][0][0] * 0.0002),
                                            y + (clean_contours[i][0][0][1] * 0.0002),
                                            z),
                                      Rotation(3.1415, 0, 0))], speed, MT_LINEAR)  # подъем для переход в след. контур
        robot.await_motion()
    init_position = Position(Point(x, y, z), Rotation(3.1415, 0, 0))
    robot.set_position(init_position, 10)
    robot.await_motion()
    time_finish = time.time()
    print("Time: " + time_finish - time_start)


def Hatch(ip, speed, clean_contours):
    pass


def Stop(ip):
    robot = RobotPulse(ip)
    robot.freeze()
