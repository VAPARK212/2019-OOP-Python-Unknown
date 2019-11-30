import webbrowser


# 장소의 이름과 위도, 경도를 전달받으면 해당 위치의 카카오맵을 여는 함수
def open_map(name, y, x):   # 병원 이름, 위도, 경도 전달
    link = "https://map.kakao.com/link/map/"+str(name)+','+str(y)+','+str(x)    # 카카오 맵 링크
    # print(link)
    webbrowser.open(link)


if __name__ == "__main__":
    open_map("카카오", 37.402056, 127.108212)


# 출처: https://riptutorial.com/ko/python/example/27066/%EA%B8%B0%EB%B3%B8-%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%EB%A1%9C-url-%EC%97%B4%EA%B8%B0
# 출처: http://apis.map.kakao.com/web/guide/
