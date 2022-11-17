from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for c in range(10):  
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(4):
        robotArm.moveLeft()
    if c==1 or c>=3 and c<5 or c>=6:
        robotArm.moveLeft()
robotArm.wait()