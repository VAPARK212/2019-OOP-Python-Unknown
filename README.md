# 2019-2 객체지향 프로그래밍 프로젝트 - **{팀명}**
구성원: 2-2 양윤정 | 2-3 박유진 | 2-6 김선진

## 1. 주제
최적 응급의료센터 찾기

## 2. 동기
세종시에서 거주하고 하고 있는 학생으로, 아직 종합병원의 응급실이 없었을 적에 세종시에서 급성맹장염에 걸렸었다. 세종시 내 충남대병원 응급센터 분원, 유성 선병원을 방문했지만, 전자는 내과 의료진이 근무하지 않는다는 이유로, 후자는 소아과가 없다는 이유로 응급의료시술을 받지 못하고 충남대병원까지 가서 수술을 받은 적이 있다. 대전 내에서도 병원을 어디 갈지 잘 몰라 헤맸었다. 이런 급박한 상황에서 최적의 응급의료센터를 찾아주는 프로그램을 개발하고자 했다.

## 3. 프로그램 사용 대상
급하게 응급의료센터를 찾고 있으나, 자신의 위치에서 최적의 응급의료센터를 찾기 어려운 사람들을 위한 프로그램이다. 예를 들면 새로 이사한 사람들이나, 아직은 응급의료센터가 없는 지역에 거주하는 사람들은 이 프로그램을 이용하여 자신에게 최적의 응급의료센터를 찾을 수 있을 것이다.

## 4. 목적
현재 위치에 대한 정보를 입력받으면 가용병상 정보, 떨어진 거리 등 다양한 필수 정보들을 종합하여 병적으로 응급한 상황이 발생하였을 때 현재 상태에 최적인 병원을 제시해주는 프로그램을 구현하는 것이 목표다. 이 프로그램을 통해 뇌출혈, 뇌경색, 응급투석 등 응급 상황에서 보다 더 빠른 대처를 할 수 있을 것으로 기대된다.

현재 위치 + 갈 수 있는 병원(수용정보, 가용병상 정보) -> 갈 수 있는 병원 중 제일 가까움(위치 정보) -> 제시


## 5. 주요기능
사용자의 현재 위치를 IP 주소로 부터 받고
사용자가 본인에게 필요한 진료나 응급처치를 직접 선택하게 하여
사용자에게 필요한 응급 대처가 가능한 병원 중 가장 가까운 병원(들)의 이름과 주소를 제시해준다. (병원의 개수는 선택 조건마다 다르기 때문이다)


