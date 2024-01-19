import streamlit as st
import pandas as pd
from datetime import datetime

# 初期化
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = pd.DataFrame(columns=['Task', 'Deadline', 'Priority', 'Category'])

# タスクの追加機能
def add_task():
    with st.sidebar:
        st.header("Add New Task")
        task = st.text_input('Task', key='new_task')
        deadline = st.date_input('Deadline', key='new_deadline')
        priority = st.selectbox('Priority', ['高', '中', '低'], key='new_priority')
        category = st.text_input('Category', key='new_category')
        if st.button('Add Task'):
            new_task = pd.DataFrame([[task, deadline, priority, category]], columns=['Task', 'Deadline', 'Priority', 'Category'])
            st.session_state['tasks'] = pd.concat([st.session_state['tasks'], new_task], ignore_index=True)

# タスクの編集と削除機能
def edit_and_delete_tasks():
    for i in range(len(st.session_state['tasks'])):
        with st.expander(f"Task {i + 1}"):
            row = st.session_state['tasks'].iloc[i]
            edited_task = st.text_input('Task', value=row['Task'], key=f'task_{i}')
            edited_deadline = st.date_input('Deadline', value=row['Deadline'], key=f'deadline_{i}')
            edited_priority = st.selectbox('Priority', ['高', '中', '低'], index=['高', '中', '低'].index(row['Priority']), key=f'priority_{i}')
            edited_category = st.text_input('Category', value=row['Category'], key=f'category_{i}')

            if st.button('Save Changes', key=f'save_{i}'):
                st.session_state['tasks'].iloc[i] = [edited_task, edited_deadline, edited_priority, edited_category]
            
            if st.button('Delete Task', key=f'delete_{i}'):
                st.session_state['tasks'] = st.session_state['tasks'].drop(st.session_state['tasks'].index[i])
                st.experimental_rerun()

# タスクの表示機能
def display_tasks():
    st.header("Your Tasks")
    st.dataframe(st.session_state['tasks'])

# メイン関数
def main():
    st.title("Task Manager App")
    add_task()
    display_tasks()
    edit_and_delete_tasks()

# スクリプトとして実行された場合にのみmain()を実行
if __name__ == '__main__':
    main()
