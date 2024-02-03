import streamlit as st
import pandas as pd
import time
import requests
from streamlit_autorefresh import st_autorefresh

#st.write('Hello, Nancy :sunglasses:')
#st.caption('我是許乃心')
st.title('群輝商務科技的雞舍')
st.header(':blue[pico專案1] :red[溫度] :violet[濕度]',divider='rainbow')
#st.snow()
st.balloons()
count = st_autorefresh(interval=5000, limit=100, key="fizzbuzzcounter")
#with st.spinner('Wait for it...'):
#    time.sleep(3)
#st.success('Done!')

url='https://blynk.cloud/external/api/get?token=OjsaRz73dEbe7wlmUomfBRB38u8kSMj6&v1&v0'

req = requests.request('GET',url)
if req.status_code ==200:
    all_data = req.json()
    col1, col2= st.columns(2)
    col1.metric("光線", f'{all_data["v0"]}')
    col2.metric("可變電阻", f'{all_data["v1"]}')
else:
    st.warning('連線失敗! 請重新測試~~~', icon="⚠️")

