from time import sleep
import turtle

class SpaceShip:
    
    def __init__(self, start_x, start_y, start_x_vel=0.0, start_y_vel=0.0, time_multiplier=1.0):
        self.mass = 1
        self.x = start_x
        self.y = start_y
        self.xVel = start_x_vel
        self.yVel = start_y_vel
        self.xAcc = self.yAcc = 0
        self.first_cycle = True
        self.time_multiplier = time_multiplier

    def updatePosition(self, xForce, yForce):
        """
        updates the position of the spaceship given x and y forces
        """

        self.xAcc = xForce/self.mass
        self.yAcc = yForce/self.mass

        if self.first_cycle:

            self.xVel += self.xAcc*self.time_multiplier/2
            self.yVel += self.yAcc*self.time_multiplier/2
            self.first_cycle = False

        else:
        
            self.xVel += self.xAcc*self.time_multiplier
            self.yVel += self.yAcc*self.time_multiplier

        # x and y's are pre-calculated for next cycle relative to Feynman's method so we calculate the forces from the right place
        self.x += self.xVel*self.time_multiplier
        self.y += self.yVel*self.time_multiplier

    def getProperties(self):
        return f"x: {round(self.x, 3)}, x vel: {round(self.xVel, 3)}, x acc: {round(self.xAcc, 3)}, y: {round(self.y, 3)}, y vel: {round(self.yVel, 3)}, y acc: {round(self.yAcc, 3)}"

    def getMass(self) -> float: return self.mass
    def getX(self) -> float: return self.x
    def getY(self) -> float: return self.y


def display_point(x, y):
    """
    Displays a point on a graph with x and y values between -10 and 10 inclusive.
    If the point is outside the graph, it displays a blank grid.
    """

    if -10 <= x <= 10 and -10 <= y <= 10:
        row = 10 - y
        column = x + 10

        grid = [['.' for _ in range(21)] for _ in range(21)]

        grid[row][column] = 'O'
        grid[10][10] = '+'

        for row in grid:
            print(' '.join(row))
    else:
        grid = [['.' for _ in range(21)] for _ in range(21)]
        grid[10][10] = '+'

        for row in grid:
            print(' '.join(row))
    

my_space_ship = SpaceShip(start_x=0, start_y=5, start_x_vel=0.1, time_multiplier=0.01)
screen = turtle.getscreen()
t = turtle.Turtle()
t.shape(name="circle")
t.speed("fastest")
time = 0
distance = abs((my_space_ship.getX()**2 + my_space_ship.getY()**2))**(1/2)
# let's have 0, 0 be the gravity thingy
while True: # time < 2.4:
    distance = abs((my_space_ship.getX()**2 + my_space_ship.getY()**2))**(1/2)

    xForce = -my_space_ship.getX()*my_space_ship.getMass()/distance**3
    yForce = -my_space_ship.getY()*my_space_ship.getMass()/distance**3

    my_space_ship.updatePosition(xForce=xForce, yForce=yForce)

    distance = abs((my_space_ship.getX()**2 + my_space_ship.getY()**2))**(1/2)

    t.goto(my_space_ship.getX()*50, my_space_ship.getY()*50)
