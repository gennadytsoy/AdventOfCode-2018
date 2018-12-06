#getting started on day 3 this one is gonna be a doozy
from math import sqrt

claims = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']
#with open('day3p1-curtis-input.txt') as infile:
    #claims = infile.read().splitlines()

fabric = (1000,1000)

#create a few helper classes to make the code easier to read rather than using lists for all the items in the claim
class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle():
    def __init__(self, coord, width=0, height=0):
        self.point = coord
        self.width = width
        self.height = height

class Claim():
    def __init__(self, id_, rect):
        self.id = id_
        self.rect = rect

    def overlap(self, other):
        #check if second rectangle x coordinate is to the right of the first rectanlge x coordinate and visa versa
        if self.rect.point.x + self.rect.width < other.rect.point.x or other.rect.point.x + other.rect.width > self.rect.point.x or self.rect.point.y + self.rect.height > other.rect.point.y or other.rect.point.y + other.rect.height > self.rect.point.y:
            return False
        
        #if self.rect.point.y < other.rect.point.y + other.rect.height or self.rect.point.y + self.rect.height < other.rect.point.y:
            #return False
        
        return True

def splitClaim(c):
    _id = c.split(' ')[0][-1]
    _coord = c.split(' ')[2][:-1].split(',')
    _size = c.split(' ')[3].split('x')
    return _id, _coord, _size

def createClaims(c):
    _id, _point, _size = splitClaim(c)
    point = Point(_point[0], _point[1])
    rect = Rectangle(point, _size[0], _size[1])
    claim  = Claim(_id, rect)
    return claim

def calcOverlap(c1, c2):
    a1 = abs(int(c1.rect.point.x) - (int(c1.rect.point.x) + int(c1.rect.width))) * abs(int(c1.rect.point.y) - (int(c1.rect.point.y) + int(c1.rect.height)))
    #print(a1)
    a2 = abs(int(c2.rect.point.x) - (int(c2.rect.point.x) + int(c2.rect.width))) * abs(int(c2.rect.point.y) - (int(c2.rect.point.y) + int(c2.rect.height)))
    #print(a2)
    #aI = (min((int(c1.rect.point.x) + int(c1.rect.width)), (int(c2.rect.point.x) + int(c2.rect.width))) - max(int(c1.rect.point.x), (int(c1.rect.point.x) + int(c1.rect.width)))) * (min((int(c1.rect.point.y) + int(c1.rect.height)), (int(c2.rect.point.y) + int(c2.rect.height))) - max(int(c1.rect.point.y), (int(c1.rect.point.y) + int(c1.rect.height))))
    aI = (min(int(c1.rect.point.x) + int(c1.rect.width), int(c2.rect.point.x) + int(c2.rect.width)) - max(int(c1.rect.point.x), int(c2.rect.point.x))) * (min(int(c1.rect.point.y) + int(c1.rect.height), int(c2.rect.point.y) + int(c2.rect.height)) - max(int(c1.rect.point.y), int(c2.rect.point.y)))
    #print(aI)
    return (aI)

totalOverlap = 0
for i in range(len(claims)-1):
    for j in range(i+1, len(claims)):
        claim1 = createClaims(claims[i]) #user helper classes to create a claim object for ease of use and readability
        claim2 = createClaims(claims[j]) #user helper classes to create a claim object for ease of use and readability
        if claim1.overlap(claim2):
            print('Claims overlap')
            totalOverlap += calcOverlap(claim1, claim2)
        else:
            print('No Claims Overlap')

print(totalOverlap)
