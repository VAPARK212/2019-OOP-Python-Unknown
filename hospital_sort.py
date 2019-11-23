from get_location import *
import operator


class Hospital_sort:
    def __init__(self):
        self.sx = float(get_local().get_points()[0])    # ip 주소 이용-> 사용자 위치 좌표
        self.sy = float(get_local().get_points()[1])
        self.dic = {}

    def cal_distance(self, key, x, y):
        self.dic[key] = (self.sx-x)*(self.sx-x)+(self.sy-y)*(self.sy-y)

    def sort_by_distance(self):     # 거리 기준 정렬 후 병원 이름 리스트 리턴
        sorted_dic = sorted(self.dic.items(), key=operator.itemgetter(1))
        # print(len(sorted_dic))
        # print(sorted_dic)
        li = []
        for i in range(len(sorted_dic)):
            li.append(sorted_dic[i][0])
        return li


# import하고 사용 예시
if __name__ == "__main__":
    dic_hos = {'아산병원': [1, 2], '세종병원': [3, 4], '신촌세브란스': [5, 6]}    # 임의의 hospital info data 딕셔너리
    di = Hospital_sort()    # class
    for keys in dic_hos:
        di.cal_distance(keys, dic_hos[keys][0], dic_hos[keys][1])    # 딕셔너리의 key와 value 값(x좌표 and y좌표)을 cal_distance 함수에 전달
    hospital_name_list = di.sort_by_distance()     # 반드시 cal_distance 함수 실행 이후에 sort_by_distance 함수를 실행, 거리 기준으로 정렬된 병원 이름 데이터 리스트 리턴
    print(hospital_name_list)

    # 제대로 정렬되었는지 확인용
    # di.sort_by_distance()
