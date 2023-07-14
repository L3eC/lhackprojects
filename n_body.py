class Body:

    def __init__(self, mass, start_x, start_y, vel_start_x, vel_start_y):

        self.mass = mass
        self.x = start_x
        self.y = start_y
        self.x_vel = vel_start_x
        self.y_vel = vel_start_y
        
    def updatePosition(self):
        # Set position
        self.x += self.x_vel
        self.y += self.y_vel

        # Calculate forces, velocities
        x_force = 
        y_force =
