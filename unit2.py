from widget import Widget
class TestWidget:
    def testSize(self):
        expectedSize = (40, 40);
        widget = Widget()
        if widget.getSize() == expectedSize:
            print ("test [Widget]: getSize works perfected!")
        else:
            print ("test [Widget]: getSize doesn't work!")

if __name__ == '__main__':
    myTest = TestWidget()
    myTest.testSize()
