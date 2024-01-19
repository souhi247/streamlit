import streamlit as st
import csv

FILEPATH = 'tasks.csv'

# CSV ファイルからタスクを読み込む関数
def read_tasks(file_path=FILEPATH):
    tasks = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            tasks.append(row)
    return tasks

# CSV ファイルにタスクを書き込む関数
def write_tasks(tasks, file_path=FILEPATH):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(tasks)

# 新しいタスクを追加する関数
def add_task():
    new_task = [st.session_state["new_task"], st.session_state["new_deadline"],
                st.session_state["new_priority"], st.session_state["new_category"]]
    tasks.append(new_task)
    write_tasks(tasks)

st.title("Daily Task Manager")
st.subheader("Manage your daily tasks and to-do's")

tasks = read_tasks()

# タスクの表示と削除
for index, task in enumerate(tasks):
    task_str = f"{task[0]} - Deadline: {task[1]} - Priority: {task[2]} - Category: {task[3]}"
    checkbox = st.checkbox(task_str, key=task[0])
    if checkbox:
        tasks.pop(index)
        write_tasks(tasks)
        del st.session_state[task[0]]
        st.experimental_rerun()

# タスクの追加フィールド
with st.form("new_task_form"):
    st.text_input("Enter a task", key="new_task")
    st.date_input("Deadline", key="new_deadline")
    st.selectbox("Priority", ['High', 'Medium', 'Low'], key="new_priority")
    st.text_input("Category", key="new_category")
    submitted = st.form_submit_button("Add Task")
    if submitted:
        add_task()