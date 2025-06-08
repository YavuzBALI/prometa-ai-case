import json
import os
import sys
import time

import requests
import streamlit as st
from streamlit_autorefresh import st_autorefresh

parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from config import config

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "unique_id" not in st.session_state:
    st.session_state.unique_id = None

if "length_message" not in st.session_state:
    st.session_state.length_message = 0

if "timeout" not in st.session_state:
    st.session_state.timeout = 0

st.set_page_config(page_title="Chat-Style JSON Görüntüleme", layout="wide")
st.title("Analyze of Chat")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fira+Code&family=Quicksand:wght@500&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background-color: #2e2e2e;
    color: #ffffff;
}
.message-box {
    background-color: #444;
    padding: 14px 18px;
    margin-bottom: 12px;
    border-radius: 12px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.3);
    font-family: 'Fira Code', monospace;
    font-size: 14px;
    color: #e0e0e0;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    with st.form("upload_form"):
        uploaded_file = st.file_uploader("Upload the Chat Data (JSON File)", type="json")
        submitted = st.form_submit_button("Send")
    if submitted and uploaded_file:
        json_data = json.load(uploaded_file)
        response = requests.post(config.intent_service.url + config.intent_service.post_service, json=json_data)
        st.session_state.unique_id = response.json()
        if response.status_code == 200:
            st.success("The Document Has Been Uploaded")
            st.session_state.submitted = True
            st.session_state.timeout = 0
        else:
            st.error("The Document Has Not Been Uploaded")
            st.session_state.submitted = False

if st.session_state.submitted:
    response = requests.get(config.log_service.url + config.log_service.get_service,
                            params={"unique_id": st.session_state.unique_id})
    if response.status_code == 200:
        result = response.json()
        message_dict = {"content": "START"}
        for i, message_dict in enumerate(result):
            if message_dict['speaker'] == "agent":
                st.markdown(f"""
                    <div class='message-box'>
                        <b style='color:blue;'>AGENT</b><br>
                        <span style='color:red;'>Content:</span> {message_dict['content']}<br>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class='message-box'>
                        <b style='color:yellow;'>CUSTOMER</b><br>
                        <span style='color:red;'>Content:</span> {message_dict['content']}<br>
                        <span style='color:red;'>Intent:</span> {message_dict['intent']}<br>
                        <span style='color:red;'>Segment:</span> {message_dict['segment']}
                    </div>
                """, unsafe_allow_html=True)

            if st.session_state.length_message < i:
                time.sleep(0.1)

        if len(result) != st.session_state.length_message:
            st.session_state.length_message = len(result)

        if ('END' in message_dict["content"]) or (st.session_state.timeout > 120):
            st.session_state.submitted = False
            uploaded_file = None
        else:
            st.session_state.timeout = st.session_state.timeout + 1
            st_autorefresh(interval=3000, key="auto")
    else:
        st.markdown(f"<div class='message-box'>Request False</div>", unsafe_allow_html=True)
        st.session_state.timeout = st.session_state.timeout + 1
        st_autorefresh(interval=3000, key="auto")
