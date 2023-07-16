class Body:

    def __init__(self, mass, start_x, start_y, vel_start_x, vel_start_y, time_multiplier):

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

class Simulator:

    def __init__(self, bodies: list):
        self.bodies = bodies

    def cycle(self):
        for body in self.bodies:
            xForce = yForce = 0
            body.updatePosition(
