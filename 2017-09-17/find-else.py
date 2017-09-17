#for構文でelseを使用
#食材一覧リスト
foodstuff = ["Banana", "Mango", "Fish", "Carrot", "cabbage"]

#マンゴーないか確認
for food in foodstuff:
    if food == "Mango":
        print("マンゴー入ってまっせ")
        break
else:
    print("ありやせん")
