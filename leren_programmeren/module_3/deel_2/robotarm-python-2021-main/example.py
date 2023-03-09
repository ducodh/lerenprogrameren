from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
i=1
while True:
    robotArm.grab()
    color = robotArm.scan()
    if color != "":
        for c in range(i): 
            robotArm.moveRight()
        robotArm.drop()
        for c in range(i):
            robotArm.moveLeft()
        i+=1
    if color == "":
        break
robotArm.wait()