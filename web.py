import streamlit as st
import functions

todos = functions.read_files()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_file(todos)


st.title("My todo app")
st.subheader("This is my todo app")
st.write("This app would help improve productivity...")
for index, tos in enumerate(todos):
    checkbox = st.checkbox(tos, key=tos)
    if checkbox:
        todos.pop(index)
        functions.write_file(todos)
        del st.session_state[tos]
        st.experimental_rerun()

st.text_input(placeholder="Type a new todo", label="", on_change=add_todo, key="new_todo")

