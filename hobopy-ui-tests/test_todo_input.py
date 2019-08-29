from selene.api import *

# ToDo新規登録のテストシナリオ
class TestTodoInputSelene:

    def test_ToDoを一件登録する(self, driver):
        # 画面を開く
        driver.get('http://127.0.0.1:8002/index.html')

        # 登録ボタンをタップする
        driver.s("#new-todo").click()
        driver.s(".modal-title").should(be.visible)

        # 各入力欄に値を入力する
        driver.s("#modal-todo-title").set_value("CATCH the GLORY")
        driver.s("#modal-todo-memo").set_value("新時代、熱狂しろ！")
        driver.s("#modal-todo-priority").click()
        driver.s("#modal-todo-priority :nth-child(3)").click()

        # 登録ボタンをタップする
        driver.s("#register-button").click()

        # 入力した内容が表示されていることを確認
        driver.s("#todo-list").should(be.visible)
        assert_flg = False
        todo_elements = driver.ss("#todo-list tr")
        for todo_element in todo_elements:
            if todo_element.s("td:nth-of-type(2)")\
                    .text.find("CATCH the GLORY"):
                assert_flg = True
        assert assert_flg
