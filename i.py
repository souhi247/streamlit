import streamlit as st
import pandas as pd
from datetime import datetime

# タスクを保存するためのデータフレームを初期化
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = pd.DataFrame(columns=['Task', 'Deadline', 'Priority', 'Category'])

# タスクを追加する関数
def add_task():
    with st.expander("タスクを追加する"):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            task = st.text_input('Task', key='task')
        with col2:
            deadline = st.date_input('Deadline', key='deadline')
        with col3:
            priority = st.selectbox('Priority', ['High', 'Medium', 'Low'], key='priority')
        with col4:
            category = st.text_input('Category', key='category')
        if st.button('追加'):
            new_task = pd.DataFrame([[task, deadline, priority, category]], columns=['Task', 'Deadline', 'Priority', 'Category'])
            st.session_state['tasks'] = pd.concat([st.session_state['tasks'], new_task], ignore_index=True)        

# タスクを編集する関数
def edit_task(index):
    task_key = f'task_{index}'
    category_key = f'category_{index}'
    deadline_key = f'deadline_{index}'
    priority_key = f'priority_{index}'
    st.session_state['tasks'].loc[index, 'Task'] = st.text_input('Edit Task', st.session_state['tasks'].loc[index, 'Task'], key=task_key)
    st.session_state['tasks'].loc[index, 'Deadline'] = st.date_input('Edit Deadline', st.session_state['tasks'].loc[index, 'Deadline'], key=deadline_key)
    priority_options = ['High', 'Medium', 'Low']
    current_priority = st.session_state['tasks'].loc[index, 'Priority']
    priority_index = priority_options.index(current_priority) if current_priority in priority_options else 0
    st.session_state['tasks'].loc[index, 'Priority'] = st.selectbox('Edit Priority', priority_options, index=priority_index, key=priority_key)
    st.session_state['tasks'].loc[index, 'Category'] = st.text_input('Edit Category', st.session_state['tasks'].loc[index, 'Category'], key=category_key)
    if st.button('Update Task', key=f'update_{index}'):
        st.rerun()

# タスクを削除する関数
def delete_task(index):
    if st.button('Delete', key=f'delete_{index}'):
        st.session_state['tasks'] = st.session_state['tasks'].drop(index)
        st.rerun()

# タスクを表示する関数
def display_tasks():
    sort_by = st.selectbox('Sort by', ['Deadline', 'Priority', 'Category'])
    sorted_tasks = st.session_state['tasks'].sort_values(by=[sort_by])
    for index, task in sorted_tasks.iterrows():
        with st.expander(f"Task: {task['Task']} - Deadline: {task['Deadline']} - Priority: {task['Priority']} - Category: {task['Category']}"):
            edit_task(index)
            delete_task(index)

# アプリのメイン関数
def main():
    st.title("タスク管理ツール")
    add_task()
    display_tasks()

    # タスクの編集
    #with st.expander("Edit Tasks"):
    #    edit_task(index)

if __name__ == '__main__':
    main()
