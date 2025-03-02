import streamlit as st
import func

todos = func.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + "\n")
    func.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("It works.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="1", label_visibility="hidden", placeholder="Add a new todo",
              on_change=add_todo, key="new_todo")
