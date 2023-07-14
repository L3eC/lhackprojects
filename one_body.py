from time import sleep

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

    def updatePosition(self):
        """
        updates the position of the spaceship given x and y forces
        """

        if self.first_cycle:
            self.xVel += self.xAcc*self.time_multiplier/2
            self.yVel += self.yAcc*self.time_multiplier/2
            self.first_cycle = False

        else:
            self.x += self.xVel*self.time_multiplier
            self.y += self.yVel*self.time_multiplier

            # calculate force HERE before the next step- the forces are incorrect because
            # they're passed before those new x and y values are calculated
            distance = abs((my_space_ship.getX()**2 + my_space_ship.getY()**2))**(1/2)

            xForce = -self.x*self.mass/distance**3
            yForce = -self.y*self.mass/distance**3


            self.xAcc = xForce/self.mass
            self.yAcc = yForce/self.mass
        
            self.xVel += self.xAcc*self.time_multiplier
            self.yVel += self.yAcc*self.time_multiplier

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
    

my_space_ship = SpaceShip(start_x=0.5, start_y=0, start_y_vel=1.630, time_multiplier=0.1)
time = 0
time_mult = 0.1
distance = abs((my_space_ship.getX()**2 + my_space_ship.getY()**2))**(1/2)
# let's have 0, 0 be the gravity thingy
while time < 2.4:
    print('\n-------------------------------\n')

    my_space_ship.updatePosition()

    distance = abs((my_space_ship.getX()**2 + my_space_ship.getY()**2))**(1/2)

    print(f"time: {round(time, 3)}, {my_space_ship.getProperties()}, distance: {round(distance, 3)}, 1/distance^3: {round(1/distance**3, 3)}")
    
    # display_point(int(my_space_ship.getX()), int(my_space_ship.getY()))

    sleep(1/15)
    time += time_mult
