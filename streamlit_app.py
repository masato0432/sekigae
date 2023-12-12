python
import streamlit as st
import numpy as np

# アプリケーションのタイトル
st.title('席替えアプリ')

# 開始ボタン
if st.button('開始'):
    # 7行6列の席を表す配列を作成し、1から41の数字をランダムに割り当てる
    seats = np.arange(1, 42).reshape(7, 6)
    np.random.shuffle(seats)

    # 結果の表示
    st.write(seats)