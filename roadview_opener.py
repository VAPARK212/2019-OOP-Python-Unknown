import webbrowser


def open_map(x, y):
    frontcode = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8"/>
        <title>Kakao 지도 시작하기</title>
    </head>
    <body>
        <div id="map" style="width:500px;height:400px;"></div>
        <script type="text/javascript" src="https://dapi.kakao.com/v2/maps/sdk.js?appkey=ea01b00367677ce3c9f5208fa6f4a478"></script>
        <script>
            var container = document.getElementById('map');
            var options = {
                center: new kakao.maps.LatLng(
    """
    rearcode = """
    ),
                level: 3
            };
    
            var map = new kakao.maps.Map(container, options);
        </script>
    </body>
    </html>
    
    <!--출처: http://apis.map.kakao.com/web/guide/#step1-->
    """

    with open("roadview.html", 'w') as f:
        f.write(str(frontcode)+str(x)+','+str(y)+str(rearcode))

    webbrowser.open("roadview.html")


if __name__ == "__main__":
    open_map(33.450701, 126.570667)

# 출처: https://riptutorial.com/ko/python/example/27066/%EA%B8%B0%EB%B3%B8-%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%EB%A1%9C-url-%EC%97%B4%EA%B8%B0