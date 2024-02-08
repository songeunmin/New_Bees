from pathlib import Path
import streamlit as st
import config  
from utils import load_model, infer_uploaded_image, infer_uploaded_video, infer_uploaded_webcam, model_load
from datetime import datetime



# setting page layout
st.set_page_config(
    page_title="뉴비즈",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto"
    )

st.sidebar.header("반가워요~ 🎉")

# 현재 날짜와 시간 가져오기
current_datetime = datetime.now()
selected_time = current_datetime.time()
# 사이드바에 현재 날짜와 시간으로 초기화된 날짜 입력 추가

st.sidebar.write("**오늘의 날짜는** :",current_datetime.strftime('%Y-%m-%d'))

# model optionsst
task_type = st.sidebar.selectbox(
    "**목적**",
    ["Detection"]
)

model_type = None
if task_type == "Detection":
    model_type = st.sidebar.selectbox(
        "**모델을 선택 하세요**",
        config.DETECTION_MODEL_LIST
    )
else:
    st.error("Currently only 'Detection' function is implemented")

confidence = float(st.sidebar.slider(
    ":blue[*임계값 설정*]", 30, 100, 50)) / 100


model_path = ""
if model_type:
    model_path = Path(config.DETECTION_MODEL_DIR, str(model_type))
else:
    st.error("Please Select Model in Sidebar")

# load pretrained DL model
try:
    model = load_model(model_path) or model_load(model_path) 

except Exception as e:
    st.error(f"Unable to load model. Please check the specified path: {model_path}")

# image/video options
st.sidebar.header(":red[*실시간 영상*], :red[*동영상*], :red[*사진*] 모두 가능해요!")
source_selectbox = st.sidebar.selectbox(
    "Select Source",
    config.SOURCES_LIST
)

st.title("운전자 행동 분석")
st.divider()
st.subheader("운전자의 행동을 자사의 :blue[*`안전 메뉴얼`*]과 대조합니다.")

st.success("안전한 운전을 하는 당신이 아름답습니다.",icon ="✅")

source_img = None
if source_selectbox == config.SOURCES_LIST[0]: # Image
    infer_uploaded_image(confidence, model)
elif source_selectbox == config.SOURCES_LIST[1]: # Video
    infer_uploaded_video(confidence, model)
elif source_selectbox == config.SOURCES_LIST[2]: # Webcam
    infer_uploaded_webcam(confidence, model)
    
else:
    st.error("웹캠의 경로를 확인하세요")

st.divider()



