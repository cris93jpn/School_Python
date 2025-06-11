'''
クラス変数
'''

#クラス定義
class Product:
    #クラス変数
    sum = 0
    sho = []

    #クラスメソッド定義
    @classmethod
    def sales(cls):
        if cls.sum >= 1000000:
            return "売上好調"
        elif cls.sum >= 500000:
            return "売上半減"
        else:
            return "売上赤字"


    @classmethod
    def category(cls, ban):
        if ban >= 1000 and ban < 2000:
            return 'アウター'
        elif ban >= 2000 and ban < 3000:
            return 'インナー'
        elif ban >= 3000 and ban <= 4000:
            return 'ワンピース'
        elif ban >= 4000 and ban <= 4999:
            return 'パンツ'
        else:
            return None
        
    #コンストラクタ
    def __init__(self, ban, price, quan):
        self.ban = ban
        self.price = price
        self.cat = self.category(ban)
        self.quan = quan
        self.uri = 0


    
        
    #売上    
    def calc_sal(self):
        self.uri = self.price * self.quan
        Product.sum += self.uri
        Product.sho.append(self)
    
    #表示
    def show_detail(self):
        print('商品番号：', self.ban)
        print('単価：', self.price)
        print('売上個数：', self.quan)
        print('売上金額：', self.uri)

#メイン


while True:
    bango = int(input('商品番号を入力してください'))
    if bango == 9999:
        break
    if not (bango >= 1000 and bango <=4999):
        print('商品番号エラー。再入力してください。')
        continue

    category = Product.category(bango)
    print('商品分類名は：', category)

    #単価と売上個数入力
    nedan = int(input('単価を入力してください'))
    quantity = int(input('売上個数を入力してください：'))

