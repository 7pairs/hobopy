import requests

endpoint = 'http://127.0.0.1:8000/todos'
expected_dic = {
    'id': 'aa0123456789',
    'title': 'ブライアン・シュリッター',
    'memo': 'シュレッダー',
    'priority': 3,
    'completed': False
}

def test_get_all_todosで指定のToDoが含まれていること():
    get_todos = requests.get(endpoint)
    actual_json = get_todos.json()
    assert expected_dic in actual_json
