import webbrowser


def open_map(name, y, x, localID): # roadview.html 여는 함수
    frontcode = """
        <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Map</title>
        
    </head>
    <body>
    <div id="map" style="width:100%;height:350px;"></div>
    
    <script type="text/javascript" src="https://dapi.kakao.com/v2/maps/sdk.js?appkey=ea01b00367677ce3c9f5208fa6f4a478"></script>
    <script>
    """
    rearcode = """
    var mapContainer = document.getElementById('map'),
        mapOption = { 
            center: new kakao.maps.LatLng(y,x),
            level: 3
        };
    
    var map = new kakao.maps.Map(mapContainer, mapOption);
    
    var markerPosition  = new kakao.maps.LatLng(y, x); 
    
    var marker = new kakao.maps.Marker({
        position: markerPosition
    });

    marker.setMap(map);
    
    var iwContent = '<div style="padding:5px;">name<br><a href="https://map.kakao.com/link/to/"""

    lastcode = """style="color:blue" target="_blank">Way</a></div>',
        iwPosition = new kakao.maps.LatLng(y, x);
    
    var infowindow = new kakao.maps.InfoWindow({
        position : iwPosition, 
        content : iwContent
    
    
    });
    
      
    infowindow.open(map, marker);
    
    
    </script>
    </body>
    </html>
    """

    with open("roadview.html", 'w') as f:
        f.write(str(frontcode)+'\n'+'    let name=\''+str(name)+'\'\n'+'    let y='+str(y)+'\n'+'    let x='+str(x)+str(rearcode)+str(localID)+"\""+str(lastcode))

    f.close()
    webbrowser.open("roadview.html")


if __name__ == "__main__":
    open_map('kakao', 37.402056, 127.108212, 18577297)

# 출처: https://riptutorial.com/ko/python/example/27066/%EA%B8%B0%EB%B3%B8-%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%EB%A1%9C-url-%EC%97%B4%EA%B8%B0