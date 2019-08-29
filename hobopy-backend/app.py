from chalice import Chalice, NotFoundError
from chalicelib import database

app = Chalice(app_name='hobopy-backend')

# すべてのToDoを取得する
@app.route('/todos', methods=['GET'])
def get_all_todos():
    return database.get_all_todos()

# 指定されたIDのToDoを取得する
@app.route('/todos/{todo_id}', methods=['GET'])
def get_todo(todo_id):
    todo = database.get_todo(todo_id)
    if todo:
        return todo
    else:
        raise NotFoundError('Todo not found.')  # 404を返す
