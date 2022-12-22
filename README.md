# healthweb

## 프로젝트 기간: 2022/12/05 ~ 2022/12/09

### 프로젝트 개요
홈트가 유행하고 있는 지금 시대에 keypoint detection을 활용한 홈트 보조를 위한 웹 서비스를 만들고자 함

### 진행상황
프론트 엔드 보충

### 폴더 및 파일 설명
장고 프로젝트인 health 폴더

웹을 실행하기 위해 필요한 설치 라이브러리들 requirements.txt

### 사용모델
mediapipe pose

### 진행 과정
1. 사용하려는 것들을 검토하면서 틀을 만들면서 기획
2. 유튜브 자세 영상 참고
3. 유튜브 자세 영상에 알고리즘으로 사용할 변수들이 어떻게 변하는지 확인
4. 시간상 푸쉬업 알고리즘만 구현
5. 배포할 초기 단계 완성
6. aws ec2로 1차 배포
7. 도메인과 https까지 적용 완료
8. js로 카메라와 모델 연결
9. 스쿼트 알고리즘 추가
10. 부트스트랩을 이용하여 프론트엔드 보충

### 웹설명
첫 화면에 운동 종류를 선택할 수 있습니다.

선택 후에 다른 화면으로 이동하고 웹캠이 나옵니다.

웹캠 왼쪽에 운동 종류와 카운팅 숫자가 나옵니다.

지금 구현한 푸쉬업과 스쿼트는 잘 동작하기 위해선 전신이 웹캠에 나와야하고 카메라 위차는 옆에서 바라보는 방향에 있어야합니다.

둘 다 올라올 때 카운팅을 합니다.

### 주소(현재 중지)
https://myhealthweb.site

### 한계 및 보완점
1. 더 좋은 서비스를 하려면 운동 종류 늘릴 필요가 있고 알고리즘 개선이 필요함
2. html을 꾸밀 프론트엔드 기술이 필요함
3. etc..
