#印税を計算する関数
def calc_royality(price, sales, per):
    rate = per / 100  #印税率
    ro = int(price * sales * rate) #定価と発行部数と印税率を掛け、整数にする
    return ro

#ユーザから情報を入力してもらう
i = input("定価は？")
price = int(i)

i = input("発行部数は？")
sales = int(i)

i = input("印税率（％）は？")
per = float(i)

#結果を表示
v = calc_royality(price, sales, per)  #calc_royalityを呼び出す
print("印税は", v, "円です")
