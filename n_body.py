from scipy.constants import G
import turtle

class Body:

    def __init__(self, name, mass, start_x=0.0, start_y=0.0, vel_start_x=0.0, vel_start_y=0.0, time_multiplier=0.1):
        
        self.name = name
        self.mass = mass
        self.x = start_x
        self.y = start_y
        self.x_vel = vel_start_x
        self.y_vel = vel_start_y
        self.time_multiplier = time_multiplier
        self.first_cycle = True
        
    def updatePosition(self, xForce, yForce):

        xAcc = xForce/self.mass
        yAcc = yForce/self.mass

        if self.first_cycle:

            self.x_vel += xAcc*self.time_multiplier/2
            self.y_vel += yAcc*self.time_multiplier/2
            self.first_cycle = False

        else:

            self.x_vel += xAcc*self.time_multiplier
            self.y_vel += yAcc*self.time_multiplier
        
        # Set position
        self.x += self.x_vel
        self.y += self.y_vel
    
    def getName(self) -> str: return self.name
    def getMass(self) -> float: return self.mass
    def getX(self) -> float: return self.x
    def getY(self) -> float: return self.y

class Simulator:

    def __init__(self, bodies: list[Body]):
        self.bodies = bodies
        self.screen = turtle.getscreen()
        self.screen.bgcolor("black")
        self.turtleBodyDict = {}
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        for index, body in enumerate(bodies):
            self.turtleBodyDict[body] = turtle.Turtle()
            self.turtleBodyDict[body].color(colors[index])
            self.turtleBodyDict[body].speed("fastest")

    def cycle(self):
        for body in self.bodies:
            xForce = yForce = 0
            for other_body in self.bodies:
                if other_body is not body:
                    distance = ((body.getX() - other_body.getX())**2+(body.getY() - other_body.getY())**2)**(1/2)
                    xForce -= G*body.getMass()*other_body.getMass()*(body.getX() - other_body.getX())/distance**3
                    yForce -= G*body.getMass()*other_body.getMass()*(body.getY() - other_body.getY())/distance**3
            print("name: " + body.getName() + ", yForce: " + str(round(yForce, 20)) + ", y: " + str(round(body.getY(), 10)))
            body.updatePosition(xForce=xForce*10000000000, yForce=yForce*10000000000)

        self.draw()

    def draw(self, scale=5):
        for body in self.turtleBodyDict:
            self.turtleBodyDict[body].goto(body.getX()*scale, body.getY()*scale)
    
simulator = Simulator([Body(name="sun", mass=500, start_x=0, start_y=10, vel_start_x = -0.1, time_multiplier=0.001),
                       Body(name="othersun", mass=500, start_x=0, start_y=-10, vel_start_x=0.1, time_multiplier=0.001),
                       Body(name="planet", mass=0.1, start_x=0, start_y=50, vel_start_x=0.11, time_multiplier=0.001),
                      Body(name="otherplanet", mass=0.1, start_x=0, start_y=0, vel_start_x=0.05, time_multiplier=0.001)])

while True:
    simulator.cycle()
