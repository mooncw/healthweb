# healthweb
<svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>Django</title><path d="M11.146 0h3.924v18.166c-2.013.382-3.491.535-5.096.535-4.791 0-7.288-2.166-7.288-6.32 0-4.002 2.65-6.6 6.753-6.6.637 0 1.121.05 1.707.203zm0 9.143a3.894 3.894 0 00-1.325-.204c-1.988 0-3.134 1.223-3.134 3.365 0 2.09 1.096 3.236 3.109 3.236.433 0 .79-.025 1.35-.102V9.142zM21.314 6.06v9.098c0 3.134-.229 4.638-.917 5.937-.637 1.249-1.478 2.039-3.211 2.905l-3.644-1.733c1.733-.815 2.574-1.53 3.109-2.625.561-1.121.739-2.421.739-5.835V6.059h3.924zM17.39.021h3.924v4.026H17.39z"/></svg>
## 프로젝트 기간: 2022/12/05 ~ 2022/12/23

### 프로젝트 개요
홈트가 유행하고 있는 지금 시대에 keypoint detection을 활용한 홈트 보조를 위한 웹 서비스를 만들고자 함

### 진행상황
프론트 엔드 보충

### 폴더 및 파일 설명
장고 프로젝트인 health 폴더

웹을 실행하기 위해 필요한 설치 라이브러리들 requirements.txt

### 사용 keypoint detection 모델
mediapipe pose(https://google.github.io/mediapipe/solutions/pose.html)

### 진행 과정
1. 사용하려는 것들을 검토하면서 틀을 만들면서 기획
2. 유튜브 자세 영상 참고
3. 유튜브 자세 영상에 알고리즘으로 사용할 변수들이 어떻게 변하는지 관찰
4. 관찰을 통해 간단한 푸쉬업 알고리즘만 구현
5. 푸쉬업 알고리즘 테스트 후 간단한 조정
6. 배포할 초기 단계 완성
7. aws ec2로 1차 배포
8. 도메인과 https까지 적용 완료
9. python으론 웹앱에서의 웹캠 서비스가 효과적이지 않은 것 같아 푸쉬업 알고리즘, 모델 사용, 웹캠 사용을 python 대신 js로 사용함
10. 간단한 스쿼트 알고리즘 추가하고 테스트 후 간단한 조정
11. 부트스트랩을 이용하여 프론트엔드 보충

### 웹설명
첫 화면에 운동 종류를 선택할 수 있습니다.

선택 후에 다른 화면으로 이동하고 웹캠이 나옵니다.

상단에 운동 종류와 주의사항이 나와있습니다.

그 밑에 웹캠이 나오는 박스와 카운팅 숫자가 나오는 박스가 있습니다.

둘 다 올라올 때 카운팅을 합니다.

### 주소(현재 )
https://myhealthweb.site

### 한계 및 보완점
1. 더 좋은 서비스를 하려면 운동 종류 늘릴 필요가 있고 필요한 자세 확인이나 카운팅 음성과 같은 필요한 기능이 더 있다고 생각하고 알고리즘 개선도 필요하다고 생각합니다.
2. 운동 종류를 늘린다면 DB를 쓰는 게 좋아보임 (DB 컬럼 ex. id, 큰 범위 운동 종류, 작은 범위 운동 종류, 자극 근육 부위, 카메라 방향, ...)
3. 카운팅 될 때마다 해당하는 숫자를 말해주는 카운팅 음성 기능이 있으면 더 좋다고 생각합니다.
4. 한 세트가 끝나면 휴식시간을 재주는 타이머 기능이 있으면 더 좋다고 생각합니다.
5. html을 더 잘 꾸밀 프론트엔드 기술이 필요합니다.
6. 카메라를 동작시키는데 조금 오래 걸립니다.
7. etc..
