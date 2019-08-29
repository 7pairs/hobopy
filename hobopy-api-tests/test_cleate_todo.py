import pytest
import json
import requests

endpoint = 'http://127.0.0.1:8000/todos'
headers_dic = {'content-type': 'application/json'}

# 組み合わせテストで使う値
empty = ""
mixed = "進化系 ダゲking。心技体、珠玉の日本最高LEVEL。"
symbol = "突破する♪シンデレラ♡ボーイ。"
new_line = '''真獅子の、

骨と牙'''
str_zero = "0"
nomal = '3'
out = '4'
int_num = 2

# 組み合わせパラメーター
case_palam_dic = [
    {'case': 'No0 Happy Path',
        'title': '本田圭佑', 'memo': 'のびしろ', 'priority': 1},
    {'case': 'No1 empty,new_line,empty',
        'title': empty, 'memo': new_line, 'priority': empty},
    {'case': 'No2 mixed,mixed,nomal',
        'title': mixed, 'memo': mixed, 'priority': nomal},
    {'case': 'No3 empty,symbol,str_zero', 
        'title': empty, 'memo': symbol, 'priority': str_zero},
    {'case': 'No4 symbol,new_line,nomal', 
        'title': symbol, 'memo': new_line, 'priority': nomal},
    {'case': 'No5 symbol,empty,str_zero', 
        'title': symbol, 'memo': empty, 'priority': str_zero},
    {'case': 'No6 str_zero,symbol,empty', 
        'title': str_zero, 'memo': symbol, 'priority': empty},
    {'case': 'No7 str_zero,mixed,int_num', 
        'title': str_zero, 'memo': mixed, 'priority': int_num},
    {'case': 'No8 new_line,symbol,nomal', 
        'title': new_line, 'memo': symbol, 'priority': nomal},
    {'case': 'No9 symbol, str_zero, empty', 
        'title': symbol, 'memo': str_zero, 'priority': empty},
    {'case': 'No10 str_zero, str_zero, out', 
        'title': str_zero, 'memo': str_zero, 'priority': out},
    {'case': 'No11 empty, str_zero, nomal', 
        'title': empty, 'memo': str_zero, 'priority': nomal},
    {'case': 'No12 new_line, str_zero, nomal', 
        'title': new_line, 'memo': str_zero, 'priority': nomal},
    {'case': 'No13 new_line, str_zero, str_zero', 
        'title': new_line, 'memo': str_zero, 'priority': str_zero},
    {'case': 'No14 str_zero, empty, nomal', 
        'title': str_zero, 'memo': empty, 'priority': nomal},
    {'case': 'No15 mixed, new_line, out', 
        'title': mixed, 'memo': new_line, 'priority': out},
    {'case': 'No16 mixed, symbol, str_zero', 
        'title': mixed, 'memo': symbol, 'priority': str_zero},
    {'case': 'No17 symbol, symbol, int_num', 
        'title': symbol, 'memo': symbol, 'priority': int_num},
    {'case': 'No18 str_zero, new_line, str_zero', 
        'title': str_zero, 'memo': new_line, 'priority': str_zero},
    {'case': 'No19 mixed, empty, empty', 
        'title': mixed, 'memo': empty, 'priority': empty},
    {'case': 'No20 empty, empty, int_num', 
        'title': empty, 'memo': empty, 'priority': int_num},
    {'case': 'No21 new_line, empty, out', 
        'title': new_line, 'memo': empty, 'priority': out},
    {'case': 'No22 new_line, mixed, empty', 
        'title': new_line, 'memo': mixed, 'priority': empty},
    {'case': 'No23 mixed, str_zero, int_num', 
        'title': mixed, 'memo': str_zero, 'priority': int_num},
    {'case': 'No24 empty, mixed, out', 
        'title': empty, 'memo': mixed, 'priority': out},
    {'case': 'No25 symbol,symbol,out',
        'title': symbol, 'memo': symbol, 'priority': out},
    {'case': 'No26 symbol,mixed,str_zero',
        'title': symbol, 'memo': mixed, 'priority': str_zero}
    ]
conditions_ids = ['conditions({})'.format(t['case']) for t in case_palam_dic]


@pytest.mark.parametrize("conditions_dic", case_palam_dic, ids=conditions_ids)
def test_cleate_taskで登録ができること(conditions_dic):

    actual = requests.post(
        endpoint,
        data=json.dumps(conditions_dic),
        headers=headers_dic
    )
    actual_json = actual.json()
    assert actual_json['id']
    assert actual_json['title'] == conditions_dic['title']
    assert actual_json['memo'] == conditions_dic['memo']
    assert actual_json['priority'] == conditions_dic['priority']
