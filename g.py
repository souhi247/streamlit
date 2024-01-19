import streamlit as st
import pandas as pd
from datetime import datetime

# 初期化
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = pd.DataFrame(columns=['タスク', '期限', '優先度', 'カテゴリ'])

# タスクを追加する関数
def add_task():
    with st.sidebar:
        st.header("新しいタスクを追加:heavy_plus_sign:")
        task = st.text_input('タスク')
        deadline = st.date_input('期限')
        priority = st.selectbox('優先度', ['高', '中', '低'])
        category = st.text_input('カテゴリ')
        if st.button('追加'):
            new_task = pd.DataFrame([[task, deadline, priority, category]], columns=['タスク', '期限', '優先度', 'カテゴリ'])
            st.session_state['tasks'] = pd.concat([st.session_state['tasks'], new_task], ignore_index=True)

# タスクを表示する関数
def display_tasks():
    st.subheader("タスク一覧:scroll:")
    sort_by = st.selectbox('並び順', ['期限', '優先度', 'カテゴリ'])
    sorted_tasks = st.session_state['tasks'].sort_values(by=[sort_by])
    edited_df = st.data_editor(sorted_tasks, num_rows="dynamic", disabled=("col1"), width=704)

# メイン関数
def main():
    st.title("タスク管理ツール:white_check_mark:")
    add_task()
    display_tasks()

# スクリプトとして実行された場合にのみmain()を実行
if __name__ == '__main__':
    main()
