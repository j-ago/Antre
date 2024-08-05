import streamlit as st
import openai
import pandas as pd

# OpenAI APIキーを設定
if st.checkbox("Enter your OpenAI API key"):
    openai.api_key = st.text_input("OpenAI API Key", type="password")

# エクセルファイルの読み込み
def load_excel(file):
    return pd.read_excel(file)

# ChatGPT-4oにクエリを送信する関数
def query_chatgpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",  # ChatGPT-4o
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        n=1,
        temperature=0.7
    )
    return response.choices[0].message['content'].strip()

# Streamlitアプリケーションの設定
st.title("アントレ様 ChatGPT-4o サンプル")

# エクセルファイルのアップロード
uploaded_file = "Antre_Marketing_Campaigns.xlsx"

# ユーザーからの質問を入力
user_question = st.text_area("ここに聞きたいキャンペーンを入れてください。（例：過去成功したオンライン施策を教えて）:")

# 質問の送信ボタン
if st.button("送信"):
    if uploaded_file is not None and user_question:
        # エクセルファイルを読み込む
        data = load_excel(uploaded_file)
        
        # エクセルデータをテキストに変換
        data_text = data.to_string(index=False)
        
        # ChatGPTに送信するプロンプトを作成
        prompt = f"以下のデータを基にして、次の質問に答えてください：\n\n{data_text}\n\n質問: {user_question}"
        
        # ChatGPT-4oにクエリを送信し、回答を取得
        answer = query_chatgpt(prompt)
        
        # 回答を表示
        st.write("Answer:", answer)
    else:
        st.error("Please upload an Excel file and enter a question.")

# カスタムCSSを追加
def add_custom_css():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f0f0f5;
            color: #333333;
        }
        .stTextInput, .stTextArea, .stFileUploader, .stButton, .stCheckbox {
            border-radius: 10px;
            padding: 10px;
            margin: 10px 0;
            font-size: 16px;
            background-color: #ffffff;
            border: 2px solid #ff6f61;
        }
        .stButton>button {
            background-color: #ff6f61;
            color: white;
            font-weight: bold;
            border: none;
        }
        .stButton>button:hover {
            background-color: #ff856c;
            color: white;
        }
        .stCheckbox>div {
            background-color: #ff6f61;
            color: white;
            font-weight: bold;
        }
        .stTitle {
            color: #ff6f61;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# カスタムCSSを適用
add_custom_css()

