#入力を得てインチをセンチへ
#変換前の値
per_inch = 2.54
#ユーザから入力を得る
user = input("何インチなの？")
#浮動小数点型へ変換
inch = float(user)
#計算
cm = inch*per_inch
#結果を表示
desc = "{0}インチ = {1}センチ".format(inch, cm)
print(desc)