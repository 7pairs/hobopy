import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selene.driver import SeleneDriver

@pytest.fixture(scope='function')
def driver():
    # テスト前処理
    options = ChromeOptions()
    # ヘッドレスモードを有効にする（次の行をコメントアウトすると画面が表示される）
    options.add_argument('--headless')

    # ChromeのWebDriverオブジェクトを作成する
    driver = Chrome(options=options,
                    executable_path='/usr/local/bin/chromedriver')

    # # Windowsの場合のChromeのWebDriverオブジェクトの作成はこちらのコードになります
    # # ChromeのWebDriverオブジェクトを作成する
    # options.binary_location = \
    #     "C:\\Program Files (x86)" \
    #     "\\Google\\Chrome\\Application\\chrome.exe"
    # driver = Chrome(
    #     options=options,
    #     executable_path=
    #     'D:\\Program\\chromedriver_win32\\chromedriver.exe')

    # テストケース実施
    yield driver

    # テスト後処理
    driver.close()
