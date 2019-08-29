from chalice import NotFoundError
import pytest
import app

class TestGetTodo:
    expected_dic = {
        "id": 201,
        "title": "まんじゅう事件",
        "memo": "ごま大福だったし、ぼくは食べてないですよ。",
        'priority': 1,
        'completed': False,
    }

    def test_get_todoでToDoが取得できること(self, monkeypatch):
        monkeypatch.setattr(
            'chalicelib.database.get_todo',
            lambda _: self.expected_dic)
        actual_dic = app.get_todo(201)
        assert actual_dic == self.expected_dic

    def test_get_todoでToDoがないときにエラーが返ること(self, monkeypatch):
        with pytest.raises(NotFoundError):
            monkeypatch.setattr(
                'chalicelib.database.get_todo',
                lambda _: 0)
            app.get_todo(202)