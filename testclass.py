class TestDat():
    def __init__(self):
        self.Dat1 = None
        self.Dat2 = None
    
TestArray = [] #empty array
size = 2       #number of loops

for x in range(size):  # appending empty objects
    TestArray.append(TestDat())

#initialize later
TestArray[0].Dat1 = 0
TestArray[0].Dat2 = 1

TestArray[1].Dat1 = 3
TestArray[1].Dat2 = 4

print("print everithing")
for x in range(len(TestArray)):
    print("object "+str(x))
    print(TestArray[x].Dat1)
    print(TestArray[x].Dat2)