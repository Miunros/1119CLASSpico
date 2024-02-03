import streamlit as st
import pandas as pd
import requests

#st.write('Hello, Nancy :sunglasses:')
#st.caption('我是許乃心')
st.title('群輝商務科技的雞舍')
st.header(':blue[pico專案1] :red[溫度] :violet[濕度]',divider='rainbow')
#st.snow()
st.balloons()

url='https://blynk.cloud/external/api/get?token=OjsaRz73dEbe7wlmUomfBRB38u8kSMj6&v1&v0'

req = requests.request('GET',url)
if req.status_code ==200:
    all_data = req.json()
    st.info(f'光線:{all_data["v0"]}', icon="ℹ️")
    st.info(f'可變電阻:{all_data["v1"]}', icon="ℹ️")
else:
    st.warning('連線失敗! 請重新測試~~~', icon="⚠️")