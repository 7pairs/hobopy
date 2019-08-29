from chalicelib import database

class TestBroadcastGaora:
    def test_broadcast_gaoraを実行する(self):
        expected_memo = "源田たまらん"
        actual_memo = database.broadcast_gaora(expected_memo)
        assert actual_memo == expected_memo

    def test_broadcast_gaoraのテストを失敗させる(self):
        expected_memo = "源田たまらん"
        actual_memo = database.broadcast_gaora(expected_memo)
        assert actual_memo == expected_memo + "!"  # ←ここで失敗するはず

    def test_broadcast_gaoraをホームランなし30文字で実行する(self):
        expected_memo = "去年の今頃の自分のことを考えたら、天国と地獄じゃないですけど"
        actual_memo = database.broadcast_gaora(expected_memo)
        assert actual_memo == expected_memo

    def test_broadcast_gaoraをホームランなし31文字で実行する(self):
        param = "同じ札幌で、負けて胴上げしているので、似ているなと思いました。"
        expected_memo = "『イッツ！』同じ札幌で、負けて胴上げしているので、" \
                        "似ているなと思いました。" \
                        "『ゴーンヌ!』"
        actual_memo = database.broadcast_gaora(param)
        assert actual_memo == expected_memo

    def test_broadcast_gaoraをホームランなしで実行する(self):
        expected_memo = "源田たまらん"
        actual_memo = database.broadcast_gaora(expected_memo)
        assert actual_memo == expected_memo

    def test_broadcast_gaoraをホームランありで実行する(self):
        param = "自分が満塁ホームランを打って、その後におかわりも打って"
        expected_memo = "自分が満塁『イッツ！』を打って、" \
                        "その後におかわりも打って『ゴーンヌ!』"
        actual_memo = database.broadcast_gaora(param)
        assert actual_memo == expected_memo

    def test_broadcast_gaoraを半角カナ付きで実行する(self):
        param = "３・２・１！ホームランｱｯﾌﾟﾙﾊﾟｰﾝﾁ!!"
        expected_memo = "３・２・１！『イッツ！』ｱｯﾌﾟﾙﾊﾟｰﾝﾁ!!" \
                        "『ゴーンヌ!』"
        actual_memo = database.broadcast_gaora(param)
        assert actual_memo == expected_memo

    def test_broadcast_gaoraをサロゲートペア文字付きで実行する(self):
        param = "ホームラン打ったら𩸽作ってあげる"
        expected_memo = "『イッツ！』打ったら𩸽作ってあげる" \
                        "『ゴーンヌ!』"
        actual_memo = database.broadcast_gaora(param)
        assert actual_memo == expected_memo