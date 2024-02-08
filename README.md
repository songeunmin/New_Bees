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
&emsp;&ensp;Ⅰ. 주제선정</br>&emsp;&ensp;Ⅱ. 데이터 탐색 및 이미지 전처리</br>&emsp;&ensp;Ⅲ. 모델링</br>&emsp;&ensp;Ⅳ. 학습결과</br>&emsp;&ensp;Ⅴ. 웹 서비스 구현</br>&emsp;&ensp;Ⅵ. 개선사항</br>&emsp;&ensp;Ⅶ. 자료출처</br>

## Ⅰ. 주제선정
* 선정 과정</br>
  **1. 최근 교통사고 사망 사고 원인 별 조사**</br>
       &nbsp;&nbsp;&nbsp; 1)졸음 및 주시 태만이 67.6%로 가장 높은 것으로 기록</br>
  **2. AI 및 센서 기술**</br>
       &nbsp;&nbsp;&nbsp; 1) 운전자의 부주의를 감지하여 주의를 주는 모니터링 시스템들이 개발 중</br>
  **3. 자료출처**</br>
       &nbsp;&nbsp;&nbsp; 1) 서울경제 https://www.sedaily.com/NewsView/29RZKXMF51.htm</br>
       &nbsp;&nbsp;&nbsp; 2) (주)필라스크리에이션 https://thepoc.co.kr/58/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=7008773&t=board.htm

## 2. 데이터 탐색 및 이미지 전처리
* 전처리 과정</br>
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
