__pragma__('alias', 'S', '$')

from const import BASE_URL

class Model:
    # コンストラクタ
    def __init__(self):
        self._todos = []

    # 指定されたIDのToDoを取得する
    def get_todo(self, todo_id):
        for todo in self._todos:
            if todo['id'] == todo_id:
                return todo
        return None

    # すべてのToDoを取得する
    def get_all_todos(self):
        return self._todos

    # 全件取得のAPIを呼び出す
    def load_all_todos(self):
        S.ajax({
            'url': f"{BASE_URL}todos",
            'type': 'GET',
        }).done(
            self._success_load_all_todos
        ).fail(
            lambda d: alert('サーバーとの通信に失敗しました。')
        )

    # load_all_todos()成功時の処理
    def _success_load_all_todos(self, data):
        self._todos = data
        S('body').trigger('todos-updated')

    # ToDo登録のAPIを呼び出す
    def create_todo(self, data):
        S.ajax({
            'url': f"{BASE_URL}todos",
            'type': 'POST',
            'contentType': 'application/json',
            'data': JSON.stringify(data),
        }).done(
            self._success_create_todo
        ).fail(
            lambda d: alert('サーバーとの通信に失敗しました。')
        )

    # create_todo()成功時の処理
    def _success_create_todo(self, data):
        self._todos.append(data)
        S('body').trigger('todos-updated')

    # ToDo更新のAPIを呼び出す
    def update_todo(self, todo_id, data):
        send_data = {}
        for key in ['title', 'memo', 'priority', 'completed']:
            if key in data:
                send_data[key] = data[key]
        S.ajax({
            'url': f"{BASE_URL}todos/{todo_id}",
            'type': 'PUT',
            'contentType': 'application/json',
            'data': JSON.stringify(send_data),
        }).done(
            self._success_update_todo
        ).fail(
            lambda d: alert('サーバーとの通信に失敗しました。')
        )

    # update_todo()成功時の処理
    def _success_update_todo(self, data):
        for i, todo in enumerate(self._todos):
            if todo['id'] == data['id']:
                self._todos[i] = data
        S('body').trigger('todos-updated')

    # 完了状態を反転する
    def toggle_todo(self, todo_id):
        todo = self.get_todo(todo_id)
        self.update_todo(todo_id, {'completed': not todo['completed']})

    # ToDo削除のAPIを呼び出す
    def delete_todo(self, todo_id):
        S.ajax({
            'url': f"{BASE_URL}todos/{todo_id}",
            'type': 'DELETE',
        }).done(
            self._success_delete_todo
        ).fail(
            lambda d: alert('サーバーとの通信に失敗しました。')
        )

    # delete_todo()成功時の処理
    def _success_delete_todo(self, data):
        for i, todo in enumerate(self._todos):
            if todo['id'] == data['id']:
                self._todos.pop(i)
                break
        S('body').trigger('todos-updated')
