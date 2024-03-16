# 🤖 Deep running project</br>Driver inattentive object detection using YOLOv8
## 👥 Team
- Team name : 🐝 New bees (뉴비즈)
- Team members : 조서현, 윤성진, 함은규, 송은민
## :books: skill
- Programming <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
- Framework <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white"> <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=OpenCV&logoColor=white"> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white">
- Tools <img src="https://img.shields.io/badge/jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white"> <img src="https://img.shields.io/badge/visualstudiocode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white">
- Git <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=jupyter&logoColor=white"> <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">

## **Project's Purpose**
 **1. Putpose:** Save the driver from the accident by abnormal behaviors ; being sleepy, smoke, phone call etc.   
 
 **2. By what:** The notification will appear when the driver do abnormal behaviors during drive.   
 
 **3. Basic concept**   
&nbsp;&nbsp;&nbsp; 1) Classify driver's  abnormal behaviors.   
&nbsp;&nbsp;&nbsp; 2) Classify whether driver get sleepy.   
&nbsp;&nbsp;&nbsp; 3) Classify authorized driver's face identification.   
 
 **4. Role game (Project's for)**   
&nbsp;&nbsp;&nbsp; 1) 🚙+🏢 The manager who magaging the company's car.    
&nbsp;&nbsp;&nbsp; 2) 🚙+💳 The rental car company owner who borrow the car to people.    
&nbsp;&nbsp;&nbsp; 3) 🚖+👤:ma The taxi company owner who incruit new man who has no information for.   

## 목차(INDEX)
&emsp;&ensp;Ⅰ. 주제선정</br>&emsp;&ensp;Ⅱ. 데이터 탐색 및 이미지 전처리</br>&emsp;&ensp;Ⅲ. 모델링</br>&emsp;&ensp;Ⅳ. 학습결과 및 Streamlit 구현</br>&emsp;&ensp;Ⅴ. 개선사항</br>&emsp;&ensp;Ⅵ. 참고자료

## Ⅰ. 주제선정
  **1. 최근 교통사고 사망 사고 원인 별 조사**</br>
       &nbsp;&nbsp;&nbsp; 1)졸음 및 주시 태만이 67.6%로 가장 높은 것으로 기록</br>
  **2. AI 및 센서 기술**</br>
       &nbsp;&nbsp;&nbsp; 1) 운전자의 부주의를 감지하여 주의를 주는 모니터링 시스템들이 개발 중</br>
  **3. 자료출처**</br>
       &nbsp;&nbsp;&nbsp; 1) 서울경제 https://www.sedaily.com/NewsView/29RZKXMF51.htm</br>
       &nbsp;&nbsp;&nbsp; 2) (주)필라스크리에이션 https://thepoc.co.kr/58/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=7008773&t=board.htm

## Ⅱ. 데이터 탐색 및 이미지 전처리
  **1. Dataset : AIHub "운전 사고 예방을 위한 운전자 부주의 행동 검출 모델"** </br>
       &nbsp;&nbsp;&nbsp; 1) 출처 : https://aihub.or.kr/aihubdata/data/view.do?currMenu=120&topMenu=100&aihubDataSe=extrldata&dataSetSn=448.htm</br>
       &nbsp;&nbsp;&nbsp; 2) 7종의 운전자 얼굴 객체를 탐지 및 분류</br>
       &nbsp;&nbsp;&nbsp; 3) Class : Face, Eye-opened, Eye-closed, Mouth-opened, Mouth-closed, Cigar, Phone</br>
       &nbsp;&nbsp;&nbsp; 4) Train - Images,labels , Valid - Images,labels</br>
  **2. 주요 전처리**</br>
       &nbsp;&nbsp;&nbsp; 1) Cigar, Phone의 이미지가 다른 Class보다 상대적으로 너무 적음</br>
       &nbsp;&nbsp;&nbsp; 2) Cigar, Phone을 제외한 이미지 랜덤으로 1/2 삭제하는 과정 2번을 거침</br>
       &nbsp;&nbsp;&nbsp; 3) YOLO 모델을 학습시키기 위해 Json으로 구성되어 있는 labels를 txt로 변경</br>
       &nbsp;&nbsp;&nbsp; 4) 서로 일치하는 Images & Label Copy

## Ⅲ. 모델링
  **1. 모델선정 : YOLOv8n** </br>
       &nbsp;&nbsp;&nbsp; 1) 객체 검출 모델 중 가장 우수함</br>
  **2. 모델링 과정**</br>
       &nbsp;&nbsp;&nbsp; 1) Install ultralytics</br>
       &nbsp;&nbsp;&nbsp; 2) Yaml파일 경로 설정 및 Class 설정</br>
       &nbsp;&nbsp;&nbsp; 3) YOLOv8n을 학습 (epoch=20, batch=51, optimizer="AdamW")</br>
       &nbsp;&nbsp;&nbsp; 4) 작업 경로 runs 파일 자동생성 후 결과 저장

## Ⅳ. 학습결과 및 Streamlit 구현
  **1. 학습결과** </br>
       &nbsp;&nbsp;&nbsp; 1) batch images 및 시각화</br>
  **2. Streamlit 구현**</br>
       &nbsp;&nbsp;&nbsp; 1) Install Streamlit</br>
       &nbsp;&nbsp;&nbsp; 2) Python 스크립트 파일로 변환</br>
       &nbsp;&nbsp;&nbsp; 3) 실행 후 Streamlit Test</br>
       &nbsp;&nbsp;&nbsp; 4) 배포

## Ⅴ. 개선사항
  **1. 아두이노, 라즈베리파이를 사용해 제품화** </br>
  **2. Cigar, Phone 데이터를 증가시켜 더 좋은 성능 유도**</br>
       &nbsp;&nbsp;&nbsp; 1) 더 많은 Cigar, Phone 이미지 라벨링 후 데이터셋에 추가해 모델 성능 향상 </br>
       &nbsp;&nbsp;&nbsp; 2) Object Cut-Mix 기법을 사용해 모델 성능 향상</br>
  **3. 다양한 시도**</br>
       &nbsp;&nbsp;&nbsp; 1) 운전자 안면 인식 기술 추가 : 구현은 했으나, streamlit에 적용하지 못함</br>
       &nbsp;&nbsp;&nbsp; 2) 운전자 부주의 검출 시 옵션 추가

## Ⅵ. 참고자료
  **1. 조재익, 이성주, 정호기, 박강령, 김재희 "Vision-based method for detecting driver drowsiness and distraction in driver monitoring system" SPIE, 2011** </br>
  **2. Ultralytics YOLOv8 문서**</br>
       &nbsp;&nbsp;&nbsp; 1) https://docs.ultralytics.com/ko.htm</br>
  **3. 이민혜,강선경,신성윤, 임순자, "안면인식 기술을 활용한 차량 시동 제어 시스템" 원광대학교, 군산대학교, 학국정보통신학회, p425-426, 2021**</br>


# 🕴️ Thanks.
