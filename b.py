import streamlit as st
import csv

FILEPATH = 'tasks.csv'

def read_tasks(file_path=FILEPATH):
    with open(file_path, 'r') as file_original:
        tasks_original = file_original.readlines()
    return tasks_original

def write_tasks(tasks_original, file_path=FILEPATH):
    with open(file_path, 'w') as file_original:
        file_original.writelines(tasks_original)

def add_task():
	loc_task = st.session_state["new task"]
	tasks.append(loc_task + "\n")
	write_tasks(tasks)

st.title("Daily Task Manager")
st.subheader("This is a web version of the Daily Task Manager")
st.write("This app is used to manage your daily tasks and to-do's")

tasks = read_tasks()

for index, task in enumerate(tasks):
	checkbox = st.checkbox(task, key=task)
	if checkbox:
		tasks.pop(index)
		write_tasks(tasks)
		del st.session_state[task]
		st.experimental_rerun()

st.text_input(label="", placeholder="Enter a task",
              on_change=add_task, key="new task")