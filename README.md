# healthweb
keypoint detection 모델을 이용한 운동 보조 웹 애플리케이션 (2022/12/05 ~ 2022/12/23, 2023/08/23 ~)

<br>

## 프로젝트 개요
- 가끔 맨몸과 아령 1개로 홈트를 하는데 운동 사이클을 관리 해주는 무언가가 있으면 좋겠다는 생각을 하게 되었습니다.
- 그래서 홈트가 유행하고 있는 지금 시대에 keypoint detection을 활용해서 홈트를 하는데 편의성을 제공하고자 웹 서비스를 만들고자 했습니다.
- 여기서 편의성이란 몇 세트인지 한 세트에 몇개를 할 것인지 설정을 하고 1개를 할 때마다 카운팅 해주고 1세트가 끝날 때마다 휴식시간을 타이머 해주거나 크게 잘못된 자세를 지적해주거나 등입니다.

<br>

## 사용 기술 스택
<div>
  <img src="https://img.shields.io/badge/Git-F05032?style=flat&logo=Git&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=GitHub&logoColor=white"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=flat&logo=Django&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=flat&logo=OpenCV&logoColor=white"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=HTML5&logoColor=white"/>
  <img src="https://img.shields.io/badge/Amazon EC2-FF9900?style=flat&logo=Amazon EC2&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=JavaScript&logoColor=white"/>
  <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat&logo=Bootstrap&logoColor=white"/>
</div>

<br>

## 사용 keypoint detection 모델
- mediapipe pose(https://developers.google.com/mediapipe/solutions/vision/pose_landmarker/)
  - keypoint detection을 사용하는 이유는 포즈를 추정하는데 좋기 때문입니다.

<br>

## 진행 과정
### 1. Django, HTML 틀 구성
* 아나콘다 가상환경에서 Django를 설치 후 healthweb 폴더에 Django 프로젝트와 앱 생성

<img src="https://github.com/mooncw/healthweb/assets/97713997/99b1b983-8484-4cf0-85a8-d4fdae639dfc" width="20%" height="20%">

<br>
<br>

* 사용할 HTML 틀 구성

<img src="https://github.com/mooncw/healthweb/assets/97713997/0e1d6b78-8b90-42fe-aaeb-f1ed2399f19f" width="18%" height="18%">

<br>
<br>

### 2. db.sqlite3 테이블 생성 & Django model 추가
* 보조할 운동에 대한 데이터가 들어있는 MySQL RDB를 구축
  - Django shell을 이용하여 현재 쓸 데이터만 넣었습니다.

<img src="https://github.com/mooncw/healthweb/assets/97713997/2198e50c-57ea-4f0d-9767-d76595e6a379" width="35%" height="35%">

<br>

* Django의 models.py

<img src="https://github.com/mooncw/healthweb/assets/97713997/6ae675cd-df81-4ac0-ac2d-51d1aca300c7" width="40%" height="40%">

<br>
<br>


### 3. Django 틀에 내용 추가
* urls.py
  - url과 view를 매칭시키는 역할을 합니다.

<img src="https://github.com/mooncw/healthweb/assets/97713997/7b1e66c0-f9fa-4c03-902f-6c34eb7f66a3" width="47%" height="47%">

<br>
<br>

* views.py
  - 사용자의 요청을 받아 처리하고, url에서 얻은 id 값에 매칭되는 데이터를 Exercises에서 가져와 html에 전달하고 처리 결과를 반환하는 역할을 합니다.
 
<img src="https://github.com/mooncw/healthweb/assets/97713997/a33b3719-83b5-4847-b08b-f0d7847908b5" width="62%" height="62%">

<br>
<br>


### 4. Keypoint Detection 모델 선택
* 첫 번째 선택한 Openpose 모델 성능 테스트한 결과
  - 탐지 정확도도 좀 떨어지고
  - pose를 파악하기 위한 keypoint 개수도 적은 편이기 때문에
  - 운동 보조를 위한 keypoint detection 모델에는 적합하지않다고 판단했습니다.

* 두 번째 선택한 mediapipe pose 모델 성능 테스트한 결과
  - openpose보다 탐지가 훨씬 정확하고
  - keypoint 개수도 많은 편이고
  - keypoint마다 카메라와 신체 사이의 거리를 출력해주고
  - 어떤 keypoint가 카메라에 보이는 상태인지 안보이는 상태인지 출력해주기 때문에
  - 운동 보조를 위한 keypoint detection 모델로 적합하다고 판단해서 선택했습니다.

* Mediapipe pose 모델 관련 링크(https://developers.google.com/mediapipe/solutions/vision/pose_landmarker/)

<br>

### 5. HTML 내용 추가
**1) index.html(홈 화면)**

<img src="https://github.com/mooncw/healthweb/assets/97713997/62bdf80c-99c4-437f-a72d-4ba00c7ee850" width="62%" height="62%">

* bootstrap을 이용하여 간단한 프론트엔드 구성
<img src="https://github.com/mooncw/healthweb/assets/97713997/387a8804-5b26-4233-b8f3-2a5dc048af61" width="72%" height="72%">

<br>
<br>

* Let’s Go 버튼 누를 시 이동할 url 형식
<img src="https://github.com/mooncw/healthweb/assets/97713997/7aed24ad-871a-41ed-8a32-4c195f998b32" width="40%" height="40%">

<br>
<br>
<br>

**2) screen.html(운동 선택 후 화면)**

