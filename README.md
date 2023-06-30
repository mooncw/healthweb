# healthweb
keypoint detection 모델을 이용한 운동 보조 웹 애플리케이션 (2022/12/05 ~ 2022/12/23)

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
- 우선 django와 html 틀을 만들고 살을 붙이는 방향으로 진행했습니다.
- keypoint detection 모델로 정확도가 좋은 mediapipe pose 모델를 선택했습니다.
- 데이터 탐색 후 보조하고자 하는 운동로 맨몸 운동인 푸쉬업과 스쿼트를 선택했습니다.
- 유튜브 운동 영상에 mediapipe pose를 적용시켜 알고리즘에 사용할 변수들을 관찰했습니다.
- 관찰을 통해 각도 계산, 방향 확인, 준비 상태 확인, 카운팅 알고리즘을 구현했습니다.
- 푸쉬업과 스쿼트 각각 테스트 후 개선이 필요한 부분을 수정했습니다.
- 깃허브를 통해 AWS EC2로 1차 배포했습니다.
- Django는 웹 서버와 직접 통신할 수 없기 때문에 중간다리로 uWSGI라는 python 패키지를 설치하여 Django와 연결했습니다.
- 웹 서버 애플리케이션인 nginx를 설치하여 uWSGI와 연결했습니다.
- uwsgi.service 파일을 만들어 uWSGI를 백그라운드에서 실행이 되도록 하여 2차 배포했습니다.
- 가비아에서 도메인을 구입하고 AWS Route 53을 통해 EC2 인스턴스와 연결하여 http로 최종 배포했습니다.

<br>

## 최종 배포 후 추가 개선
- Django에서 mediapipe pose 모델을 적용시킨 웹캠이 프레임 드랍이 심해서 알고리즘, 모델 사용, 웹캠 사용을 python 대신 js로 사용하여 개선.
- 부트스트랩을 이용하여 프론트엔드 보충했습니다.
- sqlite로 보조할 운동에 대한 데이터가 들어있는 DB를 구축했습니다.

<br>

## 웹설명
- 첫 화면에 운동 종류를 선택할 수 있습니다.
- 선택 후에 다른 화면으로 이동하고 웹캠이 나옵니다.
- 상단에 운동 종류와 주의사항이 나와있습니다.
- 그 밑에 웹캠이 나오는 박스와 카운팅 숫자가 나오는 박스가 있습니다.
- 푸쉬업과 스쿼트 모두 올라올 때 카운팅을 합니다.(현재는 카운팅만 구현되어있습니다.)
- 웹캠 박스 밑에 카운팅 초기화 버튼이 있습니다.
- 상단에 Home 버튼을 누르면 첫 화면으로 돌아갑니다.

<br>

**- 홈 화면**

<br>

![firstscreen](https://github.com/mooncw/healthweb/assets/97713997/62bdf80c-99c4-437f-a72d-4ba00c7ee850)

<br>

**- 선택 후 화면**

<br>

![pushup](https://github.com/mooncw/healthweb/assets/97713997/bbb21c92-67f8-45c4-9a87-036d2e86a0a7)

<br>


## 웹 시연 영상

https://github.com/mooncw/healthweb/assets/97713997/faa69803-df4e-4c58-afde-38bab7707a30

<br>

## 주소 (2023.07.07 이후 중단 예정)
- http://myhealthweb.site
- 웹캠 기능은 다음 과정을 거친 후 사용가능합니다.
  - 크롬 주소창에 chrome://flags을 입력합니다.
  - 상단 search 입력란에 Insecure origins treated as secure을 입력합니다.
  - Insecure origins treated as secure 아래에 `http://myhealthweb.site`을 입력하고 Disabled를 Enabled로 바꿔줍니다.

<br>

## 폴더 및 파일 설명
- **health** : django 프로젝트 폴더
- **requirements.txt** : 설치한 패키지들의 정보가 들어있는 파일

<br>

## 만족스러웠던 부분
- 웹캠 화면에 keypoint detection 모델을 적용시켰습니다.
- 제가 만든 웹앱을 배포해보았습니다.
- keypoint detection 모델을 적용시킨 웹캠 화면의 심한 프레임 드랍을 개선했습니다.
- 데이터가 2개뿐이지만 Django에서 DB를 이용해봤습니다.

<br>

## 개선사항
- 더 좋은 서비스를 하려면 운동 종류 늘릴 필요가 있고 자세 확인, 카운팅 음성, 알림 등과 같은 추가적인 기능이 필요하다고 생각합니다.
- 좀 더 정확한 카운팅 알고리즘이 필요하다고 생각합니다.
- sqlite는 단일 스레드로 동작하기 때문에 병렬 처리가 힘들어서 사용자가 많아지면 sqlite보다 mysql같은 것을 써야한다고 생각합니다.
- https를 적용한다면 웹캠 기능을 사용하기 위한 번거로운 작업을 할 필요가 없어질 것이라 생각합니다.
