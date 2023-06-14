from PosesBody import bodyAngles as body
from PosesBodyHead import neckAngles as neck
from PosesHand import leftHand, rightHand

# fullBody = []
# fullNeck = []
# fullLeftHand = []
# fullRightHand = []

def bodyNull():
    for axis, h in enumerate(body): 
        for frame, i in enumerate(h):
            for n,j in enumerate(i):
                frameE = frame
                while body[axis][frameE][n] == None and frame != 0:
                    frameE -= 1
                    if frameE < 0 or body[axis][frameE][n] != None:
                        break

                body[axis][frame][n] = body[axis][frameE][n]
                
                


def leftHandNull():
    for axis, h in enumerate(leftHand):
        for frame, i in enumerate(h):
            for n,j in enumerate(i):
                frameE = frame
                while leftHand[axis][frameE][n] == None and frame != 0:
                    frameE -=1 
                    if frameE < 0 or leftHand[axis][frameE][n] !=None:
                        break
                
                leftHand[axis][frame][n] = leftHand[axis][frameE][n]
                



def rightHandNull():
    for axis, h in enumerate(rightHand):
        for frame, i in enumerate(h):
            for n,j in enumerate(i):
                frameE = frame
                while rightHand[axis][frameE][n] == None and frame != 0:
                    frameE -=1
                    if frameE < 0 or rightHand[axis][frameE][n] != None:
                        break

                rightHand[axis][frame][n] = rightHand[axis][frameE][n]


def neckNull():
    for axis, h in enumerate(neck):
        for frame, i in enumerate(h):
            for n,j in enumerate(i):
                frameE = frame
                while neck[axis][frame][n] == None and frame != 0:
                    frameE -=1
                    if frameE < 0 or neck[axis][frameE][n] != None:
                        break

                    neck[axis][frame][n] = neck[axis][frameE][n]





bodything = bodyNull()
lefthandthing = leftHandNull()
righthandthing = rightHandNull()
neckthing = neckNull()
