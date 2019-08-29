# エイリアスを定義する
__pragma__('alias', 'S', '$')

from presenter import Presenter

presenter = Presenter()
S(presenter.start())
