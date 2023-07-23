from scipy.constants import G
import turtle
import math

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
        self.firstClicked = False
        self.scale = 5
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.new_body_mass = 100
        self.queued_body = None
        self.screen = turtle.getscreen()
        self.screen.bgcolor("black")
        self.turtleBodyDict = {}
        turtle.onscreenclick(fun=lambda x, y: self.createBody(x, y))
        turtle.onkeypress(key="m", fun=lambda: self.incrementBodyMass())
        turtle.onkeypress(key="n", fun=lambda: self.decrementBodymass())
        turtle.listen()

        for index, body in enumerate(bodies):
            self.turtleBodyDict[body] = turtle.Turtle()
            self.turtleBodyDict[body].color(colors[index])
            self.turtleBodyDict[body].speed("fastest")
            self.turtleBodyDict[body].shapesize(math.log(math.log(body.getMass(), 10), 10)/2)
            # self.turtleBodyDict[body].width(2.5)
            # self.turtleBodyDict[body].hideturtle()
            self.turtleBodyDict[body].shape("circle")

        self.utilTurtle = turtle.Turtle()
        self.utilTurtle.shape("circle")
        self.utilTurtle.penup()
        self.utilTurtle.goto(-turtle.window_width()/2 + 50, turtle.window_height()/2 - 50)
        self.utilTurtle.color("white")

    def cycle(self):
        if not self.queued_body == None: 
            self.bodies.append(self.queued_body)
            self.turtleBodyDict[self.bodies[-1]] = turtle.Turtle()
            self.turtleBodyDict[self.bodies[-1]].speed("fastest")
            self.turtleBodyDict[self.bodies[-1]].shapesize(math.log(math.log(self.queued_body.getMass(), 10), 10)/2)
            self.turtleBodyDict[self.bodies[-1]].shape("turtle")
            self.turtleBodyDict[self.bodies[-1]].color("white")
            # self.turtleBodyDict[self.bodies[-1]].penup()
            self.queued_body = None

        forces = []
        for body in self.bodies:
            xForce = yForce = 0
            for other_body in self.bodies:
                if other_body is not body:
                    distance = ((body.getX() - other_body.getX())**2+(body.getY() - other_body.getY())**2)**(1/2)
                    xForce -= G*body.getMass()*other_body.getMass()*(body.getX() - other_body.getX())/distance**3
                    yForce -= G*body.getMass()*other_body.getMass()*(body.getY() - other_body.getY())/distance**3
            forces.append((xForce, yForce))
            # print("name: " + body.getName() + ", yForce: " + str(round(yForce, 20)) + ", y: " + str(round(body.getY(), 10)))
        
        for index, body in enumerate(self.bodies):
            body.updatePosition(xForce=forces[index][0], yForce=forces[index][1])
            if abs(body.getX()*self.scale) > turtle.window_width()/2 or abs(body.getY()*self.scale) > turtle.window_height()/2: 
                self.turtleBodyDict[body].hideturtle()
                self.bodies.pop(index)
                self.turtleBodyDict.pop(body)

        self.draw()

    def createBody(self, x, y):
        if not self.firstClicked:
            self.new_body_start_x = x
            self.new_body_start_y = y
            self.utilTurtle.color("pink")
            self.firstClicked = True

        else:
            self.queued_body = Body(name="user body", mass=self.new_body_mass, 
                                    start_x=self.new_body_start_x/self.scale, start_y = self.new_body_start_y/self.scale,
                                    vel_start_x=(x-self.new_body_start_x)/500, vel_start_y=(y-self.new_body_start_y)/500, time_multiplier=0.001)

            self.utilTurtle.color("white")
            self.firstClicked = False

    def incrementBodyMass(self): 
        self.new_body_mass *= 100
    
    def decrementBodymass(self): 
        self.new_body_mass /= 100
        

    def draw(self):
        if self.new_body_mass >= 1: self.utilTurtle.shapesize(math.log(math.log(self.new_body_mass, 10)+1, 10)/2)
        self.utilTurtle.clear()
        for body in self.turtleBodyDict:
            self.turtleBodyDict[body].goto(body.getX()*self.scale, body.getY()*self.scale)

    
# simulator = Simulator([Body(name="sun", mass=5000000000000, start_x=0, start_y=10, vel_start_x = -0.1, time_multiplier=0.001),
#                        Body(name="othersun", mass=5000000000000, start_x=0, start_y=-10, vel_start_x=0.1, time_multiplier=0.001),
#                         Body(name="planet", mass=100, start_x=0, start_y=50, vel_start_x=0.11, time_multiplier=0.001),
#                        Body(name="otherplanet", mass=100, start_x=0, start_y=0, vel_start_x=0.07, time_multiplier=0.001)])

# simulator = Simulator([Body(name="sun", mass=1000, start_x=0, start_y=0, vel_start_x = 0, time_multiplier=0.001),
#                       Body(name="planet", mass=1, start_x=0, start_y=50, vel_start_x = .1, time_multiplier=0.001)])


# simulator = Simulator([Body(name="sun", mass=10000000000000, start_x=0, start_y=10, vel_start_x = 0.1, time_multiplier=0.001),
#                        Body(name="othersun", mass=10000000000000, start_x=0, start_y=-10, vel_start_x=-0.1, time_multiplier=0.001),
#                        Body(name="thirdsun", mass=10000000000000, start_x=0, start_y=50, vel_start_x=0.2, time_multiplier=0.001),
#                        Body(name="otherplanet", mass=100, start_x=0, start_y=20, vel_start_x=0.35, time_multiplier=0.001)])

simulator = Simulator([Body(name="sun", mass=10000000000000, start_x=0, start_y=-20, vel_start_x = 0.2, time_multiplier=0.001),
                       Body(name="othersun", mass=10000000000000, start_x=0, start_y=-30, vel_start_x=0.0, time_multiplier=0.001),
                       Body(name="thirdsun", mass=10000000000000, start_x=0, start_y=20, vel_start_x=-0.1, time_multiplier=0.001),
                       Body(name="otherplanet", mass=100, start_x=0, start_y=0, vel_start_x=0.2, time_multiplier=0.001)])

while True:
    simulator.cycle()
