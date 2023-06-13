from PosesBody import bodyAngles as body
from PosesBodyHead import neckAngles as neck
from PosesHand import leftHand, rightHand

def bodyNull():
    for frame, i in enumerate(body):
        lastangle = None
        for n,j in enumerate(i):
            if j == None:
                j = last_angle
                if j == None:
                    print("Angle " + str(J) + " Part " + str(n) + " Frame " + str(frame))
            else: 
                lastangle = j


bodyNull()

print(body)