from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')

for c in range(8):
    robotArm.moveRight()
for i in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color != "white":
        robotArm.drop()
    else:
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    if i < 8:
        robotArm.moveLeft()
robotArm.wait()

# count=8
# for i in range(count):
#     robotArm.grab()
#     color = robotArm.scan()
#     if color != "white":
#         robotArm.drop()
#         robotArm.moveRight()
#     else:
#         robotArm.moveRight()
#         robotArm.drop()
#         robotArm.moveRight()
#         count -= 1
