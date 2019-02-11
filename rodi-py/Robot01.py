import rodi
import time

robot = rodi.RoDI()

for i in range(4):
    robot.move_forward()
    time.sleep(2)
    robot.move_right()
    time.sleep(0.5)
robot.move_stop()
print("Cuadrado")

while True:
    print (robot.see())
    time.sleep(0.1)

while True:
    distance = robot.see()
    if distance > 10:
        robot.move_forward()
    else:
        robot.move_left()
    time.sleep(0.1)

while True:
    linea = robot.sense()
    print(linea[0])
    print(linea[1])
    time.sleep(3)

    if linea[0]>=100 and linea[1]>=100:
        robot.move_forward(30,-30)
    elif linea[0]<=90 and linea[1]<=90:
        robot.move_right(30,-30)
    else:
        robot.move_left(-20,20)