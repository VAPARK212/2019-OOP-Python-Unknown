from get_location import *
import operator


class Hospital_sort:
    def __init__(self):
        self.sx = float(get_local().get_points()[0])    # ip 주소 이용-> 사용자 위치 좌표
        self.sy = float(get_local().get_points()[1])
        self.dic = {}

    # 사용자의 현재 위치와 병원 사이 거리의 제곱을 계산하여 class 내의 dict에 저장하는 함수
    def cal_distance(self, key, x, y):
        self.dic[key] = (self.sx-x)*(self.sx-x)+(self.sy-y)*(self.sy-y)

    # class 내의 dict의 value를 기준으로 오름차순 정렬하는 함수
    def sort_by_distance(self):     # 거리 기준 정렬 후 병원 이름 리스트 리턴
        sorted_dic = sorted(self.dic.items(), key=operator.itemgetter(1))
        # print(len(sorted_dic))
        # print(sorted_dic)
        li = []
        length = len(sorted_dic)

        # 최종 출력되는 병원 정보는 5개이므로 불필요하게 소모되는 시간을 단축하기 위해 정렬된 병원의 개수가 5개보다 많을 경우 리턴하는 병원 개수를 5개로 제한
        if(length > 5):
            length = 5
        for i in range(length):
            li.append(sorted_dic[i][0])
        return li


# import하고 사용 예시
if __name__ == "__main__":
    dic_hos = {'아산병원': [2.35126543215, 2], '세종병원': [3, 4], '신촌세브란스': [5, 6]}    # 임의의 hospital info data 딕셔너리
    di = Hospital_sort()    # class
    for keys in dic_hos:
        di.cal_distance(keys, dic_hos[keys][0], dic_hos[keys][1])    # 병원 이름과 해당 병원의 x좌표, y좌표를 cal_distance 함수에 전달
    hospital_name_list = di.sort_by_distance()     # 반드시 cal_distance 함수 실행 이후에 sort_by_distance 함수를 실행, 거리 기준으로 정렬된 병원 이름 데이터 리스트 리턴
    print(hospital_name_list)

    # 제대로 정렬되었는지 확인용
    # di.sort_by_distance()