<img src="https://github.com/mooncw/healthweb/assets/97713997/bbb21c92-67f8-45c4-9a87-036d2e86a0a7" width="62%" height="62%">

<br>
<br>

* views.py에서 넘어온 exercise_data 이용
<img src="https://github.com/mooncw/healthweb/assets/97713997/79064530-9307-4e42-8d2a-be9f99702e13" width="69%" height="69%">

<br>
<br>

### 6. 운동 종류 선택 후 운동 알고리즘 구현
* 집에서 가장 쉽게 할 수 있는 운동으로 맨몸 운동인 푸쉬업과 스쿼트가 떠올라서 보조할 운동으로 이 2가지를 선택했습니다.
* 옆모습을 찍은 youtube의 운동 영상에 mediapipe pose를 적용시켜서 keypoint가 어떻게 변하는지 눈으로 관찰했습니다.
* 가장 크게 변화를 보이는 keypoint의 변수값을 따로 print해서 다시 한번 관찰했습니다.
* 옆모습을 기준으로 카운팅을 하기 위한 크게 4가지의 운동 알고리즘을 구현했습니다.
  - 인접한 keypoint들 간의 각도를 출력해주는 각도 계산 알고리즘
  - 사용자가 현재 왼쪽 옆모습인지 오른쪽 옆모습인지 확인하는 방향 확인 알고리즘
  - 각 운동 보조에 필요한 사용자의 keypoint가 카메라에 보이고 주요 keypoint들 간의 각도 값에 따른 상태를 확인하는 준비 확인 알고리즘
  - 이전에 확인한 가장 크게 변화를 보이는 keypoint를 이용한 카운팅 알고리즘
* 각도 계산 알고리즘
  - keypoint의 x, y, z 좌표 변수들을 이용했습니다.
  - 인접한 keypoint들 간의 각도를 두 벡터의 사이각 공식으로 구하여 값을 리턴합니다.

<img src="https://github.com/mooncw/healthweb/assets/97713997/81c6807e-c078-4dd4-a618-77b4e3ed6ece" width="45%" height="45%">

<br>
<br>

* 방향 확인 알고리즘
  - 카메라와 keypoint 간의 거리를 나타내는 z 변수를 이용했습니다.
  - 좌측 어깨 끝이 더 가까우면 left, 우측 어깨 끝이 더 가까우면 right를 리턴합니다.
 
<img src="https://github.com/mooncw/healthweb/assets/97713997/5083b962-a3e8-4f00-b437-179acead1fdc" width="32%" height="32%">

<br>
<br>

* 준비 확인 알고리즘
  - 가시성을 나타내는 visibility 변수를 이용했습니다.
  - 방향에 따라 운동 보조에 필요한 keypoint가 가시성 상태와 주요 keypoint들 간의 각도 상태에 따라 준비 상태를 리턴합니다.

