import streamlit
import streamlit as web
import functions
todos = functions.get_todos()

def add_todo():
    todo = web.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

web.title("My Todo App")
web.subheader("This my personal todo app.")
web.write("This app is to increase yout productivity")

for index,todo in enumerate(todos):
    checkbox = web.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del streamlit.session_state[todo]
        streamlit.experimental_rerun()

web.text_input(label="Enter New Todo",placeholder="add new todo...",
               on_change=add_todo,key='new_todo')
