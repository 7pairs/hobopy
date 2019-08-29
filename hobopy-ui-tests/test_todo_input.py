from pages.todo_list_page import TodoListPage

# ToDo新規登録のテストシナリオ
class TestTodoInputPageobj:

    def test_ToDoを一件登録する(self, driver):

        param_title = "CATCH the GLORY"
        param_memo = "新時代、熱狂しろ！"
        param_priority = "低"

        expected_title = "CATCH the GLORY"

        todo_list_page = TodoListPage(driver)

        # 画面を開く
        todo_list_page.open_page()

        # 登録ボタンをタップする
        todo_input_modal = todo_list_page.click_register()

        # 各入力欄に値を入力する
        todo_input_modal.input_param(
            param_title, param_memo, param_priority)

        # 登録ボタンをタップする
        todo_input_modal.click_register()

        # 入力した内容が表示されていることを確認
        assert todo_list_page.is_exist_title(expected_title)
