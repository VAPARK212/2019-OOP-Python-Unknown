import math
import collections
from get_location import *


dic_tmp = {}

class Hospital_sort:
    def __init__(self):
        self.sx = get_local().get_points()[0]
        self.sy = get_local().get_points()[1]

    def get_distance(self, x, y):
        return math.sqrt((self.sx-x)*(self.sx-x)+(self.sy-y)(self.sy-y))

    def put_dist_dic(dist):
        pass

    def sorting(x1, y1):
        pass


if __name__ == '__main__':
    print('test')
