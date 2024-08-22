from physics import v2
class icon:
    def __init__(self, points):
        self.points = points
    def to_tuple(self):
        pts = []
        for pt in self.points:
            pts.append(pt.tuple())
        self.pts = pts
        return self.pts
pts = [
v2(0, 5),
v2(0, 2),
v2(2, 0),
v2(5, 0),
v2(5, 5),
v2(4, 5),
v2(4, 3),
v2(1, 3),
v2(1, 5)
]
save = icon(pts)

pts = [
v2(3.5, 3.5),
v2(1.5, 1.5),
v2(3, 0),
v2(5, 0),
v2(5, 2),
v2(2, 5),
v2(0, 5),
v2(0, 3),
v2(1.5, 1.5)
]
eraser = icon(pts)

pts = [
v2(0, 4),
v2(4, 0),
v2(5, 1),
v2(1, 5),
v2(0, 5),
v2(0, 4),
v2(1, 5)
]
pen = icon(pts)

icons = []
icons.append(save)
icons.append(eraser)
icons.append(pen)