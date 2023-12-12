import streamlit as st
import numpy as np

# アプリケーションのタイトル
st.title('席替えアプリ')

# 開始ボタン
if st.button('開始'):
    # 1から41の数字をランダムに並べ替えて、7行6列の席に割り当てる
    seats = np.random.choice(np.arange(1, 42), size=(7, 6), replace=False)

    # 結果の表示
    st.write(seats)