## 6. 프로젝트 핵심
API 받기:
Kakao map API
(http://apis.map.kakao.com/android/documentation/#MapView_CurrentLocationEventListener_Methods_onCurrentLocationUpdate)
전국 응급의료기관 조회 서비스 API
XML 형식으로 되어있어 조건에 맞는 요청을 한 후 결과 parsing하는 방법으로 접근
(https://www.data.go.kr/dataset/15000563/openapi.do)

각 API를 이용해 정보를 받아서 이용 할 수 있는 형태로 변환한다.

IP주소에서 받는 정보:
현재 위치 (시 단위)

Kakao map API
병원의 이름을 이용하여 사용자와 가까운 거리의 병원들을 찾아낸다.
-> 이 정보로 이용할 수 있는 병원들 중에 현위치와 가까운 순서대로 정렬한다.

응급의료 조회서비스에서 받는 정보:
기관 정보
: ( 기관명 / 기관 id / 주소 / 응급실 전화 )
: ( 응급실 / 응급실 가용여부 )
-> 응급의료센터 추천 시 제시

수술 가능 정보 (Y/N)
: 뇌출혈 수술
뇌경색의재관류
심근경색의재관류
복부손상의수술
사지접합의수술
응급내시경
응급투석
조산산모
정신질환자
신생아
중증화상
-> 필요한 의료 처리 가능 정보 판단 

UI 구현 :
PyQt5으로 UI를 구현
사용자의 위치 정보를 IP를 통하여 확인
사용자의 현재 상태(아픈 곳) input (ex: 외상)

판단:
사용자가 중복 입력한 정보를 바탕으로 위치한 시 내의 이용할 수 있는 병원을 선별한다.
선별한 병원들이 각각 가장 가까운 거리 순으로 5개의 병원을 선정한 후, 병원 정보를 사용자에게 제시한다. 
만약에 병원이 없는 경우, 그냥 가까운 병원을 찾아준다. 


## 7. 구현에 필요한 라이브러리나 기술
GUI | pyqt5 | GUI 구성을 마우스로 할 수 있는 프로그램 제공
platform 에러 발생시: http://doongkibangki.tistory.com/24
 
Kakao API
주소 좌표: https://developers.kakao.com/docs/restapi/local

ipapi: ip 추적을 통해 사용자의 현재 위치 확인
주소: https://ipapi.co/

API 신청을 통하여 획득한 키를 이용하여 웹페이지 접속 후 파싱
requests, bs4이용
전국 응급의료기관 조회 서비스:
병원 정보:  https://www.data.go.kr/dataset/15000563/openapi.do


## 8. **분업 계획**
다음 3가지 역할을 위주로 분업하려고 한다.
박유진:
- 전국 응급의료기관 조회 서비스 API(병원 정보)를 이용하여 위치에 있는 모든 병원들의 정보를 찾아낸다
- 각 병원의 id를 이용해서 각 병원이 행할 수 있는 진료를 정리하고 함수화한다.

김선진:
- IP주소를 이용하여 사용자가 위치한 곳을 찾아내고, 이 정보를 공유한다
- Kakao map API(사용자의 위치 탐색)를 이용해서 사용자가 이용할 수 있는 병원들을 가까운 순서로 정렬하고, 그 결과를 UI 개발자에게 보낸다

양윤정:
- UI를 작성하여 사용자가 손 쉽고 헷갈리지 않게 정보를 입력(병명이나 특수한 시술에 관한 설명은 여기서 진행)하고, 결과가 효과적으로 보이도록 설계
- 전국 응급의료기관 조회 서비스 API(병원 정보)의 정리된 정보 중에서 입력한 정보를 토대로 사용자가 갈 수 있는 병원들을 선별한다.


## 9. 기타

## 10. 실행 방법
1. Treatment.py를 실행합니다.
2. PyQt UI에 제시된 진료 목록 중에서 필요한 것을 선택합니다(선택하지 않아도 됩니다, 중복가능).
3. 약 10초 후 우측에 현위치, 현상황에서 최적인 응급의료센터와 관련 정보가 출력되고 Map 링크를 클릭하면 해당 병원의 카카오맵 웹사이트가 열립니다.
* 응급의료센터 공공데이터에 포함되지 않은 병원일 경우 실존해도 출력되지 않을 수 있습니다.
* 만약 사용자의 현재 위치 기준이 아닌(ip 추적을 하지 않고) 특정 도시 기준으로 프로그램을 테스트해보고 싶으시다면 Treatment.py의 154번째줄을 region1 = '서울특별시' 처럼 특정 도시명으로 수정하시면 됩니다.

<hr>

#### readme 작성관련 참고하기 [바로가기](https://heropy.blog/2017/09/30/markdown/)

#### 예시 계획서 [[예시 1]](https://docs.google.com/document/d/1hcuGhTtmiTUxuBtr3O6ffrSMahKNhEj33woE02V-84U/edit?usp=sharing) | [[예시 2]](https://docs.google.com/document/d/1FmxTZvmrroOW4uZ34Xfyyk9ejrQNx6gtsB6k7zOvHYE/edit?usp=sharing) | [[예시 3]](https://github.com/goldmango328/2018-OOP-Python-Light) | [[예시4]](https://github.com/ssy05468/2018-OOP-Python-lightbulb) | [[모두보기]](https://github.com/kadragon/oop_project_ex/network/members)
