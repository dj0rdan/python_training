#カラットからグラム数へ
#変換前の値
per_ct = 0.2
#入力を得る
user = input("何カラット？")
#浮動少数点数に
ct = float(user)
#計算
g = ct*per_ct
#結果
desc = "{0}カラット = {1}グラム".format(ct, g)
print(desc)