from selene.api import *
import time

# ToDo入力モーダルのPageクラス
class TodoInputModal:
    # UIのセレクタ
    TITLE_SELECTOR = "#modal-todo-title"
    MEMO_SELECTOR = "#modal-todo-memo"
    PRIORITY_SELECT_SELECTOR = "#modal-todo-priority"
    PRIORITY_OPTION_SELECTOR = {
        "高": "#modal-todo-priority :nth-child(1)",
        "中": "#modal-todo-priority :nth-child(2)",
        "低": "#modal-todo-priority :nth-child(3)"
    }
    REGISTER_BUTTON_SELECTOR = "#register-button"

    def __init__(self, driver=None):
        self.driver = driver
        driver.s(".modal-title").should(be.visible)

    # パラメータを入力する
    def input_param(self,
                    title_input_value,
                    memo_input_value,
                    priority_input_value):
        self.driver.s(
            self.TITLE_SELECTOR).set_value(title_input_value)
        time.sleep(1)
        self.driver.s(
            self.MEMO_SELECTOR).set_value(memo_input_value)
        self.driver.s(
            self.PRIORITY_SELECT_SELECTOR).click()
        self.driver.s(
            self.PRIORITY_OPTION_SELECTOR[priority_input_value])\
            .click()

    # 登録ボタンをクリックする
    def click_register(self):
        self.driver.s(self.REGISTER_BUTTON_SELECTOR).click()
