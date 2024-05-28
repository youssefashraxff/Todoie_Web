def getTodos():
    with open('todos.txt','r') as file:
        todos = file.readlines()
    return todos

def setTodos(todos_arg):
    with open('todos.txt','w') as file:
        file.writelines(todos_arg)
