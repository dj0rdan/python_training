# for構文をフラグで分岐する
#弁当食材データからリストを作る

foodstuff = ["Banana", "Mango", "Fish", "Carrot", "cabbage"]

#マンゴーがないか確認
flag_found = False  #マンゴーがないかを確認する変数。初期値としてFalseを設定
for food in foodstuff:  #foodという変数に、foodstuffの値が1つずつ入る。繰り返しのたびに新しい値が入る。
    if food == "Mango":
        flag_found = True
        break

if flag_found:
    print("マンゴー入ってる！")
else:
    print("マンゴー入ってない")
