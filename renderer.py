import sys
import numpy as np
import PyQt5
from typing import List
from PyQt5.QtCore import Qt, QEvent
from PyQt5 import QtWidgets, QtCore, QtGui

# all distance units inches

# while True:
#     x_coord_of_rendered = 24/point_z * point_irl_coords[0]
#     y_coord_of_rendered = 24/point_z * point_irl_coords[1]



class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()

        self.scene = QtWidgets.QGraphicsScene(0, 0, 200, 200)
        self.view = QtWidgets.QGraphicsView(self.scene)

        self.test_triangle = Triangle3d([[-1, -1, 20], [1, -1, 20], [0, 1, 20]], self.scene)

        """
        self.point_irl_coords = [0, 0, 20]
        self.convergence_pt_to_screen_distance = 24

        self.ellipse_representing_rendered = QtWidgets.QGraphicsEllipseItem(0, 0, 10, 10)
        self.ellipse_representing_rendered.setBrush(Qt.red)
        self.scene.addItem(self.ellipse_representing_rendered)
        """

        self.refresh_time = 17 # => ~60fps
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_stuff)
        self.timer.start(self.refresh_time)

        self.setFocusPolicy(Qt.StrongFocus)
        self.setCentralWidget(self.view)

        self.show()

    def keyPressEvent(self, a0):

        print(f"key pressed!! Key text is {a0.text()}")

        # update irl coords of point
        if a0.text() == "k": # go up
            triangle_coords = self.test_triangle.get_coords()
            for point in triangle_coords: # TODO: make this into a sensible matrix based thingy
                point[1] += 1
            self.test_triangle.set_coords(triangle_coords)
            #  self.point_irl_coords[1] += 1

        elif a0.text() == "j": # go down
            triangle_coords = self.test_triangle.get_coords()
            for point in triangle_coords:
                point[1] -= 1
            self.test_triangle.set_coords(triangle_coords)
            #  self.point_irl_coords[1] -= 1

        elif a0.text() == "h":
            triangle_coords = self.test_triangle.get_coords()
            for point in triangle_coords:
                point[0] -= 1
            self.test_triangle.set_coords(triangle_coords)
            #  self.point_irl_coords[0] -= 1

        elif a0.text() == "l":
            triangle_coords = self.test_triangle.get_coords()
            for point in triangle_coords:
                point[0] += 1
            self.test_triangle.set_coords(triangle_coords)
            #  self.point_irl_coords[0] += 1
        elif a0.text() == "i":
            triangle_coords = self.test_triangle.get_coords()
            for point in triangle_coords:
                point[2] -= 1
            self.test_triangle.set_coords(triangle_coords)
            #  self.point_irl_coords[2] -= 1
        elif a0.text() == "o":
            triangle_coords = self.test_triangle.get_coords()
            for point in triangle_coords:
                point[2] += 1
            self.test_triangle.set_coords(triangle_coords)
            #  self.point_irl_coords[2] += 1
        else:
            super(Ui, self).keyPressEvent(a0)
            return

        # # calculate new projected coords of point's image
        # if not self.point_irl_coords[2] == 0:
        #     x_coord_of_rendered = 24/self.point_irl_coords[2] * self.point_irl_coords[0] + 100
        #     y_coord_of_rendered = 24/self.point_irl_coords[2] * self.point_irl_coords[1] + 100
        # else:
        #     x_coord_of_rendered = 24/(self.point_irl_coords[2] + 0.01) * self.point_irl_coords[0] + 100
        #     y_coord_of_rendered = 24/(self.point_irl_coords[2] + 0.01) * self.point_irl_coords[1] + 100

        # self.ellipse_representing_rendered.setX(x_coord_of_rendered)
        # self.ellipse_representing_rendered.setY(y_coord_of_rendered)


    def update_stuff(self):
        pass


class Triangle3d:

    def __init__(self, points_coords: List[List[float]], scene: QtWidgets.QGraphicsScene):

        self.points_coords = points_coords

        self.projected_triangle = QtWidgets.QGraphicsPolygonItem(QtGui.QPolygonF([QtCore.QPointF(0, 0),
                                                                                 QtCore.QPointF(1, 0),
                                                                                 QtCore.QPointF(0, 1)]))

        scene.addItem(self.projected_triangle)

        self.draw()

    def draw(self):

        projected_coords = []
        for point_coords in self.points_coords:
            if not point_coords[2] == 0:
                projected_x_coord = 24 / point_coords[2] * point_coords[0] + 100
                projected_y_coord = 24 / point_coords[2] * point_coords[1] + 100
            else:
                projected_x_coord = 24 / (point_coords[2] + 0.01) * point_coords[0] + 100
                projected_y_coord = 24 / (point_coords[2] + 0.01) * point_coords[1] + 100

            projected_coords.append([projected_x_coord, projected_y_coord])

        self.projected_triangle.setPolygon(QtGui.QPolygonF([QtCore.QPointF(projected_coords[0][0], projected_coords[0][1]),
                                                            QtCore.QPointF(projected_coords[1][0], projected_coords[1][1]),
                                                            QtCore.QPointF(projected_coords[2][0], projected_coords[2][1])]))

    def set_coords(self, points_coords: List[List[float]], auto_draw: bool = True):
        self.points_coords = points_coords
        if auto_draw: self.draw()

    def get_coords(self) -> List[List[float]]:
        return self.points_coords

    def get_qpolygon(self): return self.projected_triangle


app = QtWidgets.QApplication(sys.argv)
ui = Ui()

app.exec_()
