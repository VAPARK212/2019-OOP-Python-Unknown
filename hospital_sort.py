import math
from get_location import *


class Hospital_sort:
    def __init__(self):
        self.sx = get_local().get_points()[0]
        self.sy = get_local().get_points()[1]
        self.dic = {}

    def get_distance(self, key, x, y):
        self.dic[key] = math.sqrt((self.sx-x)*(self.sx-x)+(self.sy-y)(self.sy-y))
        return self.dic[key]

    def sorting(self):
        sorted_dic = sorted(self.dic.items())
        return sorted_dic


if __name__ == "__main__":
    dic_hos = {'아산병원': {1, 2}, '세종병원': {3, 4}, '신촌세브란스': {5, 6}}
    dic = Hospital_sort
    for key in dic_hos:
        dic.get_distance(key, dic_hos[key][0], dic_hos[key][1])
