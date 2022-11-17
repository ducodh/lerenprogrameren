from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
counter = 9
for i in range(5):
    robotArm.grab()
    for c in range (counter):
        robotArm.moveRight()
    robotArm.drop()
    counter-=1
    for c in range(counter):
        robotArm.moveLeft()
    counter-=1
robotArm.wait()