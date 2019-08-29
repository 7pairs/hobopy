__pragma__('alias', 'S', '$')

from model import Model
from view import View

class Presenter:
    # コンストラクタ
    def __init__(self):
        self._model = Model()
        self._view = View()
        self._bind()

    # イベントをバインドする
    def _bind(self):
        S('body').on('todos-updated', self._on_todos_updated)
        S('#input-form').on('show.bs.modal', self._on_show_modal)
        S('#register-button').on('click', self._on_click_register)
        S('#todo-list').on('click', '.toggle-checkbox', self._on_click_checkbox)
        S('#todo-list').on('click', '.delete-button', self._on_click_delete)

    # 初期表示処理
    def start(self):
        self._model.load_all_todos()

    # todos-updated受信時の処理
    def _on_todos_updated(self, event):
        self._view.render_todo_list(self._model.get_all_todos())

    # show.bs.modal受信時の処理
    def _on_show_modal(self, event):
        target_id = S(event.relatedTarget).attr('id')
        if target_id == 'new-todo':
            self._view.show_new_modal()
        elif target_id.startswith('update-'):
            todo_id = target_id[7:]
            todo = self._model.get_todo(todo_id)
            self._view.show_update_modal(todo)

    # register-buttonのclick受信時の処理
    def _on_click_register(self, event):
        input_data = self._view.get_input_data()
        if input_data['id']:
            self._model.update_todo(input_data['id'], input_data)
        else:
            self._model.create_todo(input_data)
        self._view.close_modal()

    # toggle-checkboxのclick受信時の処理
    def _on_click_checkbox(self, event):
        target_id = S(event.target).attr('id')
        if target_id.startswith('check-'):
            todo_id = target_id[6:]
            self._model.toggle_todo(todo_id)

    # delete-buttonのclick受信時の処理
    def _on_click_delete(self, event):
        target_id = S(event.target).attr('id')
        if target_id.startswith('delete-'):
            todo_id = target_id[7:]
            self._model.delete_todo(todo_id)
