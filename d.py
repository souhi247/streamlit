import streamlit as st
import pandas as pd


file_path = "tasks.csv"
tasks = pd.read_csv(file_path, encoding="shift-jis")

st.title("Daily Task Manager")
st.subheader("This is a web version of the Daily Task Manager")
st.write("This app is used to manage your daily tasks and to-do's")

for index, task in enumerate(tasks):
	checkbox = st.checkbox(task, key=task)
	if checkbox:
		tasks.pop(index)
		write_tasks(tasks)
		del st.session_state[task]
		st.experimental_rerun()

st.text_input(label="", placeholder="Enter a task",
              on_change=add_task, key="new task")