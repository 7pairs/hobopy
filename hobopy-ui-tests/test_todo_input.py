from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select

# ToDo新規登録のテストシナリオ
class TestTodoInputSpaghetti:

    def test_ToDoを一件登録する(self, driver):
        # 画面を開く
        driver.get('http://127.0.0.1:8002/index.html')

        # 登録ボタンをタップする
        driver.find_element_by_id("new-todo").click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of(
                driver.find_element_by_class_name("modal-title"))
        )

        # 各入力欄に値を入力する
        driver.find_element_by_id(
            "modal-todo-title").send_keys("CATCH the GLORY")
        driver.find_element_by_id(
            "modal-todo-memo").send_keys("新時代、熱狂しろ！")
        priority_element = driver.find_element_by_id(
            "modal-todo-priority")
        priority_select_element = Select(priority_element)
        priority_select_element.select_by_value("3")

        # 登録ボタンをタップする
        driver.find_element_by_id("register-button").click()

        # 入力した内容が表示されていることを確認
        WebDriverWait(driver, 10).until(
            EC.visibility_of(driver.find_element_by_id("todo-list"))
        )
        assert_flg = False
        table_element = driver.find_element_by_id("todo-list")
        todo_title_elements = \
            table_element.find_elements_by_css_selector(
                "td:nth-of-type(2)")
        for todo_title_element in todo_title_elements:
            if todo_title_element.text.find("CATCH the GLORY"):
                assert_flg = True
        assert assert_flg