<img src="https://github.com/mooncw/healthweb/assets/97713997/c9bb5f79-3632-44f5-be5f-552e3283e05f" width="51%" height="51%">

<br>
<br>

* 카운팅 알고리즘
  - 각 운동에 가장 크게 변하는 keypoint들 간의 각도를 이용했습니다.
  - 각도가 일정 이상이 되면 up, 이하가되면 down이 되는 status 변수를 만들었습니다.
  - status 변수를 이용하여 down에서 up에 되면 카운트 1 오르게 했습니다.

<img src="https://github.com/mooncw/healthweb/assets/97713997/540606fe-f650-4502-8fca-43dd95bd5435" width="20%" height="20%">
<br>
<img src="https://github.com/mooncw/healthweb/assets/97713997/8ec858c2-5f87-480e-bf91-31a1795cd247" width="52%" height="52%">

<br>
<br>

### 7. 배포
* 로컬에서 만든 것을 깃허브에 올리고 AWS EC2에서 git clone하여 1차 배포했습니다.
* Django는 웹서버와 직접 통신할 수 없기 때문에 중간다리로 uWSGI python 패키지를 설치하여 Django와 연결했습니다.
* 웹서버 애플리케이션인 nginx를 설치하여 uWSGI와 연결했습니다.
* uwsgi.service 파일을 만들어 uWSGI를 백그라운드에서 실행이 되도록하여 2차 배포했습니다.
* 가비아에서 도메인을 구입하고 AWS Route 53을 통해 구매한 도메인과 EC2 인스턴스을 연결하여 최종 배포했습니다.
* 이 후, 개선한 부분이 있을 때마다 재배포했습니다.

<br>

## 주소 (현재 비용 문제로 중단)
- http://myhealthweb.site
- 웹캠 기능은 다음 과정을 거친 후 사용가능합니다.
  - 크롬 주소창에 chrome://flags을 입력합니다.
  - 상단 search 입력란에 Insecure origins treated as secure을 입력합니다.
  - Insecure origins treated as secure 아래에 `http://myhealthweb.site`을 입력하고 Disabled를 Enabled로 바꿔줍니다.

<br>

## 2022/12/23 최종 배포 후 추가 개선
* 서버가 1코어 1기가램이라 Django에서 mediapipe pose 모델을 적용시킨 웹캠이 프레임 드랍이 심해서 카운팅을 위한 알고리즘, 모델 사용을 CSR로 처리하여 개선
* sqlite3에서 mysql로 DB 교체
* html 구조 개선

<br>

## 웹 시연 영상

https://github.com/mooncw/healthweb/assets/97713997/faa69803-df4e-4c58-afde-38bab7707a30

<br>


<br>

## 폴더 및 파일 설명
- **health** : django 프로젝트 폴더
- **requirements.txt** : 설치한 패키지들의 정보가 들어있는 파일

<br>

## 만족스러웠던 부분
- 웹캠 화면에 keypoint detection 모델을 적용시켰습니다.
- 제가 만든 웹앱을 배포해보았습니다.
- keypoint detection 모델을 적용시킨 웹캠 화면의 심한 프레임 드랍을 SSR에서 CSR로 바꿔서 개선했습니다.
- 데이터가 2개뿐이지만 Django에서 DB를 이용해봤습니다.

<br>

## 개선사항
- 더 좋은 서비스를 하려면 운동 종류 늘릴 필요가 있고 자세 확인, 카운팅 음성, 알림 등과 같은 추가적인 기능이 필요하다고 생각합니다.
- 좀 더 정확한 카운팅 알고리즘이 필요하다고 생각합니다.
- sqlite는 단일 스레드로 동작하기 때문에 병렬 처리가 힘들어서 사용자가 많아지면 sqlite보다 mysql같은 것을 써야한다고 생각합니다.
- https를 적용한다면 웹캠 기능을 사용하기 위한 번거로운 작업을 할 필요가 없어질 것이라 생각합니다.
