import streamlit as st
from todo_functions import getTodos,setTodos

todos = getTodos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    setTodos(todos)
   
st.title("Todoie")
st.write("Increase you <b>productivity</b>.",
          unsafe_allow_html=True)

for i,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(i)
        setTodos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='',placeholder="Add a new task.",
              on_change=add_todo,key="new_todo")    

#st.session_state
