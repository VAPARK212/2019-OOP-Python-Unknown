import math
from get_location import *


class Hospital_sort:
    def __init__(self):
        str_sx = get_local().get_points()[0].split('.')

        self.sx = float(get_local().get_points()[0])
        self.sy = float(get_local().get_points()[1])
        self.dic = {}

    def get_distance(self, key, x, y):
        self.dic[key] = math.sqrt((self.sx-x)*(self.sx-x)+(self.sy-y)(self.sy-y))

    def sort_by_distance(self):
        sorted_dic = sorted(self.dic.items())
        return sorted_dic


if __name__ == "__main__":
    import copy

    dic_hos = {'아산병원': [1, 2], '세종병원': [3, 4], '신촌세브란스': [5, 6]}
    di = Hospital_sort()
    for keys in dic_hos:
        di.get_distance(keys, dic_hos[keys][0], dic_hos[keys][1])
    new_dic = copy.deepcopy(di.sort_by_distance())
    print(new_dic)