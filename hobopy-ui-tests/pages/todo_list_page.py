from selene.api import *
from .todo_input_modal import TodoInputModal

# ToDo一覧のPageクラス
class TodoListPage:
    URL = 'http://127.0.0.1:8002/index.html'
    REGISTER_BUTTON_SELECTOR = "#new-todo"
    TODO_LIST_SELECTOR = "#todo-list tr"
    TODO_TITLE_CELL_SELECTOR = "td:nth-of-type(2)"

    def __init__(self, driver=None):
        self.driver = driver

    # ToDo一覧を新規で開く
    def open_page(self):
        self.driver.get(self.URL)

    # ToDo登録ボタンを入力する
    def click_register(self):
        self.driver.s(self.REGISTER_BUTTON_SELECTOR).click()
        return TodoInputModal(self.driver)

    # 引数のタイトルが画面上に存在するかチェックする
    def is_exist_title(self, title):
        exist_flg = False
        self.driver.s("#todo-list").should(be.visible)
        todo_elements = self.driver.ss(self.TODO_LIST_SELECTOR)
        for todo_element in todo_elements:
            todo_title_cell = todo_element.s(
                self.TODO_TITLE_CELL_SELECTOR)
            if todo_title_cell.text.find(title):
                exist_flg = True
        return exist_flg
