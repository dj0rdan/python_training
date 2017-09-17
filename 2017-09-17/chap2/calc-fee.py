#遊園地入場料計算

#人数入力
children = int(input("子供料金(13歳未満)は何人？"))
normal = int(input("通常価格(13~64歳)は何人？"))
elder = int(input("ジジイババア(65歳以上)は何匹おるんや"))
#集計

total_num = children+normal+elder
children_price =  children *500
normal_price = normal*1000
elder_price = elder*700
total_price = children_price+normal_price+elder_price
#割引対象か確認
if total_num >= 10:
    print("団体割引あるで")
    total_price = total_price*0.8
else:
    print("割引なんかねえ")

#結果
print("子供料金　: {0}人 × 500= {1}円".format(children, children_price))
print("子供料金　: {0}人 × 1000= {1}円".format(normal, normal_price))
print("子供料金　: {0}人 × 700= {1}円".format(elder, elder_price))
print("合計:{0}人 {1}円".format(total_num, total_price))
