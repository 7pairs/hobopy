from chalice import BadRequestError, Chalice, NotFoundError
from chalicelib import database

app = Chalice(app_name='hobopy-backend')

# すべてのToDoを取得する
@app.route('/todos', methods=['GET'], cors=True)
def get_all_todos():
    return database.get_all_todos()

# 指定されたIDのToDoを取得する
@app.route('/todos/{todo_id}', methods=['GET'], cors=True)
def get_todo(todo_id):
    todo = database.get_todo(todo_id)
    if todo:
        return todo
    else:
        raise NotFoundError('Todo not found.')  # 404を返す

# Todoを登録する
@app.route('/todos', methods=['POST'], cors=True)
def create_todo():
    # リクエストメッセージボディを取得する
    todo = app.current_request.json_body

    # 必須項目をチェックする
    for key in ['title', 'memo', 'priority']:
        if key not in todo:
            raise BadRequestError(f"{key} is required.")

    # データを登録する
    return database.create_todo(todo)

# 指定されたIDのToDoを更新する
@app.route('/todos/{todo_id}', methods=['PUT'], cors=True)
def update_todo(todo_id):
    changes = app.current_request.json_body

    # データを更新する
    return database.update_todo(todo_id, changes)

# 指定されたIDのToDoを削除する
@app.route('/todos/{todo_id}', methods=['DELETE'], cors=True)
def delete_todo(todo_id):
    # データを削除する
    return database.delete_todo(todo_id)
