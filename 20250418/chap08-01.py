'''
chap08-01
'''

#クラス定義
class Shop:
    def __init__(self, in_ban, in_name, in_uri):
        #初期化用メソッド
        self.ban = in_ban
        self.name = in_name
        self.uri = in_uri

    #店の情報を表示
    def show_detail(self):
        print('店番：', self.ban)
        print('店名：', self.name)
        print('売上額：', self.uri)

    #売上額の結果を戻る
    def results(self):
        if self.uri <= 1000:
            res1 = '低迷'
        elif self.uri <= 5000:
            res1 = '現状維持'
        else:
            res1 = '好調'
        #戻り値
        return res1
    
#メイン
shp1 = Shop(201, '渋谷', 1500)
shp1.show_detail()
re = shp1.results()
print('売上判定は', re)
print()
    
shp2 = Shop(202, '新宿', 5800)
shp2.show_detail()
re2 = shp2.results()
print('売上判定は', re2)
