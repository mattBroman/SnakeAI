class Segment:
    width = 20;
    height = 20;
    color = (255, 0, 0)

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def move(self, vec):
        self.x += vec[0]*Segment.width
        self.y += vec[1]*Segment.height

class Snake:
    def __init__(self, _x=100, _y=100):
        self.head = Segment(_x,_y)
        self.body = [self.head]
        self.moveVec = [0, 1]

    def move(self):
        finalSeg = self.body.pop()
        finalSeg.x = self.head.x + self.moveVec[0] * 20
        finalSeg.y = self.head.y + self.moveVec[1] * 20

        self.head = finalSeg
        self.body.insert(0, finalSeg)

    def grow(self):
        newSeg = Segment(self.body[-1].x, self.body[-1].y)
        self.move()
        self.body.append(newSeg)

    def changeDir(self, _x, _y):
        if (_x != 0 and self.moveVec[0] == 0) or (_y != 0 and self.moveVec[1] == 0) :
            self.moveVec[0] = _x
            self.moveVec[1] = _y
