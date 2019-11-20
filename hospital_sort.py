import math
import collections
from get_location import *
from hospital_info import *

x = get_local().get_points()[0]
y = get_local().get_points()[1]

print(x, y)



def sorting(x1, y1):
    Point2D = collections.namedtuple('Point2D', ['x', 'y'])
    p1 = Point2D(x=x1, y=y1)
    p2 = Point2D(x=x2, y=y2)
