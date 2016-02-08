class Location:
    def __init__(self, x, y):
        self.xloc = x
        self.yloc = y


    def getx(self):
        """
        Returns x location
        """
        return self.xloc


    def gety(self):
        """
        Returns y location
        """
        return self.yloc


    def setx(self, x):
        """
        Sets the x value
        """
        self.xloc = x


    def sety(self, y):
        """
        Sets the y value
        """
        self.yloc = y


    def tostring(self):
        """
        Returns the x and y location in a string
        """
        return "x: " + str(self.xloc) + " y: " + str(self.yloc)